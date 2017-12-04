import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler

df = pd.read_csv(
        filepath_or_buffer="vid_n_chan.txt",
        header=None,
        sep=","
        )

data = df.values.tolist()
data[178917] = [0.0, 0.0,0.0,0.0,0.0,0.0,0.0,0.0]
X = []
counter = 1
for each in data:
    print counter
    print map(int, each)
    X.append(map(int,each))
    counter += 1

scaler = StandardScaler(copy=True, with_mean=True, with_std=True)

# scaled, now can be concatenated with binary data
X_std = scaler.fit_transform(X)
print X_std[0]
one = np.array(X_std[0])
s = np.sum(one)
print "sum: ", s
one = one/np.sqrt(abs(np.sum(one)))

print np.dot(one, one)
