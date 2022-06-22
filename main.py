# ------------------------For Nested Loops------------------------
for i in range(3):
	for j in range(2):
		print(i, j)

for i in range(3):
	print('===> First Loop')
	print(f'i={i}')
	for j in range(2):
		print('Second Loop')
		print(f'j = {j}')

num_rows = 5
for i in range(5):
	for num_cols in range(num_rows-i):
		print('*', end='')
	print()
