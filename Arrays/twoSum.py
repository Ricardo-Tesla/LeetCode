def twoSum(nums, target):
    index_map={}
#i: key, number: value

    for i, number in enumerate(nums):
        complement=target-number
    
        if complement in index_map:
            return [index_map[complement],i]
    
        index_map[number]=i  #add the number to the map
    
        

nums = [3,3]
target = 6

print(twoSum(nums, target))