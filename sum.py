from cs50 import get_int

num1 = get_int("Enter num one = ")
num2 = get_int("Enter num two = ")

print(f"Sum= {num1+num2}" )


x = int(input("enter x="))
y = int(input("enter y="))

# print(f"Sum= {x+y}" )

if x < y :
    print("x is less than y")
elif x > y:
    print("x is greater than y")
else:
    print("x is equal to y")