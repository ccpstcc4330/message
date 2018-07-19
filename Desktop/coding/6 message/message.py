data = []
count = 0
with open('reviews.txt', 'r') as f:
	for line in f:#一行一行讀數據檔
		data.append(line)
		count += 1
		if count % 1000 == 0: # %是一種運算符號: 求餘數
			print(len(data))
print(len(data))
print(data[0])
print('---------------------')
print(data[1])