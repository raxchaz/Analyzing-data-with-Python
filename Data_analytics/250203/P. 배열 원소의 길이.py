# 문자열 배열 strlist가 매개변수로 주어집니다. 
# strlist 각 원소의 길이를 담은 배열을 return 하도록 solution 함수를 완성하세요.

# 1 <= strlist 원소의 길이 <= 100
# strlist는 알파벳 소문자, 대문자, 특수문자로 구성되어 있습니다.

def solution(strlist):
    answer=[]
    for i in strlist:
        answer.append(len(i))
    return answer

# def == 함수를 만들겠다!
# solution == 그냥 객체 이름
# (strlist) == 이 함수가 strlist라는 것을 받아서 사용할 거라는 의미
# 여기서 strlist == 문자열들의 리스트

# answer[] == answer라는 이름의 빈 상자 만들기
# for == 리스트 안에 있는 것들을 하나씩 꺼내어서 반복할 거라는 의미
# i == 리스트 안에서 꺼낸 단어를 담는 작은 바구니
# strlist 안에 단어가 몇 개이든, 하나씩 꺼내어서 i에 담을 예정

# len(i) == i가 몇 글자인지 세는 함수
# answer.append()는 글자 수를 answer라는 상자에 넣는 것
# append == 덧붙이다.


# List Comprehension 
def solution(strlist):
    return [len(i) for i in strlist]
# == strlist에 있는 단어를 하나씩 꺼내어서, 그 글자 수를 리스트로 만들자!


# 파이썬에게 클론(:)이란,
# 여기서부터 새로운 블록이 시작된다고 알려주는 중요한 역할!

if 3 > 2:
    print("3이 2보다 크다.")

# == if 뒤에 : → "조건이 맞으면 이 아래 코드를 실행합니다."

for i in [1, 2, 3]:
    print(i)
# == for 뒤에 : → "이 아래 코드를 반복해!"


def say_hello():
    print("안녕!")

# == def 뒤에 : → "이게 함수의 본문이야!"

# 추가 지식
# 한 줄로 끝나는 list Comprehension일 경우, :를 사용하지 않아!
# 이미 구조가 간단하기 때문에 for가 바로 리스트 안에서 동작하기 때문!

[len(i) for i in strlist]