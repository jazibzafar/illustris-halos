#!/usr/bin/env python
# coding: utf-8

# In[81]:


import numpy as np
import h5py


# In[169]:


with h5py.File('groups_135.0.hdf5', 'r') as hdf:
    base_items = list(hdf.items())
    print('items in base_items are', base_items)
    Group = hdf.get('Group')
    Group_items = list(Group.items())
#     print('items in Group are', Group_items)
    GroupBHMass = np.array(Group.get('GroupBHMass'))
    print('GroupBHMass contains', GroupBHMass)
    GroupBHMdot = np.array(Group.get('GroupBHMdot'))
    print('GroupBHMdot contains', GroupBHMdot)
    GroupFirstSub = np.array(Group.get('GroupFirstSub'))
    print('GroupFirstSub contains', GroupFirstSub)
    GroupGasMetallicity = np.array(Group.get('GroupGasMetallicity'))
    print('GroupGasMetallicity contains', GroupGasMetallicity)
    GroupLen = np.array(Group.get('GroupLen'))
    print('GroupLen contains', GroupLen)
    GroupLenType = np.array(Group.get('GroupLenType'))
    print('GroupLenType contains', GroupLenType)
    GroupMass = np.array(Group.get('GroupMass'))
    print('GroupMass contains', GroupMass)
    GroupMassType = np.array(Group.get('GroupMassType'))
    print('GroupMassType contains',GroupMassType)
    GroupNsubs = np.array(Group.get('GroupNsubs'))
    print('GroupNsubs contains', GroupNsubs)
    GroupPos = np.array(Group.get('GroupPos'))
    print('GroupPos contains',GroupPos)
    GroupSFR = np.array(Group.get('GroupSFR'))
    print('GroupSFR contains', GroupSFR)
    GroupStarMetallicity = np.array(Group.get('GroupStarMetallicity'))
    print('GroupStarMetallicity contains',GroupStarMetallicity)
    GroupVel= np.array(Group.get('GroupVel'))
    print('GroupVel contains', GroupVel)
    GroupWindMass = np.array(Group.get('GroupWindMass'))
    print('GroupWindMass contains',GroupWindMass)
    Group_M_Crit200 = np.array(Group.get('Group_M_Crit200'))
    print('Group_M_Crit200 contains', Group_M_Crit200)
    Group_M_Crit500 = np.array(Group.get('Group_M_Crit500'))
    print('Group_M_Crit500 contains',Group_M_Crit500)
    Group_M_Mean200 = np.array(Group.get('Group_M_Mean200'))
    print('Group_M_Mean200 contains', Group_M_Mean200)
    Group_M_TopHat200 = np.array(Group.get('Group_M_TopHat200'))
    print('Group_M_TopHat200',Group_M_TopHat200)
    Group_R_Crit200 = np.array(Group.get('Group_R_Crit200'))
    print('Group_R_Crit200 contains', Group_R_Crit200)
    Group_R_Crit500 = np.array(Group.get('Group_R_Crit500'))
    print('Group_R_Crit500',Group_R_Crit500)
    Group_R_Mean200 = np.array(Group.get('Group_R_Mean200'))
    print('Group_R_Mean200 contains', Group_R_Mean200)
    Group_R_TopHat200 = np.array(Group.get('Group_R_TopHat200'))
    print('Group_R_TopHat200',Group_R_TopHat200)
    print(GroupBHMass.shape)
    
    
    
#     Group_datasets = ['GroupBHMass', 'GroupBHMdot', 'GroupFirstSub', 'GroupGasMetallicity', 'GroupLen','GroupLenType','GroupMass', 'GroupMassType', 'GroupNsubs', 'GroupPos', 'GroupSFR', 'GroupStarMetallicity','GroupVel','GroupWindMass','Group_M_Crit200','Group_M_Crit500','Group_M_Mean200','Group_M_TopHat200','Group_R_Crit200','Group_R_Crit500','Group_R_Mean200','Group_R_TopHat200']
#     print(Group_datasets)
    
#     for i in range(23):
#         Group_datasets = np.array(Group.get(Group_datasets[i]))
    


# In[ ]:





# In[191]:


Group_datasets = ['GroupBHMass', 'GroupBHMdot', 'GroupFirstSub', 'GroupGasMetallicity', 'GroupLen','GroupLenType','GroupMass', 'GroupMassType', 'GroupNsubs', 'GroupPos', 'GroupSFR', 'GroupStarMetallicity','GroupVel','GroupWindMass','Group_M_Crit200','Group_M_Crit500','Group_M_Mean200','Group_M_TopHat200','Group_R_Crit200','Group_R_Crit500','Group_R_Mean200','Group_R_TopHat200']

