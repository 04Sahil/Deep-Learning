l1=["ki","mezu","hanna","hebbi","ashi"]
for i, ele in enumerate(l1):
    print(ele)
    print(i)
l2 = [1,4,5,8]
total = 0
for ele in range(0,len(l2)):
    total = total + l2[ele]
    print(ele)
    print(l2[ele])
print(total)
for i,ele in enumerate(l2):
    total = total + ele
    print(ele)
   
print(total)