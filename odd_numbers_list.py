# تعریف لیست برای اضافه کردن اعداد
odd_numbers_list = []

# شرط اضافه شدن اعداد به لیست
for num in range(2, 100, 2) :
    if num % 7 == 0 :
        odd_numbers_list.append(num)

# نمایش لیست
print("odd_numbers_list : " , odd_numbers_list)