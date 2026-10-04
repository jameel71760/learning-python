name = input("what is your name")
age = int(input("how old are you"))

print("hello", name)
print("you are", age, "years old")

print("in 5 years, you will be", age + 5, "years old")
print("in 10 years, you will be", age + 10, "years old")
print("in 20 years, you will be", age + 20, "years old")


name = input("what is your name")
age = int(int("how old are you"))

print("in 5 years, you will be", age + 5, "years old")
print("in 10 years, you will be", age + 10, "years old")
print("in 20 year, you will be", age + 20, "years old")
print("in 12 years, you will be", age + 12, "years old")


def age(age):
    return age - 18
age = 40
answer = age(age)
print("in 2040 you will be", answer, "years old")