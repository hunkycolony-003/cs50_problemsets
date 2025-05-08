temp = input("Enter your expression: \n")
temp = temp.split(sep = " ", maxsplit = 2)

x, y, z = temp

x = float(x)
z = float(z)

match y :
    case "+" :
        print(float(x+z))
    case "-" :
        print(float(x-z))
    case "*" :
        print(float(x*z))
    case "/" :
        print(round(x / z, 1))
