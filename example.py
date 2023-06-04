import pandas as pd
import random
lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI':lst})

data['whoAmI_robot'] = data['whoAmI'].map({'robot':1,'human':0})
data['whoAmI_human'] = data['whoAmI'].map({'robot':0,'human':1})
newData = data.drop('whoAmI',axis = 1)

print(newData.head(20))