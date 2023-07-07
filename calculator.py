import math
print("be mashin hasab khosh amadid:)")
y=input("mashin hesab pishrafte ya sade(p=pishrafte,s=sade)?")
if y=="s":
    print("1.+")
    print("2.-")
    print("3./")
    print("4.*")
    x=int(input("yeki az dastorat bala ra entekhab konid(1 ta 4): "))
    num1=int(input("addad aval ra vared konid: "))
    num2=int(input("addad dovom ra vared konid: "))
    if x==1:
        print(num1+num2)
    if x==2:
        print(num1-num2)
    if x==3:
        print(num1/num2)
    if x==4:
        print(num1*num2)
if y=="p":
    print("1.Radical")
    print("2.sin")
    print("3.cot")
    print("4.cos")
    print("5.tan")
    print("6.factorial")
    z=int(input("yeki az dastorat bala ra entekhab konid: "))
    num=int(input("addad ra vared konid: "))
    if z==1:
        print(math.sqrt(num))
    if z==2:
        print(math.sin(num))
    if z==3:
        print(math.cos(num)/math.sin(num))
    if z==4:
        print(math.cos(num))      
    if z==5:
        print(math.tan(num))
    if z==6:
        print(math.factorial(num))