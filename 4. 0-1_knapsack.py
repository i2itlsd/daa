def knapsack(weights, values, capacity):
    n = len(weights)
    # Creating a 2D table to store the maximum value at each capacity and item
    dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]

    # Build the table dp[][] in bottom up manner
    for i in range(n + 1):
        for w in range(capacity + 1):
            if i == 0 or w == 0:
                dp[i][w] = 0
            elif weights[i - 1] <= w:
                dp[i][w] = max(values[i - 1] + dp[i - 1][w - weights[i - 1]], dp[i - 1][w])
            else:
                dp[i][w] = dp[i - 1][w]

    # The last cell of the table contains the result, i.e., the maximum value
    return dp[n][capacity]

# Taking input from the user
n = int(input("Enter the number of items: "))
weights = []
values = []

print("Enter the weights of the items:")
for i in range(n):
    weight = int(input(f"Weight of item {i + 1}: "))
    weights.append(weight)

print("Enter the values of the items:")
for i in range(n):
    value = int(input(f"Value of item {i + 1}: "))
    values.append(value)

capacity = int(input("Enter the capacity of the knapsack: "))

# Calling the knapsack function
max_value = knapsack(weights, values, capacity)

print(f"The maximum value that can be obtained is {max_value}")


'''
Time Complexity: O(n * capacity)
Space Complexity: O(n * capacity)

dynamic programming code for solving the 0-1 Knapsack problem:

->Input:
    The user inputs the number of items, their weights, values, and the knapsack's capacity.

->DP Table Initialization:
    A 2D table dp of size (n+1) x (capacity+1) is created, where each entry dp[i][w] stores the maximum value that can be obtained with the first i items and a knapsack capacity w.

->Filling the DP Table:

    The table is filled using a bottom-up approach:
        >If an item cannot be included because its weight exceeds the current capacity, it inherits the value from the row above.
        >If the item can be included, we take the maximum value between including or excluding the item.

->Result:
    The value at dp[n][capacity] contains the maximum value that can be obtained with the given set of items and the knapsack's capacity.
'''