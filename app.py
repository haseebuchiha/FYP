# if divisble by 3 fizz
# if divisible by 5 buzz
# if divisible by 3 and 5 fizz buzz
# else return itself


def fizz_buzz(input: int):
    if input % 3 == 0 and input % 5 == 0:
        print("Fizz Buzz")
    elif input % 3 == 0:
        print("Fizz ")
    elif input % 5 == 0:
        print("Buzz")
    else:
        print(input)


x = int(input("Enter value: "))
fizz_buzz(x)
