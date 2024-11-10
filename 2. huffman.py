import heapq

class Node:
    def __init__(self, freq, symbol, left=None, right=None):
        self.freq = freq
        self.symbol = symbol
        self.left = left
        self.right = right
        self.huff = ""
    
    def __lt__(self, other):
        return self.freq < other.freq

def printNodes(node, val=""):
    newval = val + node.huff
    if node.left:
        printNodes(node.left, newval)
    if node.right:
        printNodes(node.right, newval)
    else:
        print(f"{node.symbol} -> {newval}")

def huffmanCoding():
    # Take input for characters and frequencies
    chars = input("Enter characters separated by space: ").split()
    freqs = list(map(int, input("Enter the corresponding frequencies separated by space: ").split()))

    # Create nodes for each character and frequency
    nodes = []
    for i in range(len(chars)):
        heapq.heappush(nodes, Node(freqs[i], chars[i]))
    
    # Build the Huffman tree
    while len(nodes) > 1:
        left = heapq.heappop(nodes)
        right = heapq.heappop(nodes)
        left.huff = "0"
        right.huff = "1"
        newnode = Node(left.freq + right.freq, left.symbol + right.symbol, left, right)
        heapq.heappush(nodes, newnode)
    
    # Print the Huffman codes
    print("Huffman Codes:")
    printNodes(nodes[0])

# Run the Huffman coding function
huffmanCoding()



'''
Time Complexity: O(n.logn)
Space Complexity: O(n)

Huffman coding is a greedy algorithm used for lossless data compression. It works by assigning shorter binary codes to more frequent characters and longer codes to less frequent ones, minimizing the total number of bits required for encoding.

Steps:

->Input: You are given characters and their frequencies.
->Build a Min-Heap: Nodes for each character are placed into a heap based on their frequency.
->Build the Tree: Repeatedly combine the two nodes with the smallest frequencies, creating a binary tree where each left branch gets a "0" and each right branch gets a "1".
->Generate Codes: Traverse the tree to assign binary codes to each character.
->Output: The result is the optimal Huffman codes for each character.

This results in an efficient way to encode data with variable-length codes, reducing the overall size for storage or transmission.

Greedy algorithm :A greedy algorithm is a problem-solving strategy that makes the locally optimal choice at each step with the hope of finding the global optimum.
'''