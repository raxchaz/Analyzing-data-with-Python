# 문제
# (세 자리 수 ) X (세 자리 수)는 다음과 같은 과정을 통하여 이루어진다.
# (1)과 (2) 위치에 들어갈 세 자리 자연수가 주어질 때, (3), (4), (5), (6) 위치에 들어갈 값을 구하는 프로그램 작성

# 입력 규칙
# 첫째 줄에 (1)의 위치에 들어갈 세 자리 자연수가 둘째 줄에 (2)의 위치에 들어갈 세 자리 자연수가 주어진다.

# 출력 규칙
# 첫째 줄부터 넷째 줄까지 차례대로 (3), (4), (5), (6)에 들어갈 값을 출력한다.

# 들어가기 전에, 파이썬의 나눗셈에 대해서 알아보자
# 1. / == 단순 나눗셈 (몫과 나머지 다 나옴)
# 2. // == 나눗셈의 몫만 구해짐
# 3. % == 나눗셈의 나머지만 구해짐
# 4. divmod() == 몫과 나머지 둘 다 구해짐

# 추가로, = 는 같다이고, == 는 비교할 때 사용하는 것임을 잊지 말자!

num1 = int(input())
num2 = int(input())

print(num1 * (num2 % 10))
print(num1 * ((num2 % 100) // 10))
print(num1 * (num2 // 100)) 
print(num1 * num2)

# 다른 풀이
# range 함수를 이용해서 마지막부터 시작까지 역순으로 출력 가능

num1 = int(input())
num2 = input() 
# num2를 문자열로 지정한 이유는 자리수를 쉽게 추출하기 위함이다. 
# 문자열은 각 자리수가 인덱스로 쉽게 접근이 가능하다. 

for i in range(len(num2), 0, -1):
    print(num1 * int(num2[i-1]))

# len(num2) == 문자열 num2의 길이를 구하는 것
# 예를 들어서, num2=`385`일 경우, len(num2)는 3이 될 것

# range() 함수는 숫자 시퀀스를 생성하는 데 사용하는 함수이며, 반복문을 사용할 때 자주 쓰인다.
# 따라서 range() 함수는 특정 범위의 숫자들을 만들어주는 역할을 한다.

# range() 함수는 기본적으로 3개의 인수를 받을 수 있는데,
# range(start, stop, step) == range(시작 숫자, 끝 숫자, 증가(혹은 감소) 값)

# range(stop) == stop만 주면, 숫자는 0부터 stop -1까지 생성됩니다. 
# fot i in range(5) : print(i)
# == 0부터 4까지의 숫자들을 생성합니다.

# range(start, stop) == start, stop 두 가지의 값을 주면 start부터 stop -1까지 숫자 생성
# for i in range(3, 8) : print(i)
# == 3, 4, 5, 6, 7

# range(Start, stop, step) == start부터 stop-1까지 숫자를 생성하는데, step만큼 건너뜀
# step을 양수로 설정하면 증가하고, 음수로 설정하면 감소한다.
# for i in range(2, 10, 2) : print(i) 
# == 2, 4, 6, 8

# for i in range(10, 2, -2) : print(i)
# == 10, 8, 6, 4, 2

# range()와 for()문
# range()는 반복문과 함께 사용되며, 반복문이 실행되는 횟수를 정하는 데 유용
# for i  in range(2) :
#   print(f"반복 횟수 : {i}")
# 반복 횟수 : 0
# 반복 횟수 : 1

# print에서의 f == f-string // 문자열 포맷팅을 쉽게 해주는 파이썬의 기능
# name = "홍길동"
# age = 30
# print(f"이름은 {name}이고, 나이는 {age}입니다.")

# 파이썬에서 {중괄호}는 딕셔너리와 집합(set)를 만들 때 사용되며, 포맷팅 시에도 사용함!
# 1. 딕셔너리 생성
# my_dict = {"name" : "Alice", "age" : 25}
# print(type(my_dict)) # <class 'dict'>

# 2. 집합 생성
# my_set = {1, 2, 3, 3}
# print(my_set)  # {1, 2, 3}

# 3. f-string 포맷팅
# name = "Alice"
# print(f"Hello, {name}")  # Hello, Alice

# print(num1 * int(num2[i-1]))
# num2의 각 자리수와 곱하기 

# num2가 385라는 숫자일 때
# num2[i-1]는 num2에서 뒤에서부터 한 자릿씩 추출하는 방법
# 예를 들어, i = 3일 때, num2[3-1] = num2[2] -> '5'

print(num1 * int(num2))