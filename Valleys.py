n = int(input())
hike = [1 if i=='U' else -1 for i in input()]
valley_c, level = 0, 0
for i in hike:
    level += i
    if i>0 and level==0:
        valley_c += 1
print(valley_c)