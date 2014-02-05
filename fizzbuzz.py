# Written in Python 3
def fizzbuzz(seq):
	output = []
	for i in range(1, seq, 1):
		if i % 3 == 0:
			output.append("fizz")
		elif i % 5 == 0:
			output.append("buzz")
		else:
			output.append(str(i))
	return output

def main():
	print(", ".join(fizzbuzz(int(input("FizzBuzz: ")))))
if __name__ == '__main__':
		main()