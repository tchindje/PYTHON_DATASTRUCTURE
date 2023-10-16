from stack import StaskLinkedList
def is_palindrome(A):
    i = 0
    j = len(A)-1

    while i < j and  A[i] == A[j]:
        i += 1
        j -= 1

    if i < j :
        return 0

    return  1


#problem 10 : check palindrome string using stack
def is_palindrome_using_stack(A):
    stack = StaskLinkedList()
    print(A, len(A))
    n = len(A)

    is_palin = True
    is_even = False

    if n%2==0:
        is_even = True

    m = n//2
    j=0
    while j < m :
        stack.push(A[j])
        print(A[j])
        j += 1

    if not is_even:
        print("not even")
        j += 1 #skip one letter from not even chain

    while j < n and is_palin :
        if stack.pop() != A[j]:
            is_palin = False
        j +=1

    if is_palin and stack.is_empty() :
        return  1

    return 0








