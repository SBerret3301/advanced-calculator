name = input("please enter your name : ")
print("Hello",name,", With this program, you will be able to perform some simple operations on two numbers, so please follow the following instructions: for sum use +, Difference process use -, multiplication use * , reel division use / , integer division use %","\U0001F917")
x = float(input(" write the first number :"))
op = input(" choose an operation :")
y = float(input(" write the second number :"))
while op != "+" and op != "-" and op != "*" and op != "/" and op != "%" :
    op = input("write corectly the operation : ")
if op == "+" :
    print(x, "+" ,y, "=" , x + y)
if op == "-" :
    print(x, "-" ,y, "=" ,x - y)
if op == "*" :
    print(x, "*" ,y, "=" ,x * y)
while y == 0 and (op == "/" or op == "%"):
   y = float(input(" Write the second number different from 0 : "))
if y != 0 :
  if op == "/" :
    print(x, "/" ,y, "=" ,x / y)
  elif op == "%" :
    print("the rest of division : " ,x % y)