def knapsack_with_scaling(weights, values, W, epsilon):
    n = len(weights)
    C_max = max(values)
    K = (epsilon * C_max) / n
    
    scaled_values = [int(v / K) for v in values]
    max_scaled_value = sum(scaled_values)

    dp = [[float('inf')] * (max_scaled_value + 1) for _ in range(n + 1)]

    dp[0][scaled_values[0]] = weights[0]
    
    for i in range(1, n):
        for c in range(int(max_scaled_value) + 1):
            if c >= scaled_values[i]:
                dp[i][c] = min(dp[i - 1][c], dp[i - 1][c - scaled_values[i]] + weights[i])
            else :
                dp[i][c] = dp[i - 1][c]

    for c in range(max_scaled_value, -1, -1):
        if dp[n-1][c] <= W:
            return c * K
    
    return [n][W]
