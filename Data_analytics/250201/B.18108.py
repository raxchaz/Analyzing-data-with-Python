# 1998년생인 내가 태국에서는 2541년생?!
# ICPC Bangkok Regional에 참가하기 위해 수완나품 국제공항에 막 도착한 팀 레드시프트 일행은 눈을 믿을 수 없었다. 공항의 대형 스크린에 올해가 2562년이라고 적혀 있던 것이었다.
# 불교 국가인 태국은 불멸기원(佛滅紀元), 즉 석가모니가 열반한 해를 기준으로 연도를 세는 불기를 사용한다. 반면, 우리나라는 서기 연도를 사용하고 있다. 
# 불기 연도가 주어질 때 이를 서기 연도로 바꿔 주는 프로그램을 작성하시오.

# 입력
# 서기 연도를 알아보고 싶은 불기 연도 Y가 주어진다.
# 1000 <= Y <= 3000

# 출력
# 불기 연도를 서기 연도로 변환한 결과를 출력한다.

# 불기 연도 입력
Y = int(input())

# 불기 연도를 서기 연도로 변환
segi_year = Y - 543

# 결과 출력
print(segi_year)

# def solution 을 사용하지 않은 이유는 문제의 요구사항이 간단하고, 입/출력이 직관적이기 때문!
# "코드의 목적"은 입력받은 불기 연도에서 543년을 빼는 것 뿐이기 때문에 함수로 만들지 않고 간단한 식으로 처리
# 만일 def solution을 사용하고 싶다면? 

def solution(Y):
    return Y - 543

Y = int(input())
print(soltion(Y))