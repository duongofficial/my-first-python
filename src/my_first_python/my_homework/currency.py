rate_us = 32.1
rate_jpn = 0.21


tw_dollars = input(f'{'-'*8}\n請輸入欲換匯的新台幣金額: ')

while not tw_dollars.isdigit() or float(tw_dollars) < 0:
    tw_dollars = input(f'輸入錯誤!\n\n{'-'*8}\n請重新輸入: ')

tw_dollars = float(tw_dollars)

print(f'{tw_dollars} 元台幣大約可以換到:')
print('美金:', round(tw_dollars/rate_us, 2), 'usd')
print('日幣:', round(tw_dollars/rate_jpn, 2), 'jpy')