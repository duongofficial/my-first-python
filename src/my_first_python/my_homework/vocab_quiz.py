from random import choice

vacabs = {
    "香蕉": "banana",
    "蘋果": "apple",
    "橘子": "orange",
    "西瓜": "watermelon",
    "葡萄": "grape",
    "草莓": "strawberry",
    "鳳梨": "pineapple",
    "芒果": "mango",
    "檸檬": "lemon",
    "水蜜桃": "peach"}
score = 0
key_vacabs = list(vacabs.keys())
print('-'*8)

for i in range(len(key_vacabs)):
    word_choice = choice(key_vacabs)
    key_vacabs.remove(word_choice)
    user_answer = input(f'請問「{word_choice}」的英文是什麼?:')
    if user_answer == vacabs[word_choice]:
        print('答對了!+10分\n')
        score += 10
    else :
        print(f'答錯了,正確答案是:{vacabs[word_choice]}\n你被扣！-10分\n')
        score -= 10
print('測驗結束!你的總分是:', score, '分')