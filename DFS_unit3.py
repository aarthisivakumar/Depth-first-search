#!/usr/bin/env python
# coding: utf-8

# <<<Depth First Search

# depth first is a algorithm for traversing in graph

# STACK OPERATIONS:-
# 1.push()
# 2.pop()
# 3.size()
# 4.top()
# in stack the values can be added only at the end

# In[3]:


graph={
    'start':['A','B'],
    'A':['start','E','F'],
    'B':['start','D','C'], 
    'C':['B'],
    'D':['B','Goal'],
    'E':['B','G'],
    'F':['B'],
    'G':['E'],
    'Goal':['E','F']
}


# In[4]:


graph


# In[5]:


def dfs(graph,start,goal,visited):
    stack=[start]
    while stack:
        node=stack.pop()
        if node not in visited:
            visited.append(node)
            if node==goal:
                print(visited)
            for neighbours in graph[node]:
                dfs(graph,neighbours,goal,visited)


# In[9]:


dfs(graph,"start","Goal",[])


# In[ ]:


def factorial(n):
    if n==


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




