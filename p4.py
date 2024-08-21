def main():
    n = int(input("Enter the given n numbers:\n"))
    print("SUM WITH TIME COMPLEXITY  1) O(1)")
    print("SUM WITH TIME COMPLEXITY  2) O(n)")
    print("SUM WITH TIME COMPLEXITY  3) O(n^2)")
    ch = int(input())
    sum = 0
    count = 0
    if ch == 1:
        sum = n * (n + 1) // 2
        count += 1
    elif ch == 2:
        for i in range(1, n + 1):
            sum += i
            count += 1
    elif ch == 3:
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                if j >= i:
                    sum += 1
                count += 1
    print("Sumation =", sum)
    print("Time Complexity:", count)

if __name__ == "__main__":
    main()
#Enter the given n numbers:
#50
#SUM WITH TIME COMPLEXITY  1) O(1)
#SUM WITH TIME COMPLEXITY  2) O(n)
#SUM WITH TIME COMPLEXITY  3) O(n^2)
#1
#Sumation = 1275
#Time Complexity: 1

#Enter the given n numbers:
#50
#SUM WITH TIME COMPLEXITY  1) O(1)
#SUM WITH TIME COMPLEXITY  2) O(n)
#SUM WITH TIME COMPLEXITY  3) O(n^2)
#2
#Sumation = 1275
#Time Complexity: 50


