def max_min_sum(A, B):
    # DP dict to store the difference between sums as keys and the maximum of minimum sum as values
    dp = {0: 0}
    
    for a, b in zip(A, B):
        # Temporary dict to store updates to prevent in-place modification affecting iteration
        temp_dp = {}
        for diff, min_sum in dp.items():
            # Calculate new differences and update temp_dp for choosing from A or B
            new_diff_a = diff + a - b
            new_diff_b = diff - a + b
            # Update choosing from A
            temp_dp[new_diff_a] = max(temp_dp.get(new_diff_a, 0), min_sum + a)
            # Update choosing from B
            temp_dp[new_diff_b] = max(temp_dp.get(new_diff_b, 0), min_sum + b)
        
        # Update dp with the changes from temp_dp
        dp.update(temp_dp)
    
    # Find the minimum difference and its corresponding maximum minimum sum
    min_diff = min(dp.keys(), key=abs)
    return dp[min_diff]

# Example arrays
A = [3, 2, 4, 5]
B = [1, 6, 3, 2]

# Solve the problem
max_min_sum(A, B)
