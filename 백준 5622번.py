alphabet_list = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
word = input()

time = 0
for unit in alphabet_list:
    for i in unit:
        for x in word: # 입력받은 문자를 하나씩 분리한다
            if i == x: # 두 알파벳이 같으면
                time += alphabet_list.index(unit) +3 # time = time + index +3
print(time)
####**
