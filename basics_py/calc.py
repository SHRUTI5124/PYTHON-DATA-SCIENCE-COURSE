import os

while True:
    os.system("cls") #clear screen
    print("Calculator")
    print("1. +")
    print("2. -")
    print("3. ร")
    print("4. รท")
    print("5. %")
    print("6. โโ")
    print("7. **")
    print("8. EXIT")
    ch=input("enter ur choice:")
    match ch:
        case "1":
            a=int(input("enter a no.:"))
            b=int(input("enter another no.:"))
            print(f"{a}+{b}={a+b}")
        case "2":
            a=int(input("enter a no.:"))
            b=int(input("enter another no.:"))
            print(f"{a}-{b}={a-b}")
        case "3":
            a=int(input("enter a no.:"))
            b=int(input("enter another no.:"))
            print(f"{a}*{b}={a*b}")
        case "4":
            a=int(input("enter a no.:"))
            b=int(input("enter another no.:"))
            print(f"{a}/{b}={a/b}")
        case "5":
            a=int(input("enter a no.:"))
            b=int(input("enter another no.:"))
            print(f"{a}%{b}={a%b}")
        case "6":
            a=int(input("enter a no.:"))
            b=int(input("enter another no.:"))
            print(f"{a}//{b}={a//b}")
        case "7":
            a=int(input("enter a no.:"))
            b=int(input("enter another no.:"))
            print(f"{a}*{b}={a//b}")
        case "8":
            print("BYE ๐")
            break
        case _:
            print("invalid")
    