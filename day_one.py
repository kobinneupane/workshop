import asyncio
# num_array = []
# for x in range(1,20):
#     if x%2 == 0:
#         num_array.append(x)
        
# print("even number = ", num_array)
# num_array.sort(reverse = True)
# print(num_array)



# string_array = ["ram","shyam","hemal","sheeta","ooooram"]
# print(len(string_array))
# new_array = []
# for x in range(1,len(string_array)):
#     if x%2 == 0:
#         new_array.append(x)
# string_array.pop(1)
# string_array.insert(1,"shyam rai")
# print(string_array)        
        
# print("even number = ", new_array)



# for index, value in enumerate(string_array):
#     if index % 2 == 0:
#         print(f"this is {index} index and value is {value}")
    
    





# Wap to convert temperature to and from celcius and  fahrenhiet. let celsius value = 60
# c = input("enter celsius")
# f = (c/5)*9 +32
# print(f)




# anonymousFunction = lambda x, y: x+y
# print(anonymousFunction(10,4))







# def outerFunction(x):
#     def innerFunction(y):
#         return x * y
#     return innerFunction

# closure_instance = outerFunction(4)

# result = closure_instance(5)
# print("result = ", result)






# def aFunction(a,b):
#     try:
#         result = a/b
#         return result
#     except ZeroDivisionError:
#         print("Error: Divisible xero is not allowed")
#         return None
#     except Exception as e:
#         print(f"This is an error: {e}")
        
# print(aFunction(1,0))


# take the input from the user
# def bFunction(a,b):
#     try:
#         result = a/b
#         return result
#     except ZeroDivisionError:
#         print("Error: Divisible zero is not allowed")
#         return None
#     except Exception as e:
#         print(f"This is an error: {e}")

# a =int(input("Enter the value of a"))
# b =int(input("Enter the value of b"))

# resultt = bFunction(a,b)
# print(resultt)





# celsius to fahrenhiet using function

# n = int(input("to convert celsiud to fahrenhiet : Enter 1 or to convert fahrenhiet to celsius enter 2   "))

# def celsiusToFahrenhiet(c):
#     f=(c*9/5) + 32
#     return f

# def fahrenhietToCeslius(f):
#     c = (f-32)* 5/9
#     return c

# if n==1:
#     c = int(input("Enter the celsius value"))
#     result = celsiusToFahrenhiet(c)
#     print(result)
    
# if n==2:
#     f = int(input("Enter the fahrenhiet"))
#     resultt = fahrenhietToCeslius(f)
#     print(resultt)



# async def getData():
#     print("loading")
#     await asyncio.sleep(5)
#     print("i'm here after 5 seconds")
    
# asyncio.run(getData())





