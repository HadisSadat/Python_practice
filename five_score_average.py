# محاسبه تعداد نمرات
sum_ = 0

# واردن کردن تعداد نمره بر اساس حلقه
for i in range(1, 6, 1):
    score = int(input("enter a score : "))
    sum_ += score

# محاسبه میانگین نمرات
average = sum_ / 5
print("The average is : ", average)