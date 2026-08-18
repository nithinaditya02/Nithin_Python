#question 1 (even numbers from 1 to 100)

# for i in range(1,101):
#     if i%2==0:
#         print(i)




#question 2 (odd numbers from 1 to 100)

# for i in range(1,101):
#     if i%2!=0:
#         print(i)




#question 3 (print all multiples of 5 between 1 to 100)

# for i in range(1,101):
#     if i%5==0:
#         print(i)




#question 4 (find the sum of all numbers from 1 to 100)

# sum =0
# for i in range (1,101):
#     sum=sum+i
# print(f"sum of all numbers from 1 to 100 is: {sum}") 




#question 5 ( find the sum of all even numbers from 1 to 100)
        
# sum =0
# for i in range(1,101):
#     if i%2==0:
#         sum=sum+i
# print(f"sum of all even numbers from 1 to 100 is: {sum}")




#question 6 ( take a number from user and calculate its factorial)

# num = int(input("enter a number:"))
# factorial = 1
# for i in range(1,num+1):
#     factorial = factorial * i
# print(f"factorial of {num} is: {factorial}")




#question 7 (check whether a number is palindrome or not)

# num = int(input("enter a number:"))
# temp = num
# rev = 0
# while num>0:
#     digit = num%10
#     rev = rev*10 + digit
#     num = num//10    

# if temp == rev:
#     print(f"{temp} is a palindrome")
# else:
#     print(f"{temp} is not a palindrome")






#question 8 (take a number from user and check whether its prime or not)

# num = int(input("enter a number:"))
# if num %2 != 0:
#     print(f"{num} is a prime number")
# else:
#     print(f"{num} is not a prime number")
    







#question 9 (pattern1 - X pattern)

# for i in range(5):
#     for j in range(5):
#         if j==i or j == 4-i:
#             print("*",end="")
#         else:
#             print(" ",end="")
#     print()        




#question 10 (pattern 2 - outer square pattern)


for i in range(5):
    for j in range(5):
        if i==0 or i==4 or j==0 or j==4:
            print("*",end="")
        else:
            print(" ",end="")
    print()