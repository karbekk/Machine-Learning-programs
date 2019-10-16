
# coding: utf-8

# # DECISION TREE IMPLEMENTATION- ENTROPY AND INFO GAIN

# In[4]:


import pandas as pd 
from pandas import DataFrame

df_tennis = DataFrame.from_csv(r"C:\Users\Administrator\PycharmProjects\candidateelimination\tennis.csv")
df_tennis 


# In[6]:


def entropy(probs): 
    import math 
    return sum( [-prob*math.log(prob, 2) for prob in probs] )

def entropy_of_list(a_list): 
    from collections import Counter     
    cnt = Counter(x for x in a_list) 
    print("No and Yes Classes:",a_list.name,cnt)     
    num_instances = len(a_list)*1.0     
    probs = [x / num_instances for x in cnt.values()]     
    return entropy(probs) # Call Entropy:

total_entropy = entropy_of_list(df_tennis['PlayTennis']) 
print("Entropy of given PlayTennis Data Set:",total_entropy) 


# In[11]:


def information_gain(df, split_attribute_name, target_attribute_name, trace=0): 
    print("&&&&&&&&&")
    for name,group in df_split:         
        print(name)         
        print(group) 


# In[13]:


def information_gain(df, split_attribute_name, target_attribute_name, trace=0): 
    df_split = df.groupby(split_attribute_name)
    print("splitttttttttttttttttttt")
    print(split_attribute_name)
    print("******************")
    for name,group in df_split:         
        print("Name:",name)
        print("Group:",group)
    print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
    nobs = len(df.index) * 1.0
    df_agg_ent = df_split.agg({target_attribute_name : [entropy_of_list, lambda x: len(x)/nobs] })[target_attribute_name] 
    df_agg_ent.columns = ['Entropy', 'PropObservations'] 
    new_entropy = sum(df_agg_ent['Entropy'] * df_agg_ent['PropObservations'] )
    old_entropy = entropy_of_list(df[target_attribute_name]) 
    return old_entropy - new_entropy


# In[18]:


print('Info-gain for Outlook is :'+str( information_gain(df_tennis, 'Outlook', 'PlayTennis')),"\n") 
print('\n Info-gain for Humidity is: ' + str( information_gain(df_tennis, 'Humidity', 'PlayTennis')),"\n") 
print('\n Info-gain for Wind is:' + str( information_gain(df_tennis, 'Windy', 'PlayTennis')),"\n")
print('\n Info-gain for Temperature is:' + str( information_gain(df_tennis , 'Temperature','PlayTennis')),"\n") 


# In[21]:


def id3(df, target_attribute_name, attribute_names, default_class=None):
    from collections import Counter     
    cnt = Counter(x for x in df[target_attribute_name])
    if len(cnt) == 1:         
        return next(iter(cnt)) 
    elif df.empty or (not attribute_names): 
             return default_class 
    else:
        gainz = [information_gain(df, attr, target_attribute_name) for attr in attribute_names]
        print("ATTRIBUTE NAME:",attribute_names)
        index_of_max = gainz.index(max(gainz)) 
        best_attr = attribute_names[index_of_max] 
        tree = {best_attr:{}}
        remaining_attribute_names = [i for i in attribute_names if i != best_attr]
        for attr_val, data_subset in df.groupby(best_attr): 
            subtree = id3(data_subset,
                          target_attribute_name,                         
                          remaining_attribute_names,                         
                          default_class)
            tree[best_attr][attr_val] = subtree 
        return tree
     
        


# In[22]:


attribute_names = list(df_tennis.columns)
print("List of Attributes:", attribute_names) 
attribute_names.remove('PlayTennis') 
print("Predicting Attributes:", attribute_names)


# In[23]:


from pprint import pprint 
tree = id3(df_tennis,'PlayTennis',attribute_names)
print("\n\nThe Resultant Decision Tree is :\n") 
pprint(tree) 

