customer = input("Customer name: ")
product = input("Product: ")
price = float(input("Unit price: "))
quantity = int(input("Quantity: "))

subtotal = price * quantity
discount = subtotal * 0.10
after_discount = subtotal - discount
vat = after_discount * 0.15
total = after_discount + vat

print("========= INVOICE =========")
print(f"Customer: {customer}")
print(f"Product: {product} x {quantity}")
print(f"Subtotal: {subtotal:.2f} SAR")
print(f"Discount (10%): {discount:.2f} SAR")
print(f"After discount: {after_discount:.2f} SAR")
print(f"VAT (15%): {vat:.2f} SAR")
print(f"Total: {total:.2f} SAR")

# 5) استخدمنا float للسعر لأنه ممكن يكون فيه كسور (مثل 99.50)،
# واستخدمنا int للكمية لأن عدد القطع لازم يكون رقم صحيح.
# لو أدخل المستخدم 2.5 للكمية، int("2.5") يعطي ValueError لأن int ما تقدر تحول نص فيه فاصلة عشرية.