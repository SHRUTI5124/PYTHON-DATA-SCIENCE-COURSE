''' wap to create a funvtion that will generate random 3 dice no. 
if all 3 matches display "u win" else display "u lose/try again"'''
import random as rd

def dice():
    l=['1','2','3','4','5','6']
    r=rd.choices(l, k=3)
    if(r[0]==r[1]==r[2]):
        return r,"u win🎁"
    else:
        return r,"better luck next time😢"

ans,msg=dice()
print("Rolling the dice.....")
print(" ".join(ans))
print(msg)