def pow(x, n):
   if n ==1 :
       return x
   elif n ==0:
       return  1
   return x*pow(x,n-1)

print(pow(42,0))
print(pow(1, 10))
print(pow(2,5))
print(pow(7, 2))
