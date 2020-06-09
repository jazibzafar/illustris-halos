import numpy as np
import h5py


class ReadData:
    def __init__(self, filename, group):
        self.file = filename
        self.data = h5py.File('data/'+filename, 'r')
        self.group = self.data.get(group)

    def getgroupitems(self, groupname):
        group_items = list(self.group.items())
        return group_items

    def getgroupattributes(self, attributename):
        attr = np.array(self.group.get(attributename))
        return attr
