#Question 5
x=int(input("Enter a value "))
y=int(input("Enter a value "))
if x>=1 and x<=10:
    if y>=1 and y<=10:
        z=x+y
        result=(z+30)
        print("final output",result)
    else: 
        print("condition not met")
else:
    print("X value is incorrect ")
    


