# تعریف لیست خالی برای اضافه شدن دروس و محاسبه مجموع واحد ها
lesson_list = []
sum_unit = 0

# واردن کردن اطلاعات درس
while True:
    title = input("enter a title: ")
    teacher = input("enter a name: ")
    duration = int(input("enter a duration: "))
    unit = int(input("enter a unit: "))

    sum_unit += unit

# شرط اضافه شدن درس به لیست و نمایش درس در دیکشنری
    if sum_unit <= 17:
        information_dict = {"title": title, "teacher": teacher, "duration": duration, "unit": unit}
        lesson_list.append(information_dict)
        print("saved")
    else:
        print("max unit")
        break
    print("--------------------")

# نمایش دروس موجود در لیست
    for lesson in lesson_list:
        print(f"{lesson['title']:10} by {lesson['teacher']:20} ({lesson['unit']})")