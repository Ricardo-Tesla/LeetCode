def intersectionArray(nums1, nums2):
    
    nums1.sort()
    nums2.sort()
    
    i,j=0,0
    newArray=[]
    
    while i < len(nums1) and j < len(nums2):
        if nums1[i] < nums2[j]:
            i+=1
        elif nums1[i] > nums2[j]:
            j+=1
        else:
            newArray.append(nums1[i])
            i+=1
            j+=1
    
            
    return newArray

nums1=[4,9,5]          #[1,2,2,1]   and  [2,2]
nums2=[9,4,9,8,4]
print(intersectionArray(nums1,nums2))