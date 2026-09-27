#اضافه شدن اسم دارای شرط به لیست
name_list = []


# تابع شمارش حروف صدا دار هر اسم
def vowel_char(name):
    count_ = 0

    for char in name.lower():
        if char in "aeiou":
            count_ += 1

    return count_


# وارد کردن اسم تا زمان رسیدن به شرط و اضافه شدن به لیست
while True:
    name = input("Enter a name: ")

    if name.lower() == "quit":
        break

    name_list.append(name)

name_list.sort(key=vowel_char, reverse=True)

# نمایش لیست اسامی
for name in name_list:
    print(name)