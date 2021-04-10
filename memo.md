## 丸め

### 切り捨て

7 // 2 # 3

## 変換

str(10)
int('10')

## max, min

min(a,b)
max(a,b)

## 文字を Unicode ポイントに変換

print(ord('a')) # 97
print(ord('あ')) # 12354

アルファベット → 最大 128

## range

range(5) #0,1,2,3,4
range(1,5) #1,2,3,4
range(1,10,2) #1,3,..,9
range(1,5,-1) #4,3,2,1

# 配列

## 結合

a = [1,2]
b = [3,4]
a.extend(b) #[1,2,3,4]

## 並べ替え

[2,3,1].sort() # [1,2,3]
[2,3,1].reverse() # [1,3,2]

元の配列はそのままにするには slice 使う
a = [2,3,1][::-1]

## join

a = ['python', 'list', 'exchange']
b = ','.join(str_list) # python,list,exchange

# 文字列

## 切り取り

### 両端

s = 'aaaBBBaaaCCCaaa'
t = s.strip('a') # 'BBBaaaCCC'

s = ' abc '
t = s.strip() # 'abc'

### 先頭のみ

lstrip

### 末尾のみ

rstrip
