def string_difference(str1, str2):
    m = len(str1)
    n = len(str2)

    # 初始化动态规划表格
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    # 计算编辑距离
    for i in range(m + 1):
        dp[i][0] = i
    for j in range(n + 1):
        dp[0][j] = j

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if str1[i - 1] == str2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = 1 + min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1])

    # 计算字准确率
    correct_chars = m + n - dp[m][n]

    # 计算插入数、删除数和替换数
    insertions = dp[m][n] - dp[m][n - 1]

    accuracy = (correct_chars - insertions) / m

    deletions = dp[m][n] - dp[m - 1][n]
    replacements = dp[m][n] - dp[m - 1][n - 1]

    return accuracy, dp[m][n], insertions, deletions, replacements


# 示例用法
str1 = "kitten"
str2 = "sitting"
accuracy, edit_distance, insertions, deletions, replacements = string_difference(str1, str2)
print("字准确率:", accuracy)
print("编辑距离:", edit_distance)
print("插入数:", insertions)
print("删除数:", deletions)
print("替换数:", replacements)
