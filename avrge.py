print("WELCOME  SO MUCH TO KOLEOS PYTHON FIELD")
a = input(print("ENTER THE FIRST NUMBER: "))
b = input(print("ENTER THE SECOND NUMBER: "))
c= input(print("ENTER THE THIRD NUMBER: "))
if a.isdigit() and b.isdigit() and c.isdigit:
    a=float(a)
    b = float(b)
    c = float(c)
    print("The average of the number entered is: ", (a+b+c)/3)
else:
    print("CHECK YOUR INPUT AND TRY AGAIN!!!")
