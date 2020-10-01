# Validate whether the given array is a subsequence of a largr array
# Defination of Subsequence:In mathematics, a subsequence is a sequence that can be derived from another sequence by deleting some or no elements without changing the order of the remaining elements.
#The question might appear quiet simple but this concept of subsequence is used in most of compititive coding question and interview
# Here a1 is array to check
# a2 is the larger array
def Solution(a1,a2):
    b=[]
    for i in range(len(a1)):
        b.append(a2.index(a1[i]))
    for i in range(len(b)-1):
        if(b[i+1]>b[i]):
            pass
        else:
            return False
    return True

t=int(input())
for i in range(t):
    n,m=map(int,input().split())
    a1=list(map(int,input().split()))
    a2=list(map(int,input().split()))
    res=Solution(a1,a2)
    print(res)
