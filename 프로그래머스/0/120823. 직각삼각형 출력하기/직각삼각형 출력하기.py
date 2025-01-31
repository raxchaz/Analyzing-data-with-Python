def draw_triangle(n):
    for i in range(1, n + 1):
        print("*" * i)

try:
    n = int(input(""))
    draw_triangle(n)
except ValueError:
    print("올바른 정수를 입력해주세요.")