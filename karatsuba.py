import math
# karatsuba乘法函数
def karatsuba(input1,input2):
    if (input1==0) or (input2==0) : 
        return 0
    length=max(math.floor(math.log10(input1))+1,math.floor(math.log10(input2))+1)
    if length==1:
        return input1*input2
    n2=length//2
    length=int(n2*2)
    #a,b=divmod(input1,int(math.pow(10,n2)))
    #c,d=divmod(input2,int(math.pow(10,n2)))
    a,b=divmod(input1,10**n2)
    c,d=divmod(input2,10**n2)
    ac=karatsuba(a,c)
    bd=karatsuba(b,d)
    adplusbc=karatsuba((a+b),(c+d))-ac-bd
    xy=10**length*ac+10**n2*adplusbc+bd
    return xy

def check(input1,input2):
    a=karatsuba(input1,input2)
    b=input1*input2
    print("%s"%a)
    print("%s"%b)
    return