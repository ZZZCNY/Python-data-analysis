import matplotlib.pyplot as plt
import random
gradewords=('优秀','良好','中等','及格','不及格')
testwords=[random.choice(gradewords) for i in range(1000)]
result=dict()
for item in testwords:
    if item in testwords:
        result[item]=result.get(item,0)+1
for key,v in result.items():
    print(key,v,sep='--->')
plt.pie(result.values(),labels=result.keys(),autopct='%.2f%%')
plt.show()