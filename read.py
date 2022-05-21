"""
流程：
1.建立GitHub專案
2.寫程式碼來讀取留言檔
3.測試印出data清單
4.只印出第0筆看看
5.讀取檔案的過程中 印出len(data)才知道讀取進度
6.建立版本上傳GitHub
7.算留言平均長度
8.建立版本上傳GitHub
"""


data = []
count = 0
with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
		count += 1
		if count % 10000 == 0:
			print(len(data)) # print很花時間,每1000筆才印一次
		
print('檔案讀取完了，總共有', len(data), '筆資料')

sum_len = 0
for d in data:
	sum_len = sum_len + len(d)
print('每筆留言的平均長度為', sum_len / len(data))


"""
清單做篩選
流程：
1.篩選概念
2.印篩選完的東西看看
3.建立版本上傳
4.另外一個篩選範例
"""

new = []
for d in data:
	if len(d) < 100:
		new.append(d)
print('一共有', len(new), '筆留言長度小於100')
print(new[0])
print('----------------')
print(new[1])