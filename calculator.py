#python program to form a simple calculator
print("1-Addition")
print("2-Subtraction")
print("3-Multiplication")
print("4-Division")
option=int(input("choose any one above operation: "))

if(option in[1,2,3,4]):
    num1=int(input("enter first number:"))  #we use int to convert all given input into integer
    num2=int(input("enter second number:"))
    
if(option==1):  
  result=num1+num2
elif(option==2):
  result=num1-num2
elif(option==3):
  result=num1*num2
elif(option==4):
 result=num1//num2  #if we use int, then we should use //(double forward slas) for div.
                         #single / used for float
else:
   print("invalid operation entered.")

print("The result of operation is {}".format(result))
