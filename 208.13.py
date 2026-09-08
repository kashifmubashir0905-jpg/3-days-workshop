n = int(input("Enter a number: "))
k = int(input("Enter the bit position k: "))

if n & (1 << k):
    print("The kth bit is SET")