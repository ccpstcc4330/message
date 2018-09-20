#文字的計數

data = []
count = 0
with open('reviews.txt', 'r') as f:
	for line in f:#一行一行讀數據檔
		data.append(line)
		count += 1
		if count % 1000 == 0: # %是一種運算符號: 求餘數
			print(len(data))
print('檔案讀取完了，總共有:', len(data), '筆資料')

#以下結構超重要:
wc = {} #word_count = wc
for d in data: #d 是一筆留言，data是一筆清單 
	words = d.split(' ') #將清單裡的留言分開，遇到空白鍵就分割
	for word in words: #forloop讀取每一個字
		if word in wc:
			wc[word] += 1 #(找到一次word就加一次,+= 代表累加)
		else:
			wc[word] = 1 #新增新的key進字典

for word in wc:
	if wc[word] > 1000000:
		print(word, wc[word])

print(len(wc)) #看字典裡總共幾個字

while True:
	word = input('請問你要查什麼字?')
	if word == 'q':
		break
	if word in wc:	
		print(word, '出現過的次數為:', wc[word])
	else:
		print('沒有這個字喔!')
print('感謝使用本查詢功能!')