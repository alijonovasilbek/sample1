# matrix = [[1,2,3],[4,5,6],[7,8,9]]
# a=list(zip(*matrix))
# b=[list(row) for row in a]
# print(a)
#
nums=[1,3,44,4,5]
target=8


def twosum(nums ,target):
    numtoindex={}
    print(numtoindex)
    for i in range(len(nums)):
        if target-nums[i] in numtoindex:
            return [numtoindex[target-nums[i]],i]
            print([numtoindex[target-nums[i]],i])

        numtoindex[nums[i]]=i
        print(numtoindex[nums[i]])
    return []

print(twosum(nums,target))