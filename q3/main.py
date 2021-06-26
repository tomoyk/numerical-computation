import numpy as np

"""
https://cattech-lab.com/science-tools/simulation-lecture-4-8/
http://nkl.cc.u-tokyo.ac.jp/seminars/ppOpen-HPC-intro/02b-precond.pdf
https://sungwookyoo.github.io/study/conjugate_gradient/
"""


def solver(_A, _b):
    b_norm = np.linalg.norm(_b)  # bの行列式
    x = np.array([1] * _b.size)  # 初期化
    r = _b - np.dot(_A, x)  # 残差ベクトル
    p = r.copy()
    diffs = []  # 集計用

    while True:
        # step1
        fraction_top = np.dot(p, r)
        Ap = np.dot(_A, p)
        fraction_bottom = np.dot(p, Ap)
        alpha = fraction_top / fraction_bottom

        # step2
        x = x + alpha * p

        # step3
        r = r - alpha * Ap  # 残差ベクトルを更新

        # step4
        diffs.append(np.linalg.norm(r) / b_norm)
        if np.linalg.norm(r) < (1e-20 * b_norm):
            return x, diffs

        # step5
        beta = np.dot(r, r) / fraction_top

        # step6
        p = r + beta * p


def main():
    # expect :: (4 5/2 6)
    # A = np.array([[1, 0, 0], [0, 2, 0], [0, 0, 1]])
    # b = np.array([4, 5, 6])

    # expect :: (1/11=0.0909 7/11=0.6364)
    # A = np.array([[4, 1], [1, 3]])
    # b = np.array([1, 2])

    # 検算
    # c = np.linalg.inv(A).dot(b)
    # print("c=", c)

    # 係数行列A
    import os
    d = int(os.getenv("Q3_D", 10000))
    n = int(os.getenv("Q3_N", 100))

    h = (np.pi / 2) / d
    _alpha = 1 - 2 / h**2
    _beta = 1 / h**2
    _alpha_arr = np.array([_alpha] * n)
    _beta_arr = np.array([_beta] * (n-1))
    A = np.diag(_alpha_arr) \
        + np.diag(_beta_arr, k=1) \
        + np.diag(_beta_arr, k=-1)

    # 既知ベクトルb
    b = np.array([0] * n)
    b[-1] = _beta

    # 計算
    x_arr, diff_arr = solver(A, b)
    print(x_arr)

    # 書き出し
    with open("result.csv", mode="w") as f:
        for i, val in enumerate(diff_arr):
            f.write(f"{i+1}, {val}\n")


if __name__ == "__main__":
    main()
