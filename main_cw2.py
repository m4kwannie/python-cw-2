my_name = input("enter your name")

my_age = input("enter your age")

print(f"my name is {my_name} and i am {my_age} years old")

first_number = int(input("enter your first number: "))

second_number = int(input("enter your second number: "))

operation = input("enter your operation type: ")
if operation == "+" :
    print(first_number + second_number)

elif operation == "-" :
    print(first_number - second_number)

elif operation == '*' :
    print(first_number - second_number)

elif operation == "/":
    print(first_number / second_number)

else:
    print("the operation is not valid")

bus_capacity = 50
inside_bus = int(input("people inside: "))
want_bus = int(input("people want in: "))
empty_seats = bus_capacity -inside_bus
if empty_seats>= want_bus:
    print("there is space inside")
else: 
    print("the bus is full")