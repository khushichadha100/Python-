'''
import pandas as pd
import numpy as np
data = {'a' : 0., 'b' : 1., 'c' : 2.}
s = pd.Series(data,index=['b','c','d','a'])
print (s)

import pandas as pd1
import numpy as np1
data = {'p': 0., 'r': 1., 'e': 2.,'m': 2.}
s=pd1.Series(data,index=['b','c','d','a'])
print(s)

'''
import pandas as pd
import numpy as np
s = pd.Series('its empty', index=[0, 1, 2, 3])
#print s -----WITHOUT BRACKET ***********ERROR****************

import pandas as pd 
s = pd.Series([1,2,3,4,5],index = ['a','b','c','d','e'])
print (s['a']) #accessing the first element
print (s['c']) #accessing the THIRD element
print (s['e']) #accessing the LAST (fifth) element
            ########OR########
s = pd.Series([1,2,3,4,5],index = ['a','b','c','d','e'])
print (s[0]) #accessing the first element
print (s[2]) #accessing the THIRD element
print (s[4]) #accessing the LAST (fifth) element
