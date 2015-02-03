import scipy.io as scio
import scipy.signal as sig
import matplotlib.pyplot as plt
#from matplotlib.figure import Figure

nidaqDir = '/Users/wgillis/gdrive/To Download/Lab Data/Ephys/TDT/Unsorted/Block-91'

# This only works for matlab files that are below verson 7.3
d = scio.loadmat(nidaqDir + '/data.mat', squeeze_me=True, struct_as_record=False)

# otherwise hdf5 must be used via h5py

da = d['data']

filterParams = sig.ellip(5, .2, 60, [300.0/(da.fs/2), 2e3/(da.fs/2)], 'bandpass')

filtData = sig.filtfilt(filterParams[0], filterParams[1], da.voltage[0,:])

fig = plt.figure(1)
plt.plot(filtData)
plt.title('Filtered 91')
plt.savefig('1.png')

fig2 = plt.figure(2)
plt.plot(da.voltage[0,:], '.')
plt.title('Unfiltered Block-91')
plt.savefig('2.png')

# In[ ]:



