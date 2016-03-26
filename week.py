#week.py
weeks="星期一星期二星期三星期四星期五星期六星期日"
n=input("请输入数字(1-7):")
pos=3*(int(n)-1)
weeksabb=weeks[pos:pos+3]
print(weeksabb)