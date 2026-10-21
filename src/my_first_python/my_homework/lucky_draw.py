groups = input(f'{'-'*8}\n請輸入抽獎名單(以逗號分隔):').split(',')

while len(groups) < 2:
    groups = input(f'輸入錯誤!\n\n{'-'*8}\n請重新輸入:').split(',')

print(f'\n總共有{len(groups)}人參加抽獎!')
print('頭香是:', groups[0])
print('最後一位報名是:', groups[-1])