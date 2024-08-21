#bubble sort
import random

arr = [0] * 10000
count = 0
count1 = 0

print("1.BEST CASE")
print("2.WORST CASE")
print("3.AVERAGE CASE")
ch = int(input())
if ch == 1:
    arr = list(range(1, 10001))
elif ch == 2:
    arr = list(range(10000, 0, -1))
elif ch == 3:
    arr = [random.randint(1, 10000) for _ in range(10000)]

for i in range(10000 - 1):
    for j in range(10000 - i - 1):
        if arr[j] > arr[j + 1]:
            count1 += 1
            arr[j], arr[j + 1] = arr[j + 1], arr[j]
        count += 1

print("Sorted Array:")
for i in range(10000):
    print(arr[i], end=" ")

print("\nNo. of times loop run:", count)
print("Swapping done:", count1)
#1.BEST CASE
#2.WORST CASE
#3.AVERAGE CASE
#1
#Sorted Array:
#No. of times loop run: 49995000
#Swapping done: 0




#Selection sort
import random

A = [0] * 10000
count = 0
count1 = 0

print("1.BEST CASE")
print("2.WORST CASE")
print("3.AVERAGE CASE")
ch = int(input())
if ch == 1:
    A = list(range(1, 10001))
elif ch == 2:
    A = list(range(10000, 0, -1))
elif ch == 3:
    A = [random.randint(1, 10000) for _ in range(10000)]

for i in range(10000 - 1):
    min_val = A[i]
    temp = i
    for j in range(i + 1, 10000):
        count += 1
        if min_val > A[j]:
            min_val = A[j]
            temp = j
    if min_val < A[i]:
        A[temp], A[i] = A[i], min_val
        count1 += 1

print("Sorted Array:")
for i in range(10000):
    print(A[i], end=" ")

print("\nNo. of times loop run:", count)
print("Swapping done:", count1)
#1.BEST CASE
#2.WORST CASE
#3.AVERAGE CASE
#2
#Sorted Array:
#No. of times loop run: 49995000
#Swapping done: 5000