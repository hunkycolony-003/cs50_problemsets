def main():
    camel = str(input("camelCase : "))

    while negation(camel.islower()):
        camel = make_snake(camel)
    snake = camel
    print("snake_case:", snake )


def make_snake(name):
    index, upper = identify(name)
    return join_string(name, index, upper)


def identify(name):
        n = 0
        for i in name:
            n += 1
            if i.isupper():
                return n, i


def join_string(name, n, i):
    snake = ""
    for j in range(n-1):
        snake = snake + name[j]
    snake = snake + "_" + i.lower()
    for j in range(n, len(name)):
        snake = snake + name[j]
    return snake


def negation(statement):
     if statement:
        return False
     else:
         return True

main()
