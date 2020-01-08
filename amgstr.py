#armstrong number checking
number=input("enter the number:")
length=len(number)
list1=[]
val=0
for num in number:
    print(num)
    val=val+int(num)**length
print(val)
if str(val)==str(number):
    print("yes armstrong")
else:
    print("no armstrong")


        
    
    
        





