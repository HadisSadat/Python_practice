#تعریف لیست برای اضافه کردن اسامی
names_list = []

# گرفتن مقدار از کاربر تا زمان خروج
while True :
    name =input("Enter a name : ")
    if name.lower() == "exit" :
        break
    names_list.append(name)
    names_list.sort()

#نمایش لیست
print("names_list : ", names_list)