
n= int(input("Enter the number: "))
i=1
if n%2==0:
     print("n is even")
else:
   print("n is odd")
print("Multipilcation table of : ")
for i  in range(1,11) :
    print(n, '*' ,i ,'=', n*i)
    i=i+1
    