# استقبال البيانات
products_value = float(input("Products value: "))
city = input("City: ").strip()
weight = float(input("Weight (kg): "))
coupon = input("Coupon (leave empty if none): ").strip().lower()

# حساب الشحن الأساسي
city_lower = city.lower()
if "riyadh" in city_lower:
    shipping = 15.0
elif "jeddah" in city_lower or "dammam" in city_lower:
    shipping = 20.0
else:
    shipping = 30.0

# إضافة تكلفة الوزن إذا زاد عن 5 كجم
if weight > 5:
    shipping += (weight - 5) * 2

# كود الخصم
discount = 0.0
if coupon == "tf10":
    if products_value >= 300:
        discount = products_value * 0.10
    else:
        print("Coupon tf10 requires products value of 300 SAR or more.")
elif coupon == "freeship":
    shipping = 0.0
elif coupon != "":
    print("Invalid coupon")

# الحساب النهائي والضريبة
products_after_discount = products_value - discount
vat = (products_after_discount + shipping) * 0.15
total = products_after_discount + shipping + vat

#  الملخص بالتفصيل
print(f"Products value: {products_value:.2f} SAR")
print(f"City: {city}")
print(f"Weight (kg): {weight}")
print(f"Coupon: {coupon if coupon else 'none'}")
print(f"Products after discount: {products_after_discount:.2f} SAR")
print(f"Shipping: {shipping:.2f} SAR")
print(f"VAT: {vat:.2f} SAR")
print(f"Total: {total:.2f} SAR")
