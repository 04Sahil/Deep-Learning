nums = [3,2,2,3]
val = 3
k = 0
for i ,ele in range(0,len(nums)):
    print(i)
    print(ele)
    if nums[i] != val:
        nums[k] = nums[i]
        k += 1
print(nums[:k])
        
        
        




