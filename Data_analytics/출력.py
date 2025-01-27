#01. 한 줄 문자열 출력
print("hello python world!")

#02. 특수문자열 포함하여 출력
print("\"Hello world!\"")

#03. 간단한 숫자 넣어 출력
print(a, b)

#04. 소수점 조정 출력
print("%.2f" %temp)

#05. 자릿수에 0 넣어서 출력
print("%2d" %second)
print("%2d:%2d:%2d" %(h, m, s))

#06. 유니코드 문자 출력
print("\u250C\u252C\u2510")

#07. 리스트 출력
temp = [1,2,3,4,5]
for i in temp :
    print(i, end=" ")

#08. 2차원 리스트 출력
temp = [[1,2,3,4,5],[6,7,8,9,0]]
for i in temp :
    for j in i :
        print(j, end=" ")
    print()