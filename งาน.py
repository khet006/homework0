employeeName = " นายเขตโสภณ สุทธิสาร "
position = " ประธานบริษัท"

salary = 25000.50      
bonus = 3500           
taxPercent = 7.5      

totalIncome = salary + bonus

taxAmount = totalIncome * (taxPercent / 100)

netIncome = totalIncome - taxAmount

print("===== รายงานเงินเดือนพนักงาน =====")
print(f"ชื่อพนักงาน : {employeeName}")
print(f"ตำแหน่ง : {position}")
print(f"เงินเดือน : {salary:.2f} บาท")
print(f"โบนัส : {bonus} บาท")
print(f"รายได้รวม : {totalIncome:.2f} บาท")
print(f"ภาษี {taxPercent}% : {taxAmount:.2f} บาท")
print(f"เงินสุทธิที่ได้รับ : {netIncome:.2f} บาท")
print("=================================")
