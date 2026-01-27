import sys
input = sys.stdin.read

def main():
    data = input().split()#变成字符串列表
    index = 0
    #提取n和m,输入应为nxm的矩阵
    n = int(data[index])
    index += 1
    m = int(data[index])
    index += 1

    #建立nxm的矩阵,填入相应的元素
    #matrix = []    #空列表,没有创建任何行,没办法用matrix[i][j]去赋值
    # 预先初始化n行m列的矩阵（初始值全为0）
    matrix = [[0 for _ in range(m)] for _ in range(n)]
    for i in range(n):
        for j in range(m):
            matrix[i][j] = int(data[index])
            index += 1

    #对矩阵内所有元素求和
    total =0
    for row in matrix:
        for num in row:
            total += num
    
    half_total = total / 2

    #计算列块和值&行块和值,并得到与half_total的最小差值
    total_row ,total_column= 0,0
    abs_min = float('inf')
    #首先计算行块和的情况
    row_sums = [sum(row) for row in matrix]
    for i in range(n-1):
        total_row += row_sums[i]
        abs_min = min(abs_min,abs(total_row - half_total))

    #再计算列块和的情况
    col_sums = [sum(col) for col in zip(*matrix)]
    for j in range(m-1):
        total_column += col_sums[j]
        abs_min = min(abs_min,abs(total_column - half_total))
    
    result = int(2 * abs_min)
    print(result)
    return result

if __name__ == "__main__":
    main()