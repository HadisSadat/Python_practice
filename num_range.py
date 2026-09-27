# وارد کردن عدد مورد نظر
num = int(input("Enter a number: "))

# شمارش از عدد مورد نظر تا قرینه عدد
if num > 0:
    for i in range(-num, num+1, 1):
        print(i)
elif num < 0:
    for i in range(-num, num-1, -1):
        print(i)
else:
    print("invalid")