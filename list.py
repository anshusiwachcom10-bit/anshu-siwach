# # list
# # indexcing start(0)
# fruits=["apple","mango","banana"]
# print (fruits[0])
# # iterating overlist
# fruits=["apple","mango","date"]
# for fruit in fruits :
#  print(fruits)
# #  range
# for i in range(1,4):
#  print(i)
# #  mutable(append)
# fruits=["applre","mango","date"]
# fruits ,apped["banana"]

# tuple
# num=(10,20,30,40)
# print(num)

# fruit=("apple","cherry")
# print(fruits[0])

# #set(es m union value store krta h)
# num={1,2,3}
# print(num)

# #dictionary (es m key value hote hai)
# person={"name","anshu","age",17}
# print(person)

# #while loop
# num= 2
# while num >= 20:
#  print(num)
#  num +=2

#  num=1
#  while num <= 10:
#   print(num)  
#   num +=1 

# num=1
# while num <=100:
# print(num)
# num +=1
 
#  num=1
# while num <=10:
# print(7*num)
# num +=1

# #for loop
# fruits=("apple","banana","cherry")
# for fruit in fruits:
#     print(fruit)

# num=6
# for num in range(6,12):
#     print(num)
# #2 table
# for num in range(2,21,2):
#     print(num)

# num=5 
# for num in range(5,51):
#     print(num)

#     #leap year  
# year=int(input("enter a year"))
# if (year % 4==0):
#  print("leap year")
# else:
#  print("not a leap year")

# nested loop
# for i in range(1,4):              
#  for j in range(1,4):  
#    for k in range(1,4):             
#     print(i*j*k)
 
# for i in range(1,4):
#  for j in range(1,5):
#   print(i)

# for i in range(1,4):
#      for j in range(1,4):
#         print(j) 

# for i in range(1,6):
#     for j in range(i):
#         print("*",end=" ")
#     print()


# for i in range(6,0,-1):
#     for j in range(i):
#         print("*",end=" ")
#     print() 

# num =5 

# for i in range(1,6):
#     for j in range(i ):
#         print("num" ,end=" ")
#     print()
# for i in range(1,6):
#     for j in range(1,6):
#         if i==1 or i==5 or j==1 or j==5:
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()
# function
# a="hello"
# b="student!" 
# print(a+", "+b)

# def my_name( name):
#     print(name)
# my_name("anshu")
def sumOFTwo(a,b):
    sum = a+b
    print(sum)

    sumOFTwo(10,20)