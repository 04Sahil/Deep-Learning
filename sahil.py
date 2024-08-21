print("Enter the n num")
n = int(input())
print("Select the choice\n")
print("1.O(1)\n")
print("2.O(n)\n")
print("3.O(n^2)\n")
ch = int(input())
sum = 0
count = 0

def case1():
    sum = n*(n+1)/2
    count += 1
    print(f"The sum of number is: {sum}")
    print(f"Time is: {count}")
def case2():
    for i in range(1, n+1):
        sum = sum + i
        count += 1
def case3():
    for i in range(1, n+1):
        for j in range(1, n+1):
            if j>= i:
                sum += 1
            count += 1

def m(ch):
    switch = {
        1: case1,
        2: case2,
        3: case3,
        }
    selected_case = switch.get(ch)
    selected_case()
    
m(1)
