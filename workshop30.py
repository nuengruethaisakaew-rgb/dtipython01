while True:
    num = int(input(' ป้อนตัวเลขที่ต้องการทาย : '))
    if num < 59:
        print(' คุณทายผิดตัวเลขที่ป้อนน้อยไป ')
    elif num > 59:
        print(' คุณทายผิดตัวเลขที่ป้อนมากไป ')
    else:
        print(' ยินดีด้วยคุณทายถูก ')
        break