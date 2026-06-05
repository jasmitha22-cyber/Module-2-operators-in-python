#arithmetic
x = 4
y = 2
print(x+y)
print(x-y)
print(x*y)
print(x/y)
print(x**3)
print(x%y)
print(x//y)
#comprastion
print(x==y)
print(x!=y)
print(x<y)
print(x>y)
print(x<=y)
print(x>=y)
#assignment
a=6
a += 4
a -= 5
a *= 5
a /= 6
print(a)
#logical
j=5
print(j>3 and j<10)
print(j<6 or j>10)
print(not(j==5 and j>3))
#bitwise
print(4 & 2)
print(6 | 5)
print(~6)
print(8 ^ 9)
print(3 >> 6)
print(4<<8)
#identity
d=[1,2,3,4]
e=[5,6,7,8]
f=d
print( d is e)
print( d is not e)
print(d is f)
#membership
v=["apple","banana"]
print("apple" in v)
print("banana" not in v)
#ternary
q = 80
print("big" if q > 60 else "small")
