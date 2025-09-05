# คำสั่ง break, continue *** ที่อยู่ใน Loop
# break หากถูกทำงาน จะถือว่าจบ Loop ทันที
# continue หากถูกทำงาน จะถือว่าจบรอบนั้นทันที แล้วให้ไปรอบต่อไปเลย
for i in range(5) :
    if i == 3 :
        break
    print(i, 'Hi....')
    
print('-----------------------')

for i in range(5) :
    if i == 3 :
        continue
    print(i, 'Hey....')