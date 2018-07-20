data = []
count = 0
with open('reviews.txt', 'r') as f:
	for line in f:#一行一行讀數據檔
		data.append(line)
		count += 1
		if count % 1000 == 0: # %是一種運算符號: 求餘數
			print(len(data))
print('檔案讀取完了，總共有:', len(data), '筆資料')

sum_len = 0 #add up
for d in data:
	sum_len = sum_len + len(d)

print('留言的平均長度為', sum_len/len(data))

new = []
for d in data: #d為每一筆你要叫出來的東西
	if len(d) < 100:
		new.append(d) #d這個留言裝進new清單
print('一共有', len(new), '筆留言長度小於100')
print(new[0])
