"""a=int(input())
if(a % 2==0):
    print("even")
else:
    print("odd")

a=int(input())
if(a<=35):
    print("poor student")
elif(a>=35 and a<=70):
    print("average student")
else:
    print("good student")

a=int(input())
b=int(input())
oper=input("add/sub/mult/divi")
if(oper== "add"):
     print(a+b)
elif(oper== "sub"):
     print(a-b)
elif(oper=="mult"):
     print(a*b)

elif(oper=="divi"):
     print(a/b)
else:
    print("no")
score=int(input())
if(score>=70):
   name= (input())
   dept=(input())
   loc= (input())
   print("eligible")
else:
    print("not eligible")"""
a=int(input("eng"))
b=int(input("tamil"))
c=int(input("phy"))
d=int(input("che"))
e=int(input("bio"))
add=a+b+c+d+e
avg=add/5
if(avg<=35):
    print("additional class")
else:
    print("your good")


   
    
