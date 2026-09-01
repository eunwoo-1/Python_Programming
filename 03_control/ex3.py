# for문

# for x in iterable객체:
#   ...

for i in range(5):      # 0 ~ 4
    print(i, end = " ")

a = range(5)
print(a.start, a.stop, a.step)

# 1 ~ 5
for i in range(1, 6):
    print(i, end = " ")
print()

# 1 ~ 10, 2칸씩
for i in range(1, 10, 2):
    print(i, end = " ")
print()

# 5, 4, 3, 2, 1 거꾸로
for i in range(5, 0, -1):
    print(i, end = " ")
print()

# 1 ~ 10까지 합
tot = 0