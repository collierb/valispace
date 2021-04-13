import sys

# functions
def first_func():
    x = second_func() + fifth_func()
    return x


def second_func():
    x = 5 - fourth_func()
    return x


def third_func():
    x = first_func() * second_func()
    return x


def fourth_func():
    x = 7
    return x


def fifth_func():
    x = 90 + 1
    return x


def main():
    """Ask user for a formula using our functions above and print result"""
    print("available functions are:\nf1,f2,f3,f4,f5")
    query = input("equation?\n> ")
    f1 = first_func()
    f2 = second_func()
    f3 = third_func()
    f4 = fourth_func()
    f5 = fifth_func()
    try:
        print(eval(query))
    except:
        print("user input error, try again...")


if __name__ == "__main__":
    try:
        while True:
            main()
    except KeyboardInterrupt:
        print("\nGoodbye!")
        sys.exit(0)
