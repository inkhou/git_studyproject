#coding="utf-8"

def test(a):
	b = type(a)
	return b

def main():
	result = test("123")
	print(result)

if __name__ == '__main__':
	main()