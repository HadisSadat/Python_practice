# متغیر های محاسبه مجموع اعداد و شمارش تعداد اعداد
sum_ = 0
count = 0

# شمارش اعداد دارای شرط حلقه
for i in range(100, 999, 2):
    if i % 7 == 0:
        sum_ += i
        count += 1

# محاسبه میانگین
average = sum_ / count
print("the average is : ", average)