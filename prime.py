# Any positive number greater than 1 is only divisible by two numbers i.e. 1 and the number itself is called a prime number.

def prime(num1,num2):
  for num in range(num1, num2 +1):
    if (num >1):
      for i in range(2,num):
        if (num % i) == 0:
          # print(num)
          break
      else:
        print(num)

if __name__ == '__main__':
  # prime(900,1000)
  prime(1,10)
  