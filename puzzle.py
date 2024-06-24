iNum, jNum = 4, 4
puzzleList = []
# [[1, 5, 9, 13], [2, 6, 10, 14],...]
for i in range(iNum):
    tempList = []
    for j in range(jNum):
        # i = 0, j = 0, result = 1
        # i = 0, j = 1, result = 5
        # i = 1, j = 1, result = 6
        tempList.append(j*jNum+i+1)
    puzzleList.append(tempList)
puzzleList[-1][-1] = 0

textTemp = ""
for j in range(jNum):
    for i in range(iNum):
        textTemp += str(puzzleList[i][j]) + "\t"
    textTemp += "\n"
print(textTemp)