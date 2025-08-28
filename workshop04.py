# คำสั่งแสดงผลข้อมูลใดๆ หลายประเภท print() เดียว
# วิธีที่ 1 ใช้ , 
print('DTI',999,'Bangna',10+20,True,'Hi',158.45558) 
#วิธีที่2      
print('DTI' + str(999) + 'Bangna' + str(10+20) + str(True) + 'Hi + str(158.45)')    
print('DTI' + str(999) + ' Bangna ' + str(10+20) + ' ') + str(True) + 'Hi' +str(158.45)

#วิธีที่3
print('DTI {} Bangna {} {} Hi {}'.format(999,10+20,True,158.45))
print('{}{}',format('aa','bb','cc','dd'))

#วิธีที่4
print(f'DTI {999} Bangna {10+20} {True} Hi {158.45}')