import matplotlib.pyplot as plt
cities=['delhi','mumbai','bangalore','hyderabad']
population=[23456123,20083104,18456123,13411093]
plt.barh(cities,population)
plt.xlabel('cities')
plt.ylabel('population')
plt.show()

'''
import matplotlib.pyplot as plt
import pandas as pd
data={'name':['arnav','sheela','azhar','bincy','yash','nazar'],
'height':[60,61,63,65,61,60],
'weight':[47,89,52,58,50,47]}
df=pd.DataFrame(data)
df.plot(kind='hist')
plt.show()
'''

























