def find_common_elements(ls1, ls2):
	''' Takes in 2 lists, returns a new list containing
	the common elements between the 2 input lists'''
	common_ls = []
	for i in ls1:
		for j in ls2:
			if i == j:
				common_ls.append(i)
				break
	print(common_ls)


find_common_elements([1,2,55,66,8,9], [4,5,6,55,66])

