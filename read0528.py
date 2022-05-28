data = []
count = 0
with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
		count += 1
		if count % 10000 == 0:
			print(len(data)) # print很花時間,每1000筆才印一次
		
print('檔案讀取完了，總共有', len(data), '筆資料')
print(data[0])

sum_len = 0
for d in data:
	sum_len = sum_len + len(d)
print('每筆留言的平均長度為', sum_len / len(data))

new = []
for d in data:
	if len(d) < 100:
		new.append(d)
print('一共有', len(new), '筆留言長度小於100')
print(new[0])
print('----------------')
print(new[1])

good = []
for d in data:
	if 'good' in d:
		good.append(d)

print('一共有', len(good), '筆留言提到good')


# 文字計數
# nested for loop 巢狀迴圈
wc = {} # word_count
for d in data:
	words = d.split()
	for word in words:
		if word in wc:
			#計數+1
			wc[word] += 1
		else:
			#新增key進字典 {key: value}
			wc[word] = 1

for word in wc:
	if wc[word] >1000000:
		print(word, wc[word])
#字典的長度，有多少個key
print(len(wc))

while True:
	word= input('請問你想要查什麼字：')
	if word == 'q':
		break
	if word in wc:
		print(word, '出現過的次數為', wc[word])
	else:
		print('沒出現過哦')
print('感謝使用本查詢功能')


	

