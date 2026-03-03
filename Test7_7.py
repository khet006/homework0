# 7. นําผังงานด้านล่างนี้ไปเขียนโปรแกรม
result = 1; 
n = int(input("กรุณาระบุค่า N : ")); 
if n == 0 :
    result = 0 
    print(result)

while True:
    result *= n
    if n == 1 :
        print(f"ผลลัพธ์คือ : {result}")
        break
    else:
        n = n - 1