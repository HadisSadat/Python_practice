from persian_tools import digits

lesson_list = [
    {"name":"phyton","unit":3,"teacher":"ali"},
    {"name":"phyton","unit":3,"teacher":"reza"},
    {"name":"java","unit":5,"teacher":"ahmad"},
    {"name":"c#","unit":2,"teacher":"mohsen"}

]

new_lesson_1 = {"name":"phyton","unit":3,"teacher":"reza"}
new_lesson_2 = {"name":"java","unit":5,"teacher":"ahmad"}
new_lesson_3 = {"name":"c#","unit":2,"teacher":"mohsen"}

student_lesson_list = []

def add_lesson(lesson):
    if lesson in lesson_list:
        student_lesson_list.append(lesson)
        print(student_lesson_list)

add_lesson(new_lesson_1)
add_lesson(new_lesson_2)
add_lesson(new_lesson_3)

print(student_lesson_list)

# درس ها بر اساس واحد مرتب شوند
student_lesson_list = sorted(student_lesson_list, key=lambda x: x["unit"], reverse=True)

#اسم درس ها به ترتیب حروف الفبا
student_lesson_list = sorted(student_lesson_list, key=lambda x: x["name"])

# قیمت هر واحد
def price_lesson(lesson):
    if lesson["unit"] == 2:
        lesson["price"] = 1000
    elif lesson["unit"] == 3:
        lesson["price"] = 1200
    elif lesson["unit"] == 5:
        lesson["price"] = 1400

    return lesson

# مبلغ کل پرداختی
result = list(map(price_lesson, student_lesson_list))
print(result)

prices = list(map(lambda lesson:lesson["price"], result))
print(prices)

print(digits.convert_to_word(3600))