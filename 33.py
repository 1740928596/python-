def max_sliding_window(n, k, nums):
    from collections import deque
    
    if not nums or k == 0:
        return []

    # Deque to store the indices of the elements
    deq = deque()
    result = []

    for i in range(n):
        # Remove elements out of the current window
        if deq and deq[0] == i - k:
            deq.popleft()

        # Remove elements smaller than the current element from the deque
        while deq and nums[deq[-1]] < nums[i]:
            deq.pop()

        deq.append(i)

        # The first element in deque is the largest element for the current window
        if i >= k - 1:
            result.append(nums[deq[0]])
    
    return result

# Example usage:
n,k = map(int,input().split())
nums = list(map(int,input().split()))

output = max_sliding_window(n, k, nums)
print(' '.join(map(str, output)))
