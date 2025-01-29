# 1. For loop
# A for loop is one of looping constructs in Python that is used to iterate over a sequence, such as <list, string, or tuple>.

# 1. Basic Syntax :: for variable in iterable
# The loop takes each element from iterable(반복 가능), assigns it to variable, and executes(실행) the code block.

# Example 1. Iterating Over a List
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

# → output
# apple
# banana
# cherry

# This loop extracts(추출) one item at a time from fruits and assigns it to fruits.
# Then, print(fruit) runs(실행) for each item. 

# This works for single-line expressions, but for multiple lines, we need to recongnize line breaks and rotate them.
# Then we can define our code like this 

# -----------------------------------------------------------------------------------

# Q1. 문자열 str이 주어집니다.
# 문자열을 시계방향으로 90도 돌려서 아래 입출력 예와 같이 출력하는 코드를 작성해 보세요.

def rotate_string_90():
# The function does not take any arguments; it simply processes user input and rotates it by 90 degrees.

s = input()
lines = s.split('\n')
# This line takes input from the user.
# input() 은 한 줄만 받는 함수. 
# 만약 여러 줄을 받고 싶다면, s=sys.stdin.read()

max_length = max(len(line) for line in lines)
# This finds the length of the longest line in the lines list.
# This ensures that all line have the same length for proper rotation.

lines = [line.ljust(max_length) for line in lines]
# ljust(max_length) pads shorter lines with spaces so that all lines have the same length
# ljust(width) == 문자열을 지정한 길이(width)에 맞게 좌측 정렬을 하고, 부족한 부분을 공백으로 채우는 함수
# text = "ABC"
# padded_text = text.ljust(5)  == 길이를 5로 맞추기

rotated = [''.join(line[i] for line in reversed(lines)) for i in range(max_length)]

for row in rotated:
    print(row)

rotate_string_90()


# 3 other people's solutions--------------------------------------------------------

print('\n'.join(input()))

# -----------------------------------------------------------------------------------

str = list(input())
for i in range(len(str)):
    print(str[i] )

# -----------------------------------------------------------------------------------

str = input()
for a in str:
    print(a)

# -----------------------------------------------------------------------------------
