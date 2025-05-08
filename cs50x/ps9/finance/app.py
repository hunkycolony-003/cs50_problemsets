import os

from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from werkzeug.security import check_password_hash, generate_password_hash

from helpers import apology, login_required, lookup, usd

# Configure application
app = Flask(__name__)

# Custom filter
app.jinja_env.filters["usd"] = usd

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///finance.db")


@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/")
@login_required
def index():
    """Show portfolio of stocks"""

    # Initialises variables
    stocks = []
    total = 0

    # Selects symbols of stock of that user
    symbols = db.execute("SELECT symbol FROM portfolio WHERE user_id = ?", session["user_id"])

    # Iterates over each symbol
    for symbol in symbols:

        symbol = symbol["symbol"]

        # Gets the number of total shares owned
        shares = db.execute("SELECT shares FROM portfolio WHERE symbol = ? AND user_id = ?",
                            symbol, session["user_id"])[0]["shares"]

        # Gets the current price of each share
        current_price = lookup(symbol)["price"]

        # Appends the stocks into 'stocks' with the details of each stock
        stocks.append({"symbol": symbol,
                       "shares": shares,
                       "price": usd(current_price),
                       "total": usd(shares * current_price)})

        # Calculates the total price value over all stocks
        total += current_price * shares

    # Gets the cash left in user's account
    cash = db.execute("SELECT cash FROM users WHERE id = ?", session["user_id"])[0]["cash"]

    # Calculates the total wealth of the user
    grand_total = total + cash

    return render_template("index.html",
                           portfolio={"stocks": stocks,
                                      "total": usd(total),
                                      "cash": usd(cash),
                                      "grand_total": usd(grand_total)})


@app.route("/buy", methods=["GET", "POST"])
@login_required
def buy():
    """Buy shares of stock"""

    if request.method == "POST":
        symbol = request.form.get("symbol")

        shares = request.form.get("shares")
        try:
            if int(shares) < 1 or not shares.isdigit() or int(shares) != float(shares):
                return apology("Not expected value of Share", 400)
        except ValueError:
            return apology("Enter Integer No. of Shares", 400)
        shares = int(shares)

        if not (symbol and shares):
            return apology("Please Enter Symbol/Shares")

        stock = lookup(symbol)
        if not stock:
            return apology("Invaid Symbol", 400)

        total_price = stock["price"] * shares
        cash = db.execute("SELECT cash FROM users WHERE id = ?", session["user_id"])[0]["cash"]
        if cash < total_price:
            return apology("Not enough Cash !", 400)

        db.execute(
            "INSERT INTO portfolio (user_id, symbol, shares) VALUES (?, ?, ?) ON CONFLICT (user_id, symbol) DO UPDATE SET shares = shares + ?",
            session["user_id"], symbol.upper(), shares, shares)

        db.execute("UPDATE users SET cash = ? WHERE id = ?", cash - total_price, session["user_id"])
        db.execute("INSERT INTO transactions (user_id, symbol, price, shares) VALUES (?, ?, ?, ?)",
                   session["user_id"], symbol.upper(), stock["price"], shares)

        flash("Syccesfully Bought!")
        return redirect("/")

    return render_template("buy.html")


@app.route("/history")
@login_required
def history():
    """Show history of transactions"""

    transactions = db.execute("SELECT * FROM TRANSACTIONS WHERE user_id = ? ORDER BY time DESC",
                              session["user_id"])
    if not transactions:
        transactions = []
    else:
        for i in range(len(transactions)):
            transactions[i]["price"] = usd(transactions[i]["price"])

    return render_template("history.html", transactions=transactions)


@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":
        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 403)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 403)

        # Query database for username
        rows = db.execute(
            "SELECT * FROM users WHERE username = ?", request.form.get("username")
        )

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(
            rows[0]["hash"], request.form.get("password")
        ):
            return apology("invalid username and/or password", 403)

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

        # Redirect user to home page
        flash("Logged in!")
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")


@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")


@app.route("/quote", methods=["GET", "POST"])
@login_required
def quote():
    """Get stock quote."""

    if request.method == "POST":
        stock = lookup(request.form.get("symbol"))
        if stock:
            stock["price"] = usd(stock["price"])
            return render_template("quoted.html", stock=stock)
        return apology("Invalid ticker Symbol", 400)

    return render_template("quote.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        confirmation = request.form.get("confirmation")

        for i in [username, password, confirmation]:
            if not i:
                return apology(f"{i} Not Found !", 400)

        if password != confirmation:
            return apology("Passwords Don't Match", 400)

        try:
            db.execute("INSERT INTO users (username, hash) VALUES (?, ?)",
                       username, generate_password_hash(password))
        except ValueError:
            return apology("Username Already Exists", 400)

        return redirect("/login")

    return render_template("register.html")


@app.route("/sell", methods=["GET", "POST"])
@login_required
def sell():
    """Sell shares of stock"""
    if request.method == "POST":
        symbol_to_sell = request.form.get("symbol")
        shares_to_sell = request.form.get("shares")

        if not (symbol_to_sell and shares_to_sell):
            return apology("Input not recieved", 400)
        price = lookup(symbol_to_sell)
        if not (symbol_to_sell and shares_to_sell and price):
            return apology("Symbols/Shares Not recieved", 403)
        price = price["price"]

        shares_present = db.execute("SELECT DISTINCT shares FROM portfolio WHERE user_id = ? AND symbol = ?",
                                    session["user_id"], symbol_to_sell)[0]["shares"]
        if not shares_present:
            return apology(f"{symbol_to_sell} Not Found in Portfolio")
        if shares_present < int(shares_to_sell):
            return apology("Doesn't own enough shares")

        db.execute(
            "INSERT INTO transactions (user_id, symbol, price, shares, type) VALUES (?, ?, ?, ?, ?)",
            session["user_id"], symbol_to_sell, price, shares_to_sell, "sell"
        )
        db.execute(
            "UPDATE portfolio SET shares = shares - ? WHERE user_id = ? AND symbol = ?",
            shares_to_sell, session["user_id"], symbol_to_sell
        )
        db.execute("UPDATE users SET cash = cash + ?", float(price) * int(shares_to_sell))

        flash("Successfully Sold!")
        return redirect("/")

    symbols_present = db.execute("SELECT symbol FROM portfolio WHERE user_id = ?",
                                 session["user_id"])
    symbols_present = [symbol["symbol"] for symbol in symbols_present]

    return render_template("sell.html", symbols=symbols_present)


@app.route("/reset", methods=["GET", "POST"])
@login_required
def reset():
    if request.method == "POST":
        previous = request.form.get("previous")
        new = request.form.get("new")
        confirm = request.form.get("new_confirm")

        previous_original = db.execute("SELECT hash FROM users WHERE id = ?",
                                       session["user_id"])[0]["hash"]

        if not check_password_hash(previous_original, previous):
            return apology("Old password Doesn't match", 403)
        if new != confirm:
            return apology("Conformation Doesn't match", 403)

        db.execute("UPDATE users SET hash = ?", generate_password_hash(new))

        flash("Password Changed Successfully!")
        return redirect("/")
    return render_template("reset.html")
