# puzzleList Create
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

# puzzleList Show
def puzzleShow():
    textTemp = ""
    for j in range(jNum):
        for i in range(iNum):
            textTemp += str(puzzleList[i][j]) + "\t"
        textTemp += "\n"
    print(textTemp)

# find blank
for i in range(iNum):
    for j in range(jNum):
        if puzzleList[i][j] == 0:
            blank = (i, j)
print(blank)
dirDict = {
    "left": (-1, 0), "right": (1, 0), "up": (0, -1), "down": (0, 1) # 이동 방향
}
i, j = blank # 빈칸의 좌표
ii, jj = dirDict["left"] # 퍼즐의 이동 방향
iNew, jNew = i+ii, j+jj # 이동 후 좌표
if iNew >= 0 and iNew < iNum and jNew >= 0 and jNew < jNum:
    puzzleList[i][j], puzzleList[iNew][jNew] = \
        puzzleList[iNew][jNew], puzzleList[i][j]
puzzleShow()