'''
離散化誤差を計算するプログラム
誤差の評価を行う課題
'''

import math

ENABLE_PRINT = True
ENABLE_DEBUG = False


def display_a(A):  # 便利関数
    # 表示
    print("*"*30, "Display [begin]", "*"*30)
    for _a in A:
        for _a2 in _a:
            print(int(_a2), end="\t")
        print()
    print("*"*30, "Display [end]", "*"*30)


def solver(A, b, n):
    ''' 便利関数 '''
    def _display_row():
        for x2 in range(n-1):
            print(int(A[y][x2]), end="\t")
        print()

    ''' 計算処理 '''
    for x in range(n-1):  # xを固定
        if ENABLE_DEBUG:
            print("\n", "="*40, f"start x={x}", "="*40, "\n")

        for y in range(n-1):  # yを選択
            if x == y:
                continue

            if ENABLE_DEBUG:
                print("-"*30, f"selected y={y}", "-"*30)
                _display_row()

            # 係数の計算
            try:
                # A[x][x] = A[0,0], A[1,1]
                coeff = A[y][x]/A[x][x]
                if ENABLE_DEBUG:
                    print("coeff =", coeff)
            except:
                continue

            # データの計算
            for x2 in range(n-1):
                if ENABLE_DEBUG:
                    print(f"[{y},{x2}]-({str(coeff)[:4]})*[{x},{x2}]=",
                          int(A[y][x2]), "-", int(coeff), "*", int(A[x][x2]), "=",
                          int(A[y][x2] - coeff * A[x][x2]))
                A[y][x2] = A[y][x2] - coeff * A[x][x2]
            b[y] = b[y] - coeff * b[x]

            # データの表示
            if ENABLE_DEBUG:
                _display_row()

        # 表示
        if ENABLE_DEBUG:
            display_a(A)

        # break
        # if x == 1:
        #    break

    xs = [b[i] / A[i][i] for i in range(n-1)]
    return xs


"""
# 表示
if ENABLE_PRINT:
    print("*"*30, "Debug [begin]", "*"*30)
    for _a in A:
        for _a2 in _a:
            print(int(_a2), end="\t")
        print()
    print("*"*30, "Debug [end]", "*"*30)

# 表示
if ENABLE_PRINT:
    print("b=", end="")
    for _b in b:
        print(int(_b), end="\t")
    print()
"""


def main():
    import os
    d = int(os.getenv("Q2_D", 10000))
    n = int(os.getenv("Q2_N", 100))

    h = (math.pi / 2 - 0) / d
    alpha = 1 - 2 / h**2
    beta = 1 / h**2
    if ENABLE_PRINT:
        print(f"n={n}, d={d}, h={h}, alpha={alpha}, beta={beta}")

    ''' 係数行列A '''
    A = [[0 for _ in range(n-1)] for _ in range(n-1)]
    # Alphaで初期化
    for i in range(n-1):
        A[i][i] = alpha
    # Betaで初期化
    for i in range(1, n-1):
        A[i][i-1] = beta  # 横軸
        A[i-1][i] = beta  # 縦軸

    ''' 既知ベクトルb '''
    b = [0 for _ in range(n-1)]
    b[-1] = beta

    # 実行時間の計測と実行
    import time
    elapsed_times = set()
    for _ in range(10):
        begin = time.time()
        solver(A, b, n)
        elapsed_times.add(time.time() - begin)
        # print(time.time() - begin)
        # display_a(A2)
    print("time::", n, ",", sum(elapsed_times) / len(elapsed_times))

    # 厳密解 y
    xs = [h*i for i in range(1, d)]
    ys = [math.sin(x) for x in xs]

    # 解析解 y2
    ys2 = solver(A, b, n)
    fraction_top = max(abs(y2 - y) for y2,y in zip(ys2, ys))
    fraction_bottom = max(abs(y) for y in ys)
    print("error::", d, ",", fraction_top / fraction_bottom)


if __name__ == "__main__":
    main()
