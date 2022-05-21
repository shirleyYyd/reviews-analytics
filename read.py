'''
流程：
1.建立GitHub專案
2.寫程式碼來讀取留言檔
3.測試印出data清單
4.只印出第0筆看看
5.讀取檔案的過程中 印出len(data)才知道讀取進度
6.建立版本上傳GitHub
7.算留言平均長度
8.建立版本上傳GitHub
'''


data = []
count = 0
with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
		count += 1
		if count % 10000 == 0:
			print(len(data)) # print很花時間,每1000筆才印一次
		
print(data[0])

print('-----------------------')

print(data[1])