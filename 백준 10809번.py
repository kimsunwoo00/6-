word = input()

alphabet = list(range(97,123)) # 아스키코드 숫자 범위

for i in alphabet:
    print(word.find(chr(i))) # find함수 사용
