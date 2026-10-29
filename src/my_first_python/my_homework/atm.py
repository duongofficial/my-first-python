# ATM
password = "8888"
balance = 5000


user_input = input(f'{'-'*8}\n請輸入密碼:')
while user_input != password:
    user_input = input(f'密碼錯誤!\n\n{'-'*8}\n請重新輸入:')

print('登入成功! 目前餘額:', balance,'元')


withdraw_money = input('請輸入提款金額:')
while True:
    try:
        withdraw_money = float(withdraw_money)
        if withdraw_money > balance:
            withdraw_money = input('\n餘額不足!\n請重新輸入:')
        elif withdraw_money <= 0:
            withdraw_money = input('\n金額無效!\n請重新輸入:')
        else:
            balance -= withdraw_money
            break
    except:
        withdraw_money = input('\n這不是數字!\n請輸入數字:')

print(f'提款成功!\n 💰 {withdraw_money}元')
print('剩餘餘額:', balance, '元')











