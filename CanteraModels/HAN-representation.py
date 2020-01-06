#!/usr/bin/env python
# coding: utf-8

# # Representing HAN
# This notebook explores ways to represent HAN in RMG

# In[1]:


import os, sys
rmg_path = os.getenv('RMGpy')
if rmg_path not in sys.path:
    sys.path.append(rmg_path)
sys.path

import rmgpy
print(f"RMG-Py Version {rmgpy.__version__}")
print(rmgpy.__file__)


# In[2]:


from rmgpy.molecule import Molecule


# These are the two forms of HAN, from Bannerjjee (2016), Ionic and Covalent. The Ionic form is marginally more stable, and the covalent form always becomes the ionic form when adsorbed on a metal.
# ![bannerjee-han-structures.png](attachment:bannerjee-han-structures.png)

# ## Covalent HAN

# In[3]:


no3h = Molecule().from_adjacency_list("""
NO3h
1 O u0 p2 c0 {2,S} {5,S}
2 N u0 p0 c+1 {1,S} {3,S} {4,D}
3 O u0 p3 c-1 {2,S}
4 O u0 p2 c0 {2,D}
5 H u0 p0 c0 {1,S}
""")
no3h


# In[4]:


nh2oh = Molecule().from_adjacency_list("""
NH2OH
1 N u0 p1 c0 {2,S} {3,S} {4,S}
2 O u0 p2 c0 {1,S} {5,S}
3 H u0 p0 c0 {1,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {2,S}
""")
nh2oh


# In[5]:


# This is the covalent form of HAN
no3h_h2noh =  Molecule().from_adjacency_list("""
no3h_h2noh
1  O u0 p3 c-1 {2,S} {10,H}
2  N u0 p0 c+1 {1,S} {3,D} {4,S}
3  O u0 p2 c0 {2,D}
4  O u0 p2 c0 {2,S} {7,S}
5  N u0 p1 c0 {6,S} {8,S} {9,S} {7,H}
6  O u0 p2 c0 {5,S} {10,S}
7  H u0 p0 c0 {4,S} {5,H}
8  H u0 p0 c0 {5,S}
9  H u0 p0 c0 {5,S}
10 H u0 p0 c0 {6,S} {1,H}
""")
no3h_h2noh
# the image is not drawn well because the H-bonds are ignored 
# and two halves end up superimposed on top of each other


# In[6]:


no3h_h2noh.to_smiles()


# In[7]:


for a in no3h_h2noh.atoms:
    print(a, no3h_h2noh.get_bonds(a))


# In[8]:


# It seems there are are other H-bonds that can be formed
for m in no3h_h2noh.generate_h_bonded_structures():
    print(m.to_adjacency_list())


# In[9]:


# Unfortunately, generating resonance structures fails
for m in no3h_h2noh.generate_resonance_structures():
    print(m.to_adjacency_list())


# ## Ionic HAN

# In[10]:


# This is the ionic form of HAN
no3_h3noh =  Molecule().from_adjacency_list("""
no3-_h3noh+
1  O u0 p3 c-1 {2,S} {10,H}
2  N u0 p0 c+1 {1,S} {3,D} {4,S}
3  O u0 p2 c0 {2,D}
4  O u0 p3 c-1 {2,S} {7,H}
5  N u0 p0 c+1 {6,S} {8,S} {9,S} {7,S}
6  O u0 p2 c0 {5,S} {10,S}
7  H u0 p0 c0 {4,H} {5,S}
8  H u0 p0 c0 {5,S}
9  H u0 p0 c0 {5,S}
10 H u0 p0 c0 {6,S} {1,H}
""")
no3_h3noh
# the image is not drawn well because the H-bonds are ignored 
# and two halves end up superimposed on top of each other


# In[11]:


no3_h3noh.to_smiles()


# In[12]:


for a in no3h_h2noh.atoms:
    print(a, no3h_h2noh.get_bonds(a))


# In[13]:


# It seems there are are other H-bonds that can be formed
for m in no3_h3noh.generate_h_bonded_structures():
    print(m.to_adjacency_list())


# In[14]:


# Unfortunately, generating resonance structures fails here too
for m in no3_h3noh.generate_resonance_structures():
    print(m.to_adjacency_list())


# ## Other Fragments

# In[15]:


no3j = Molecule().from_adjacency_list("""
NO3j
1 O u1 p2 c0 {2,S}
2 N u0 p0 c+1 {1,S} {3,S} {4,D}
3 O u0 p3 c-1 {2,S}
4 O u0 p2 c0 {2,D}
""")
no3j


# ## More exploring of structures...

# In[17]:


# This is the covalent form of HAN, without the H bonds
no3h_h2noh =  Molecule().from_adjacency_list("""
no3h_h2noh
1  O u0 p3 c-1 {2,S}
2  N u0 p0 c+1 {1,S} {3,D} {4,S}
3  O u0 p2 c0 {2,D}
4  O u0 p2 c0 {2,S} {7,S}
5  N u0 p1 c0 {6,S} {8,S} {9,S}
6  O u0 p2 c0 {5,S} {10,S}
7  H u0 p0 c0 {4,S}
8  H u0 p0 c0 {5,S}
9  H u0 p0 c0 {5,S}
10 H u0 p0 c0 {6,S}
""")
no3h_h2noh
# the image is not drawn well because the H-bonds are ignored 
# and two halves end up superimposed on top of each other


# In[18]:


for m in no3h_h2noh.generate_resonance_structures():
    print(m.to_adjacency_list())


# In[19]:


# This is the ionic form of HAN, without the H bonds
no3_h3noh =  Molecule().from_adjacency_list("""
no3-_h3noh+
1  O u0 p3 c-1 {2,S}
2  N u0 p0 c+1 {1,S} {3,D} {4,S}
3  O u0 p2 c0 {2,D}
4  O u0 p3 c-1 {2,S}
5  N u0 p0 c+1 {6,S} {8,S} {9,S} {7,S}
6  O u0 p2 c0 {5,S} {10,S}
7  H u0 p0 c0 {5,S}
8  H u0 p0 c0 {5,S}
9  H u0 p0 c0 {5,S}
10 H u0 p0 c0 {6,S}
""")
no3_h3noh
# the image is not drawn well because the H-bonds are ignored 
# and two halves end up superimposed on top of each other


# In[20]:


for m in no3_h3noh.generate_resonance_structures():
    print(m.to_adjacency_list())


# In[ ]:




