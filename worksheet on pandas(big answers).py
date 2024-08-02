import pandas as pd
df1=pd.DataFrame({"key":["a","b","c","d"], "value":[1,2,3,4]})
df2=pd.DataFrame({"key":["a","b","e","b"], "value":[5,6,7,8]})
df3=df1.merge(df2, on="key", how="outer")
print(df3)

import pandas as pd
df1=pd.DataFrame({"key":["a","b","c","d"], "value":[1,2,3,4]})
df2=pd.DataFrame({"key":["a","b","e","b"], "value":[5,6,7,8]})
df3=df1.merge(df2, on="key", how="inner")
print(df3)

import pandas as pd
df1=pd.DataFrame({"key":["a","b","c","d"], "value":[1,2,3,4]})
df2=pd.DataFrame({"key":["a","b","e","b"], "value":[5,6,7,8]})
df3=df1.merge(df2, on="key", how="left")
print(df3)

import pandas as pd
df1=pd.DataFrame({"key":["a","b","c","d"], "value":[1,2,3,4]})
df2=pd.DataFrame({"key":["a","b","e","b"], "value":[5,6,7,8]})
df3=df1.merge(df2, on="key", how="right")
print(df3)

import pandas as pd
df = pd.DataFrame([45,50,41,56], index = [True, False, True, False])
print(df.iloc[True])







