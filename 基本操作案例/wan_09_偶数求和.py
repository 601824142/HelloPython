i = 0
result = 0

while i <= 100:
    if i % 2 == 0:
        result += i
        print(i)
    i += 1

print("偶数和:%d" % result)
