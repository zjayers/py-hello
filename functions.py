def increment(number: int, by: int = 1) -> tuple:
    return number, number + by


answer: tuple = increment(number=2, by=3)
print(answer)


# xargs
def multiply(*numbers):
    total = 1
    for number in numbers:
        total += number
    return total


print(multiply(2, 3, 4, 5))


# xxargs
def save_user(**user):
    print(user["id"], user["name"])


save_user(id=1, name="admin")
