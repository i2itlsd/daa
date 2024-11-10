class Item:
    def __init__(self, profit, weight):
        self.profit = profit
        self.weight = weight

def fractionalKnapsack(w, arr):
    arr.sort(key=lambda x: x.profit / x.weight, reverse=True)
    finalValue = 0.0
    for item in arr:
        if w >= item.weight:
            finalValue += item.profit
            w -= item.weight
        else:
            finalValue += item.profit * (w / item.weight)
            break
    return finalValue

if __name__ == "__main__":
    n = int(input("Enter number of items:\n"))
    arr = []
    for i in range(n):
        profit = int(input(f"Enter profit of item {i + 1}:\n"))
        weight = int(input(f"Enter weight of item {i + 1}:\n"))
        arr.append(Item(profit, weight))
    
    w = int(input("Enter capacity of knapsack:\n"))
    print("Maximum value in knapsack:", fractionalKnapsack(w, arr))


'''
Time Complexity: O(n.logn)
Space Complexity: O(n)

The code solves the Fractional Knapsack Problem using a greedy algorithm:

->Item class: Represents an item with profit and weight.
->fractionalKnapsack function:
    >Sorts the items based on their profit-to-weight ratio in descending order.
    >Iterates through the sorted items, adding their full profit if the knapsack can carry the whole item.
    >If the item can't be fully carried, it adds a fraction of the item's profit based on the remaining capacity and stops after that.
->Main function:
    >Takes user input for the number of items, their profits, weights, and the knapsack's capacity.
    >Calculates and prints the maximum value the knapsack can carry using the fractionalKnapsack function.
'''