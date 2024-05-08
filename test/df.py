import numpy as np

def hilbert_matrix(size):
    H = np.zeros((size, size))
    for i in range(size):
        for j in range(size):
            H[i, j] = 1 / (i + j + 1)
    return H


# محورگيري کلي
def complete_pivoting_gaussian_elimination(A):
    # size matrix
    n = len(A)

    U = A.copy()

    P = np.eye(n)
    Q = np.eye(n)

    for k in range(n - 1):
        # پيدا کردن بزرگترين عنصر
        i_max, j_max = np.unravel_index(np.abs(U[k:, k:]).argmax(), U[k:, k:].shape)
        i_max += k
        j_max += k
        # جابجایی سطرها و ستون‌ها
        U[[k, i_max]] = U[[i_max, k]]
        U[:, [k, j_max]] = U[:, [j_max, k]]
        P[[k, i_max]] = P[[i_max, k]]
        Q[:, [k, j_max]] = Q[:, [j_max, k]]
        # حذف
        for i in range(k + 1, n):
            factor = U[i, k] / U[k, k]
            U[i, k:] -= factor * U[k, k:]
            P[i, :] -= factor * P[k, :]

    return P, U, Q


# معکوس کردن
def inverse_using_complete_pivoting(A):
    n = len(A)
    P, U, Q = complete_pivoting_gaussian_elimination(A)
    inv_U = np.linalg.inv(U)
    inv_A = np.dot(inv_U, P)
    inv_A = np.dot(Q, inv_A)
    return inv_A


# ایجاد ماتریس هیلبرت ۵ در ۵
H = hilbert_matrix(5)

# معکوس ماتريس به روش محورگير کلي
H_inv = inverse_using_complete_pivoting(H)

# ضرب ماتریس اولیه در معکوسش
result = H @ H_inv

# نمایش نتیجه
print("ماتریس اصلی هیلبرت (H):")
print(H)
print("\nمعکوس ماتریس هیلبرت (H_inv):")
print(H_inv)
print("\nنتيجه ضرب ماتريس هيلبرت در معکوسش:")
print(result)