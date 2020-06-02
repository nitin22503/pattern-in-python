def pattern1(n):
    for i in range(1,(n+1)):
        for j in range(1,(i+1)):
            print("@ ",end="")
        print("\r")
#pattern1(10)

def pattern2(n):
    k=2*n-2
    for i in range(0,n):
        for j in range(0,k):
            print(end=" ")
        k=k-1
        for j in range(0,i+1):
            print("@ ",end="")
        print("\r")
#pattern2(10)

def pattern3(n):
    k=2*n-2
    for i in range(n,-1,-1):
        for j in range(k,0,-1):
            print(end=" ")
        k=k+1
        for j in range(0,i):
            print("@ ",end="")
        print("\r")
#pattern3(10)

def pattern4(n):
    for i in range(0,n):
        for j  in range(0,i+1):
            print("@ ",end="")
        print("\r")
    for i in range(n,-1,-1):
        for j in range(0,i+1):
            print("@ ",end="")
        print("\r")
#pattern4(10)
#    @
#  @ @
#    @
def pattern5(n):
    k=2*n-2

    for i in range(0,n-1):
        for j in range(0,k):
            print(end=" ")
        k=k-2
        for j in range(0,i+1):
            print("@",end=" ")
        print("\r")
    k=-1
    for i in range(n-1,-1,-1):
        for j in range(k,-1,-1):
            print(end=" ")
        k=k+2
        for j in range(0,i+1):

            print("@ ",end="")
        print("\r")

#pattern5(10)

#hour-glass pattern
def pattern6(n):
    k = n - 2
    for i in range(n-1, -1, -1):
        for j in range( k, 0, -1 ):
            print(end=" ")
        k = k + 1
        for j in range(0, i+1):
            print("@", end=" ")
        print("\r")
    k = 2*n - 2
    for i in range(0, n-1):
        for j in range(0, k-1):
            print(end=" ")
        k = k - 1
        for j in range(0, i+1):
            print("@ ", end="")
        print("\r")
pattern6(10)

#left half pyrmid pattern
def pattern7(n):
    k=2*n-2
    for i in range(0,n):
        for j in range(0,k):
            print(end=" ")
        k=k-2
        for j in range(0,i+1):
            print("@ ",end="")
        print("\r")
#pattern7(10)

def pattern8(n):
    for i in range(n,-1,-1):
        for j in range(0,i+1):
            print("@ ",end="")
        print("\r")
#pattern8(5)
print("\n")

def pattern9(n):
    k=2*n-2
    for i in range(0,n):
        for j in range(0,k):
            print(end=" ")

        k=k-1
        for j in range(0,i+1):
            print("@ ",end="")
        print("\r")
    k=n-3
    for i in range(n,-1,-1):
        for j in range(k,-1,-1):
            print(end=" ")
        k=k+1
        for j in range(0,i+1):
            print("@ ",end="")
        print("\r")
#pattern9(10)