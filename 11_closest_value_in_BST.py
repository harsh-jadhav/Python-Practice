tree = [10, 5, 15, 2, 5, 13, 22, 14]
target = 25


def closestValueInBST(tree, target):
	if target in tree:
		return target
	else:
		b = [target] * len(tree)

		c = [abs(tree[i]-b[i]) for i in range(len(tree))]

		return tree[c.index(min(c))]

print(closestValueInBST(tree, target))