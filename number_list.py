# تعرف لیست برای اضافه کردن اعداد زوج و فرد
even_numbers_list = []
odd_numbers_list = []

# واردن کردن عدد تا زمان وارد کردن صفر
while True:
    num = int(input("Enter a number: "))
    if num == 0:
        break
    elif num % 2 == 0:
        even_numbers_list.append(num)
    else :
        odd_numbers_list.append(num)

# نمایش لیست اعداد زوج و فرد
print("even_list : " , even_numbers_list)
print("odd_list : " , odd_numbers_list)