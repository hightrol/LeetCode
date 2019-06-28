## SplitArrayLargestSum 410
def splitArray(nums, m):        
    total = sum(nums)
    n = len(nums)
    def needX(threshold):
        count = 1
        cursum = 0
        for i in range(n):
            if cursum + nums[i] <= threshold:
                cursum += nums[i]
            else:
                cursum = nums[i]
                count += 1
        return count
    l, r = max(sum(nums)//m, max(nums)), total
    while r-l >= 1:
        mid = (l+r)//2
        count = needX(mid)
        if count > m:
            l = mid+1
        else:
            r = mid
    return l

splitArray([1,6,5,6],3)
