print("---ตู้กดนํ้าอัตโนมัติ---")
print("1 : โกโก้ \n2 : โอวัลติน \n3 : ไมโล \n4 : นํ้าผลไม้ \n5 : นํ้าเปล่า")

choice = input("กรุณาเลือกหมายเลขเครื่องดื่ม(1-5):")

if choice == "1":
    Beverage = "โกโก้"
    price =50
elif choice == "2":
     Beverage = "โอวัลติน"
     price =40
elif choice == "3":
     Beverage = "ไมโล"
     price =30
elif choice == "4":
     Beverage = "นํ้าผลไม้"
     price =20
elif choice == "5":
     Beverage = "นํ้าเปล่า"
     price =10
else:
     print("ไม่มีเมนูที่คุณเลือกกรุณาเลือกใหม่")
print(f"-------------------------")
print(f"คุณซื้อเครื่องดื่ม : {Beverage} \nราคา : {price} บาท")