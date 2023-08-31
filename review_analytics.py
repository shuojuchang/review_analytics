data = []
count = 0
with open('reviews.txt', 'r') as f:
    for line in f:
        data.append(line)
        count = count + 1
        if count % 1000 == 0:
            print(len(data))
print('讀取完畢,一共有', len(data), '筆資料')
#len(data) 即為清單總筆數


# 要知道這一百萬筆的留言總平均長度為何?
sum_len = 0
for d in data: #每一筆在清單裡的資料 ; data即為清單
    sum_len = sum_len + len(d)
    average = sum_len/len(data)
print('平均留言長度為', average, '筆')


#把留言長度小於100的列到一個清單
new = []
for d in data:   #d為每一筆留言
    if len(d) < 100:
        new.append(d)
print('一共有', len(new), '筆留言低於100字')


#計算留言有包含'good'的筆數
good = []
for d in data:
    if 'good' in d:
        good.append(d)
print('一共有', len(good), '筆留言是包含good')
print(good[0])