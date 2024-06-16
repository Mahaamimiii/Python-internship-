#calculator
def add(n1,n2):
    return n1+n2
def sub(n1,n2):
    return n1-n2
def mul(n1,n2):
    return n1*n2
def div(n1,n2):
    return n1/n2
print("Enter the operation")
op= int(input("1.add 2.subtract 3.multiply 4.divide"))
n1 = int(input("enter num1:"))
n2 = int(input("enter num2:"))
if op==1:
    print(n1,"+",n2,"=",add(n1,n2))
elif op==2:
    print(n1,"-",n2,"=",sub(n1,n2))
elif op==3:
    print(n1,"*",n2,"=",mul(n1,n2))
elif op==4:
    print(n1,"/",n2,"=",div(n1,n2))
else:
    print("invalid")
