pw = input(f'{'-'*8}\n請輸入新密碼:')

while len(pw) < 8 or len(pw) > 16 or "admin" in pw.lower() or " " in pw:
    print('密碼不符合安全規範,請重新設定')
    pw = input(f'\n{'-'*8}\n請輸入新密碼:')

print('\033[92m密碼設定成功\033[0m')