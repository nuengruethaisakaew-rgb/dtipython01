# คำสั่งแสดงผลข้อมูลใดๆ หลายประเภท print() เดียว เขียนได้ 4 วิธี
# วิธีที่ 1 ใช้ , (ตรงที่ , เวลาแสดงผลจะเว้น 1 space)
print('DTI',999,'Bangna',10+20,True,'Hi',158.45558) 

#วิธีที่2 ใช้ + (ข้อมูลไหนที่ไม่ใช้ string ต้องทำให้เป็น string ก่อนด้วยฟังก์ชัน str())     
print('DTI' + str(999) + 'Bangna' + str(10+20) + str(True) + 'Hi + str(158.45)')    
print('DTI' + str(999) + ' Bangna ' + str(10+20) + ' ') + str(True) + 'Hi' +str(158.45)

#วิธีที่3 ใช้เมธอด format() ข้อมูลที่จะแสดงผลต้องเป็น string 
print('DTI {} Bangna {} {} Hi {}'.format(999,10+20,True,158.45))
print('{}{}',format('aa','bb','cc','dd'))

#วิธีที่4
print(f'DTI {999} Bangna {10+20} {True} Hi {158.45}')