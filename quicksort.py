def quicksort(my_list):
	if len(my_list) > 0:
		pivot = my_list[0]
		less = quicksort([x for x in my_list[1:] if x < pivot])
		great = quicksort([x for x in my_list[1:] if x > pivot])
		return less + [pivot] + great
	else:
		return []

def main():
	print(quicksort([4, 1, 2, 4, 2, 6, 11, 9, 3, 5, 8]))

if __name__ == '__main__':
	main()