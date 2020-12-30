#Question 6
x=eval(input("Enter a value "))
y=type(x)
print("The data type of input value is: ",y)

#alternative method question - How to get reults with simply int, float or str instead of <class 'str'>
x=eval(input("Enter a value "))
y=type(x)
if type(x) = "<class 'str'>":
    print("The data type of input value is string")
elif type(x) = "<class 'int'>":
    print("The data type of input value is int")
elif type(x) = "<class 'float'>":
    print("The data type of input value is float")
else:
print("The data type of input value is unknown")
