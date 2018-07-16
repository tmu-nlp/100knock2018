
# coding: utf-8

# In[17]:


from sklearn.externals import joblib
import numpy as np
from knock82 import VOCAB_PATH, COOC_MAT_PATH
import scipy.sparse as smat

PMI_PATH = 'ppmi.joblib'

vocab = joblib.load(VOCAB_PATH).vocabulary_
ftc = joblib.load(COOC_MAT_PATH)
N = np.sum(ftc)


# In[41]:


ft_ = np.sum(ftc, axis = 1)
f_c = np.sum(ftc, axis = 0)
xtc = np.empty_like(ftc, dtype = np.float32)
xtc[:,:] = np.outer(ft_, f_c)
xtc[np.where(ftc < 10)] = 0

t_rows, c_cols = np.where(xtc > 0) # same as xtc.nonzero()
ppmi = smat.lil_matrix(xtc.shape, dtype = np.float32)
for t, c in zip(t_rows, c_cols):
    ppmi[t, c] = max(0, np.log(N*ftc[t,c]/xtc[t,c])) # not meet np.max
t_rows, c_cols = ppmi.nonzero()
n = len(t_rows)
n = n / xtc.shape[0] / xtc.shape[1] * 100
print("Non-zero percentage:", t_rows)

joblib.dump(ppmi, PMI_PATH)

# Non-zero percentage: 0.002749996788324919