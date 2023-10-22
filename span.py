# finding a span :
# input : array A[1…n]
# finding array S[1…n] where S[i] = card ({ j | A[j] <= A[i] })

def find_span(A):
    n = len(A)
    span = [None] * n

    if n == 0:
        print("empty list")
        return

    for i in range(n):
        j = i
        cpt = 0
        while j >= 0 and A[j] <= A[i]:
            cpt += 1
            j = j - 1

        span[i] = cpt

    return span


l = [6, 3, 4, 5, 2]
print("span of {} is {}".format(l, find_span(l)))
