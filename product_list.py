#تعریف کردن لیست برای اضافه شدن محصولات و مجموع قیمت محصولات
product_list = []
sum_price = 0

# وارد کردن اطلاعات محصولات
while True:
    name = input("enter a name: ")
    quantity = int(input("enter a quantity: "))
    price = int(input("enter a price: "))

    sum_price += price

# شرط اضافه شدن محصول به لیست و اضافه شدن ان به دیکشنری
    if price <= 1000_000:
        product_dict = {"name":name, "quantity":quantity, "price":price}
        product_list.append(product_dict)
    else:
        print("max price")
        break
    print("--------------------------")

# نمایش محصولات موجود درلیست
for product in product_list:
    print(f"{product['name']:10} {product['quantity']:2} {product['price']:7}")