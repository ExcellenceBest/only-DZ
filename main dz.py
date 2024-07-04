def matrix(num):
    arr = [[0]*5 for i in range(5)]
    def app(num):
        nonlocal arr
        i, j = 0, 0
        arr[i][j] += num
        if arr[i][j] > 100:
            while arr[i][j] > 100:
                arr[i][j] = abs(arr[i][j] - 100)
                print(arr)
    return app

# matrix2 = matrix(66)
# matrix2(34)
# matrix2(68)
# # matrix2(112)
matrix(66)