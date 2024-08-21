#best case
a = []
count = 0
count1 = 0
for i in range(10000,11500):
     a.append(i)
print("Array After Sorting for Best Case of insertion sort :")
for j in range(1,len(a)):
     count += 1
     key = a[j]
     p = j - 1
     while p >= 0 and key < a[p]:
         a[p+1] = a[p]
         p = p - 1
         count1 += 1
     a[p+1]=key
print(f"The No. of j for loop execute: {count}")
print(f"The No. of i for loop execute: {count1}")

#Array After Sorting for Best Case of insertion sort :
#The No. of j for loop execute: 1499
#The No. of i for loop execute: 0

#worst
a = []
count = 0
count1 = 0
for i in range(10000,11500):
    a.append(i)
print("Array After Sorting for Worst Case of insertion sort :")
for j in range(1,len(a)):
    count += 1
    key = a[j]
    p = j - 1
    while p >= 0 and key > a[p]:
        a[p+1] = a[p]
        p = p - 1
        count1 += 1
    a[p+1]=key
print(f"The No. of j for loop execute: {count}")
print(f"The No. of i for loop execute: {count1}")

#Array After Sorting for Worst Case of insertion sort :
#The No. of j for loop execute: 1499
#The No. of i for loop execute: 1124250

#Average Case
import random
a = []
count2 = 0
for i in range(10000,15000):
     r = random.randint(10000,15000)
     a.append(r)
     count2 += 1
    
count = 0
count1 = 0
for j in range(1,len(a)):
     key = a[j]
     p = j - 1
     count = count + 1
     while p >= 0 and key < a[p]:
        
         a[p+1] = a[p]
         p = p - 1
         count1 += 1
     a[p+1] = key

print(a)
print(f"for j loop : {count}")
print(f"Inner while loop : {count1}")
print(f"range for loop : {count2}")

#for j loop : 4999
#Inner while loop : 6288266
#range for loop : 5000

