'''n = int(input("enter the range number:"))
sum_of_number = 0
for i in range(1,n+1):
  sum_of_number=sum_of_number + i
print(sum_of_number)'''



'''num = 9275
new = 0
while num > 0:
  digit = num%10
  new = new * 10 + digit
  num = num//10
print(new)
'''


'''ni = 0
n= 5421
while n > 1:
  d = n%10
  ni = ni+d
  n = n//10
print(ni)
r = ni%10
r = r + ni//10
print(r)
v = r%10
v = v + r//10
print(v)'''


n = 5421
while n >= 10 :
  sum_ = 0 
  temp = n
  while temp > 0:
    ex = temp%10
    sum_ = sum_ + ex
    temp = temp//10
    n = sum_
print(n)
 


    







