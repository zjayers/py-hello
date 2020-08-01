def fizz_buzz(inp: int):
    if (inp % 3 == 0) and (inp % 5 == 0):
        return "FizzBuzz"
    if inp % 3 == 0:
        return "Fizz"
    if inp % 5 == 0:
        return "Buzz"
    return inp


print(fizz_buzz(3))
print(fizz_buzz(5))
print(fizz_buzz(15))
print(fizz_buzz(7))
