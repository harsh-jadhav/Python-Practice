class Node:
	def __init__(self, value):
		self.value = value
		self.left = None
		self.right = None


def branchSums(root):
	sums = []
	calculateBranchSums(root, 0, sums)
	return sums


def calculateBranchSums(node, runningSum, sums):

	# if node is none then return nothing
	if node is None:
		# print("reached end")
		return
	# print(node.value, node.left, node.right)
	# set the current running sum as runningSum  + node.value
	newRunningSum = runningSum + node.value
	# if the left and right node are None then we are at the leaf node 
	# hence append the current running sum as it will be the branch sum of that branch
	if node.left is None and node.right is None:
		sums.append(newRunningSum)
		return
	# recursively calculate sum for left and right node
	calculateBranchSums(node.left, newRunningSum, sums)
	print("DoneLeft", sums)
	calculateBranchSums(node.right, newRunningSum, sums)
	print("DoneRight", sums)



if __name__ == '__main__':

		 
	#        1 
	#       / \
	#      2   3
	#     / \ / \
	#    4  5 6 7
	#   / \  \
	#  8  9   10


	# root node as 1
	root = Node(1)
	# node left to root node as 2
	root.left = Node(2)
	# node right to root node as 3
	root.right = Node(3)
	# node left to node 2 as 4
	root.left.left = Node(4)
	# node right to node 2 as 5
	root.left.right = Node(5)
	# node left to node 4 as 8
	root.left.left.left = Node(8)
	# node right to node 4 as 9
	root.left.left.right = Node(9)
	# node right to node 5 as 10
	root.left.right.right = Node(10)
	# node left to node 3 as 6
	root.right.left = Node(6)		
	# node right to node 3 as 7
	root.right.right = Node(7)

	# print(root)
	print(branchSums(root))




