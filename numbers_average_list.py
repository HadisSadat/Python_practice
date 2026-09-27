#محاسبه مجموع اعداد وارد شد و شمارش تعداد اعداد
sum_ = 0
count = 0

# وارد کردن عدد تا زمانی که صفر وارد شود و محاسبه و نمایش میانگین
while True :
    num = int(input("Enter a number: "))
    if num == 0 :
        break
    if num % 2 != 0:
        sum_ += num
        count += 1
print("sum_ : " , sum_ , " count : ", count)

if count > 0 :
    average = sum_ / count
    average = round(average, 2)

    print("The average is", average)
else :
    print("The number is not odd")