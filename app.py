# if divisble by 3 fizz
# if divisible by 5 buzz
# if divisible by 3 and 5 fizz buzz
# else return itself


def fizz_buzz(input: int):
    if (input % 3 == 0) and (input % 5 == 0):
        return "Fizz Buzz"
    if input % 3 == 0:
        return "Fizz"
    if input % 5 == 0:
        return "Buzz"

    return input


x = int(input("Enter value: "))
print(fizz_buzz(x))
