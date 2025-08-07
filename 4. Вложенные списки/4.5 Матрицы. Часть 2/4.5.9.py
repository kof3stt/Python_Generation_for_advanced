# Магический квадрат ✨🌶️
n = int(input())
data = [[int(x) for x in input().split()] for _ in range(n)]
min_i = min_j = max_i = max_j = data[0][0]
total_main_diagonal = total_secondary_diagonal = 0
total_rows, total_cols = [0] * n, [0] * n
digits = [0] * n**2
for i in range(n):
    for j in range(n):
        if 1 <= data[i][j] <= n**2:
            digits[data[i][j] - 1] += 1
        if i == j:
            total_main_diagonal += data[i][j]
            total_secondary_diagonal += data[n - j - 1][j]
        total_rows[i] += data[i][j]
        total_cols[j] += data[i][j]
if (
    min(digits) > 0
    and total_main_diagonal == total_secondary_diagonal
    and min(total_rows) == max(total_rows) == min(total_cols) == max(total_cols)
):
    print("YES")
else:
    print("NO")
