import pandas as pd 

data = {
  '이름' : ['쿠키', '판다', '펭귄', '사나', '나연', '모모'],
  '특기' : ['춤', '노래', '예능', '물고기', '헤엄', '비행'],
  '음식' : ['피자', '알파고', '문장', '아다곤예', '엘리너', '큐밥']
}

df = pd.DataFrame(data)
print(df)
