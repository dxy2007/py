proposition = open('test.pydic', 'r', encoding='UTF-8').read()
d = []
exec('proposition=' + proposition)
for i in proposition:
    print(proposition[i])
    if proposition[i] == '水是剧毒的':
        d = 1
    # continue
    elif proposition[i] == '你可以吃东西':
        print('真')
    if d == 1:
        # print('真')
        d = 0