print(Group_datasets)
len(Group_datasets)


# In[193]:


#base_items
hdf5_groups = []
for i in range(4): 
    print(i)
    hdf5_groups = base_items[i]
    print(hdf5_groups)
    


# In[171]:


with h5py.File('groups_135.0.hdf5', 'r') as hdf:
    base_items = list(hdf.items())
    Group = hdf.get('Group')
    Group_items = list(Group.items())
    #print('itemsin Group are', Group_items)
    GroupNsubs = np.array(Group.get('GroupNsubs'))
    print('GroupNsubs Contains', GroupNsubs)
    
    print(sum(GroupNsubs))


# In[124]:


hdf5_groups


# In[90]:


with h5py.File('groups_135.0.hdf5', 'r') as hdf:
    base_items = list(hdf.items())
    Group = hdf.get('Group')
    Group_items = list(Group.items())
    #print('itemsin Group are', Group_items)
    GroupNsubs = np.array(Group.get('GroupNsubs'))
    print('GroupNsubs Contains', GroupNsubs)
    


# In[85]:


# we subtract 1 from each entry in GroupNsubs to get the true number of satellites
# These will serve as our labels

GroupNsubs_true = GroupNsubs - 1
print(GroupNsubs_true)


# In[86]:


with h5py.File('groups_135.0.hdf5', 'r') as hdf:
    base1_items = list(hdf.items())
    Subhalo = hdf.get('Subhalo')
    Subhalo_items = list(Subhalo.items())
    print('items in Subhalo are' , Subhalo_items)
    


# In[170]:


with h5py.File('groups_135.0.hdf5', 'r') as hdf:
    base1_items = list(hdf.items())
    Subhalo = hdf.get('Subhalo')
    SubhaloGrNr= np.array(Subhalo.get('SubhaloGrNr'))
    print(SubhaloGrNr)
    print(SubhaloGrNr.shape)


# In[80]:


with h5py.File('groups_135.0.hdf5', 'r') as hdf:
    base_items = list(hdf.items())
    Group = hdf.get('Group')
    GroupFirstSub = np.array(Group.get('GroupFirstSub'))
    print('GroupFirstSub Contains', GroupFirstSub) # This corresponds to the index of the first/primary subhalo group within a specific FoF group
    # So if you look at GroupNsubs then the first entry is 16936 which means that the index of the primary subhalo in the 1st FOF halo is 0.
    # the index of the the primary halo in the second FOF group is 16937 because it has to be the index of the first subhalo in the second FOF group.


# In[ ]:



Christoph Behrens (behrens11)
4:07 PM
hdf["Group_R_TopHat200"][:]

Ch
Christoph Behrens (behrens11)
4:08 PM
hdf["Group/Group_R_TopHat200"][:]


# In[187]:


import numpy as np
import h5py


class ReadData:
    def __init__(self, filename, group):
        self.file = filename
        self.data = h5py.File(filename, 'r')
        self.group = self.data.get(group)

    def getgroupitems(self, groupname):
        group_items = list(self.group.items())
        return group_items

    def getgroupattributes(self, attributename):
        attr = np.array(self.group.get(attributename))
        return attr


# In[188]:


Halo_Data = ReadData('groups_135.0.hdf5','Group')


# In[189]:


import numpy as np
import h5py

def get_dataset(prefix,name):
    for i in range(0,8):
        fn = prefix+".{:d}.hdf5".format(i)
        
        with h5py.File(fn,"r") as f:
            #read the data for each file
            d=(f[name][:])
            if(i==0):
                array = d
            else:
                array = np.append(array,d)
    print (array.shape)
    return array
def do_check(firstsub,nsub,grnr):
    #checks if all the halos that have subhalos have their firstsub index set correctly, i.e. each
    #first subhalo of a group links back to the host group
    for i in range(0,nsub.size):
        if(nsub[i]==0):
            continue
        else:
            mysubhalos_index = range(firstsub[i],firstsub[i]+nsub[i])
            mysubhalos_parent = grnr[mysubhalos_index]
            if(any(mysubhalos_parent!=i)):
                raise NameError("this should not happen")
    else:
        print ("all good!")
        


# In[ ]:




