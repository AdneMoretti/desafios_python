N = int(input())
if N == 0:
    print("E")
elif N > 0 and N <= 35:
    print("D")
elif N > 35 and N <= 60:
    print("C")
elif N > 60 and N <= 85:
    print("B")
elif N > 85 and N <= 100:
    print("A")