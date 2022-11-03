import time
'''
Approach 1: Cascading
'''
def subsets(nums):
    result = [[]]
    for num in nums:
        # add = []
        # for r in result:
        #     add.append(r + [num])
        # print(add)
        # result += add
        result += [r + [num] for r in result]
    return result

def subsets3(nums):
    n = len(nums)
    output = []
    
    for i in range(2**n, 2**(n + 1)):
        # generate bitmask, from 0..00 to 1..11
        bitmask = bin(i)[3:]
        print(bitmask)
        
        # append subset corresponding to that bitmask
        output.append([nums[j] for j in range(n) if bitmask[j] == '1'])
    
    return output


nums = [1, 2, 3]
subsets3(nums)


def runTests():
    nums = [i for i in range(18)]
    #iterative
    start = time.time()
    subsets(nums)
    end = time.time()
    print(end - start)
    
    
    #Bitmask
    start = time.time()
    subsets3(nums)
    end = time.time()
    print(end - start)

# runTests()