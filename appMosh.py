# # 2 ways to impoprt packages

# from calendar import c
# import ecommerce.shipping

# ecommerce.shipping.calcShipping()

# # or a less verbose way

# from ecommerce.shipping import calcShipping

# calcShipping()


# from utils import findMax
# print(findMax([5,90,9000,10,5]))


# import converters

# print(converters.lbsToKg(180))

# #even better below

# from converters import kgToLbs

# print(kgToLbs(100))

#holycrap this is awesome!

# #inheritance

# class Mammal:
#     def walk(self):
#         print('walk')
    

# class Dog(Mammal):
#     def bark(self):
#         print('bark!')


# class Cat(Mammal):
#     pass

# Vega = Dog()
# Sketch = Cat()

# Vega.bark()
# Vega.walk()
# Sketch.walk()



# 
# class Person:
#     def __init__(self, name):
#         self.name = name
#     def talk(self):
#         print(f'Hi i am {self.name}!')


  

# chad = Person('chad')
# chad.talk()
# amy = Person('amy')
# amy.talk()
# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y

#     def move(self):
#         print('move')


#     def draw(self):
#         print('draw')

# point = Point(10,20)
# print(point.y)


#test by jlt 2022sep23 
# def myemoj(str):
#     words = str.split(" ")
#     emojis = {
#         ':)' : '😄',
#         ':(' : '😭'
#     }
#     greet = ''
#     for word in words:
#         greet += emojis.get(word, word) + " "
#     return greet


# userinput = input('>')
# print(myemoj(userinput))


# message = input("> ")
# words = message.split(" ")
# emojis = {
#     ':)' : '😄',
#     ':(' : '😭'
# }
# greet = ''
# for word in words:
#     greet += emojis.get(word, word) + " "
# print(greet)

# phnum = list(input("phone: "))
# numdic = {
#     '1' : "one",
#     '2' : "two",
#     '3' : "three",
#     '4':  "four"
# }
# ans = ""
# for num in phnum:
#     ans += numdic[num] + " "

# print(ans)



# numbs = [12,5,8,900,50,900,403,1000,8]
# numbs.sort()
# print(numbs)
# index = 0 - len(numbs)
# for num in numbs:
#     if num == numbs[index + 1]:
#         numbs.remove(num)
#     else: 
#         index += 1
# print(numbs)

# def findmax(arr):
#     big = arr[0]
#     for num in arr:
#         if num > big:
#             print(num)
#             big = num
#     return big
# print(findmax([12,5,8,900,50,403,1000]))


# nums = [5,2,5,2,2]
# for num in nums:
#     for inner in
#  #   print('x' * num)


# carinput = ''
# started = False
# #while carinput != 'quit':
# while True:
#     carinput = input("> ").lower()
#     if carinput == 'start' and started == False:
#         print('lets go!!!')
#         started = True
#     elif carinput == 'start' and started == True:
#         print('car already started')
#     elif carinput == 'stop' and started == True:
#         print('slowdown')
#         started = False
#     elif carinput == 'stop' and started == False:
#         print('already stopped')
#     elif carinput == 'help':
#         print("""
# start - to start car 
# stop - to stop car
# quit - to quit program """)
#     elif carinput == 'quit':
#         break
#     else:
#         print('sorry dont understand that')
#         break


    # if carinput != 'start' or carinput != 'stop' or carinput != 'quit':
    #     print('sorry i dont know that command') 

