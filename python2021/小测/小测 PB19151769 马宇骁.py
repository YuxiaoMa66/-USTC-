# write solution here
import numpy as np
fs = np.array([1,1,2,3,5,8,13,21,34,55,89,144,223,369,592,961,1553,2514,4067,6581])
fs2 = fs**2
fs3 = fs%2==0
fs4 = [str(i) for i in fs]
fs5 = [str(i) for i in fs]
for i in range(len(fs4)):
    fs4[i] = fs4[i][-1]
    fs5[i] = fs5[i][-1] if (len(fs5[i])>1) else 0
fs4 = np.array(fs4).astype(np.int)
fs5 = np.array(fs5).astype(np.int)