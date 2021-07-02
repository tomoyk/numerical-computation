import numpy as np


def solver(x):
    print(x.dtype)
    while 1+x > 1:
        x = x / 2
    return x * 2


def main():
    xs = [
        np.array(1, dtype=np.float16),
        np.array(1, dtype=np.float32),
        np.array(1, dtype=np.float64),
        np.array(1, dtype=np.float128),
    ]
    ys = []
    elapsed_times = []
    import time
    for x in xs:
        _tmp_elp = set()
        for _ in range(10):
            begin = time.time()
            _y = solver(x)
            _tmp_elp.add(time.time() - begin)
        ys.append(_y)
        elapsed_times.append(sum(_tmp_elp) / len(_tmp_elp))

    labels = [x.dtype for x in xs]
    # print(labels)
    # print(ys)
    # print(elapsed_times)
    for l,y,t in zip(labels, ys, elapsed_times):
        print(l, ",", y, ",", t)

if __name__ == "__main__":
    main()
