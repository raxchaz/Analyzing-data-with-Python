# 정수 n이 주어질 때, n 이하의 짝수를 모두 더한 값을 return하도록 solution 함수 작성
# 제한사항 → 0 < n <= 1000

# def solution(n):
#     return sum(i for i in range(2, n+1, 2))

# range(2, n+1, 2) == 2부터 n까지의 모든 짝수를 생성한 뒤, sum()함수를 통해 합산
# range(start, stop, step) : start부터 stop 직전까지 step간격으로 숫자를 생성하는 함수

# stop이 n+1인 이유 == range 함수는 stop 값을 포함하지 않기 때문에 n을 포함하려면 n+1로 설정해야 한다.
# 결과적으로, range(2, 11, 2) → [2, 4, 6, 8, 10]

# sum() == 숫자들의 합을 계산하는 내장 함수 
# (i for i in range(---)) == 이것은 제너레이터 표현식으로, 리스트를 생성하지 않고도 반복하면서 즉시 합산할 수 있어서 >메모리 효율<이 좋다.
# i for i range(2, n+1, 2) → range로 생성된 각 짝수 i를 하나씩 가져오고, 이 i의 값들이 sum()에 전달되어 차례로 더해짐

# def solution(n) 
# == n이라는 정수를 입력받는 함수

# return sum(i for i range(2, n+1, 2))
# == 계산된 짝수들의 합을 반환한다.

# 추가 tip!
# 제너레이터 표현식은 메모리를 적게 사용하므로, [큰 수의 합]을 구할 때 유리하다.


# ------------------------------------------------------------------------------------------------

# def solution(n):
#     answer = 0
#     for i in range(2, n+1, 2):
#         answer += i
#     return answer
    
# print(solution(10))


# ------------------------------------------------------------------------------------------------

# 무한 반복을 구현하고 싶다면?
# def solution():
#     while True:
#         n = int(input("숫자를 입력해 주세요 (0을 입력할 경우, 종료됩니다) :"))
#         if n == 0:
#             break
        
#         answer = 0 
#         for i in range(2, n+1, 2):
#             answer += i
        
#         print(f"{n} 이하 짝수의 합: {answer}")

# solution()

# ------------------------------------------------------------------------------------------------

# 특정 조건을 만족할 때까지 반복하고 싶은 경우

def solution(n):
    answer = 0
    i = 2
    while answer < 100 and i <= n:
        answer += i
        i += 2
    return answer

print(solution(100))

# ------------------------------------------------------------------------------------------------

# solution()
# 이 코드는 solution() 함수를 호출하고, 결과를 반환하지만 <출력>하지는 않는다.
# return값은 존재하지만, 콘솔에서는 보이지 않음!
# 보통 해당 코드는 내부에서 값을 계산하거나 다른 변수에 저장할 때 사용한다.
def solution():
    return "Hello, World!"

solution()



# print(solution())
# 이 코드는 solution() 함수의 반환 값을 받아서 콘솔에 출력한다.
# return 값인 "hello world!"가 실제로 눈에 보이는 출력물로 나타나는 것!
# 사용자가 결과를 볼 수 있게 출력할 때 사용한다.
def solution():
    return "Hello, World!"

# ------------------------------------------------------------------------------------------------

print(solution())

def add(a, b):
    return a + b

# 1️⃣ 반환만 하고 출력은 없음
add(3, 4)          # 아무것도 출력되지 않음

# 2️⃣ 반환값을 출력
print(add(3, 4))   # 7이 출력됨
