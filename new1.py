 #accept a number and display whether it is prime or not

num=int(input("Enter The Number: "))
if num < 2:
      print(num, "is not a prime number.")
else:
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            print(num,"Is Not A Prime Number")
            break
    else:
        print(num,"Is A Prime Number")

