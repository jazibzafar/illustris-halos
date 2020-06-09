import numpy as np
import h5py

if __name__ == "__main__":
    # subhalo = h5py.File("Data/groups_135.0.hdf5", 'r')
    with h5py.File("data/groups_135.0.hdf5", 'r') as hdf:
        base_items = list(hdf.items())
        print(base_items)
        Subhalo = hdf.get('Subhalo')
        print("subhalo", Subhalo)
        Subhalo_items = list(Subhalo.items())
        print(Subhalo_items)
        SubhaloBHMass = np.array(Subhalo.get("SubhaloBHMass"))
        print(SubhaloBHMass.shape)
        print(SubhaloBHMass)
