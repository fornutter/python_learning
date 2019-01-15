def judge_change(self, judge):
    for i in range(len(self)):
        for j in range(len(self[0])):
            if judge[i][j] != self[i][j]:
                return True
    return False

a = [
    [1, 4, 0, 0],
    [4, 1, 0, 0]
]

b = [
    [1, 4, 0, 0],
    [4, 1, 0, 0]


]
c = judge_change(a, b)

print(c)
