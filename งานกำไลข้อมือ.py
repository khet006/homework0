
print("=== โปรแกรมเลือกขนาดกำไล ===")

wrist = float(input("กรอกเส้นรอบวงข้อมือ (ซม.): "))

if wrist <= 16:
    print("ขนาดที่เหมาะสม: XS")
elif wrist <= 17:
    print("ขนาดที่เหมาะสม: S")
elif wrist <= 18:
    print("ขนาดที่เหมาะสม: M")
elif wrist <= 18.5:
    print("ขนาดที่เหมาะสม: L")
else:
    print("ขนาดที่เหมาะสม: L")
