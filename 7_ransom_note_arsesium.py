magazine = "two times three is not four".split(" ")
note = "two times two is four".split(" ")

# def checkMagazine(magazine, note): 
# 	temp = []
# 		for i in note:
# 			if i in magazine:
# 				temp.append(i)
# 				magazine.remove(i)

# 		if len(temp) == len(note):
# 			print("Yes")
# 		else:
# 			print("No")

# checkMagazine(magazine, note)

from collections import Counter
def checkMagazine(magazine, note): 
	m = Counter(magazine)
	n = Counter(note)
	temp = 1
	for k, v in n.items():
		if k  in m and m[k] >= v:
			continue
		else:
			temp = 0
			break

	if temp:
		print("Yes")
	else:
		print("No")

# checkMagazine(magazine, note)


def checkMagazine2(magazine, note): 
	m = Counter(magazine)
	n = Counter(note)
	temp = 1
	if n-m=={}:
		print("Yes")
	else:
		print("No")

checkMagazine2(magazine, note)