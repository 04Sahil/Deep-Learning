nums1 = [1,2]
nums2 = [3,4]
merged_array = nums1+nums2
num= {}
total = 0
n = len(merged_array)
for ele in range(0,len(merged_array)):
    total = total + merged_array[ele]
h =(total/n)
print(h)
