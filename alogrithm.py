

x = [1,2,3,4,1,2]
y = [6,5,4,3,2,1]

indexs = []
indexs.append(0)

for i in range(0, len(x)):
    pre = indexs[-1]
    if x[pre] < x[i] and y[pre] > y[i]:
        indexs.append(i)

print('\nx:\n')
for i in indexs:
    print str(x[i]), ''

print('\ny:\n')
for i in indexs:
    print str(y[i]), ''