# 01. 문자열 입력 
temp=input()

#02. 숫자 입력
temp=int(input())

#03. 소수점 입력
temp=float(input())

#04. 두 가지 숫자 입력
# split()은 괄호 안의 문자를 기준으로 나눈다는 의미를 가짐 
# () == 공백으로 나눈다는 의미
a,b=map(int, input().split())

#05. 두 가지 문자 입력
a,b=map(str, input().split())

#06. 리스트 입력 (한 줄로 입력된 수를 리스트로 넣을 때 사용)
a = list(map(int, input().split))

#07. 2차원 리스트 입력 (아래는 10행 크기인 경우)
a = [list(map(int, input().split())) for _ in range(10)]