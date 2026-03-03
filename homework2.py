print("---การคำนวณส่วนลดตามยอดการซื้อ---")
total_price = float(input("กรุณากรอกราคาสินค้ารวม: "))

if total_price >=10000:
     discount_rate = 0.20
     print("ยินดีด้วยคุณได้ส่วนลด 20%")
elif total_price >=7000:
     discount_rate = 0.15
     print("ยินดีด้วยคุณได้ส่วนลด 15%")
elif total_price >=5000:
     discount_rate = 0.10
     print("ยินดีด้วยคุณได้ส่วนลด 10%")
elif total_price >=1000:
     discount_rate = 0.05
     print("ยินดีด้วยคุณได้ส่วนลด 5%")
else:
     discount_rate = 0.0
     print("เสียใจด้วยด้วยคุณไม่ได้ส่วนลด")

discount_amount = total_price * discount_rate
net_price = total_price -discount_amount

print(f"--------------------------------")
print(f"ราคาปกติ :    {total_price:,.2f}บาท")
print(f"ส่วนลดที่ได้ :  {discount_amount:,.2f}บาท")
print(f"ราคาสุทธิ :    {net_price:,.2f}บาท")