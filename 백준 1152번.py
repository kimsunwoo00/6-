string = input("")

if string == " ": #문장이 공백인 경우
    print(0)
else:
    words = string.split(" ") # 띄어쓰기로 구분

    while '' in words:
        words.remove('')

print(len(words))
    
