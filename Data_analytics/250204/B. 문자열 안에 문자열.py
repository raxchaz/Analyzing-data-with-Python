# 문제
# 문자열 str1, str2가 매개변수로 주어집니다.
# str1 안에 str2가 있다면 1을, str1 안에 str2가 없다면 2를 return 하도록 함수를 완성해 주세요.

def solution(str1, str2):
    return 1 if str2 in str1 else 2


def solution(str1, str2):
    if str1.count(str2):
        return 1
    else:
        return 2
    
# count()함수
# 특정 요소가 얼마나 자주 등장하는지 세어준다.
# count() == 대, 소문자를 구분하며, 중첩된 문자열은 따로 셈!

# 기본 사용 : string.count(substring, start, end)
# substring : 찾고자 하는 문자열
# start : 검색을 시작할 인덱스 (기본 값은 0)
# end : 검색을 끝낼 인덱스 (기본값은 문자열의 끝)

text = "hello world"
print(text.count('l')) # 3

list.count(element)
fruits = [ 'apple', 'banana', 'apple', 'cherry', 'apple']
print(fruits.count('apple')) #3

tuple.count(element)
numbers = (1, 2, 3, 2, 4, 2, 5)
print(numbers.count(2)) #3



