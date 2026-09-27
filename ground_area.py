#وارد کردن طول و عرض
length = int(input("enter the length : "))
width = int(input("enter the with: "))

# محاسبه مساحت زمین
area = length * width

# نمایش مساحت زمین
print(area)

# بررسی شرایط مجوز
if 0 < area <= 100 :
    print("don't need license")
elif 100 < area <= 200 :
    print("must have license")
elif 200 < area :
    print( "not included license")
else :
    print("invalid area")