target = 100
squareSumTotal = 0
sumSquareTotal = 0

for i in range(1,target+1):
    squareSumTotal += i
    temp = i * i
    sumSquareTotal += temp


squareSumTotal = squareSumTotal * squareSumTotal
print(abs(squareSumTotal - sumSquareTotal))