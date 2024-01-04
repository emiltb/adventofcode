import numpy as np

def line_segment_intersection(l1, l2):
    (x1, y1), (x2, y2) = l1
    (x3, y3), (x4, y4) = l2

    A = np.array([[x2-x1, x4-x3], [y2-y1, y4-y3]])
    b = np.array([x3-x1,y3-y1])

    s, t = np.linalg.solve(A, b)

    if 0 <= s and t <= 1:
        return x1 + s*(x2-x1), y1 + t*(y2-y1)

if __name__ == "__main__":
    l1 = [(1,2),(0,-2)]
    l2 = [(-1,1),(2,-2)]

    print(line_segment_intersection(l1,l2))
