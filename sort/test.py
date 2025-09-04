testList = [1, 3545, -1, 55662, -34253, 67]

z = len(testList) - 1
i = 0
for i in range(z):
    if testList[i] < testList[i + 1]:
        y = testList[i]
    else:
        y = testList[i+1]
print(y)