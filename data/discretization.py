import pandas as pd
import numpy as np

df = pd.read_csv(
        filepath_or_buffer="vid_n_chan.txt",
        header=None,
        sep=","
        )

#col0 = df.iloc[:,0].values.tolist()
col1 = df.iloc[:,6].values.tolist()
#col2 = df.iloc[:,2].values.tolist()
#col3 = df.iloc[:,3].values.tolist()
#col4 = df.iloc[:,4].values.tolist()
#col5 = df.iloc[:,5].values.tolist()
#col6 = df.iloc[:,6].values.tolist()

#hist, bin_edges0 = np.histogram(col0,bins=100, density=True)
hist, bin_edges1 = np.histogram(col1,bins=100, density=True)
#hist, bin_edges2 = np.histogram(col2,bins="doane", density=True)
#hist, bin_edges3 = np.histogram(col3,bins="doane", density=True)
#hist, bin_edges4 = np.histogram(col4,bins="doane", density=True)
#hist, bin_edges5 = np.histogram(col5,bins="doane", density=True)
#hist, bin_edges6 = np.histogram(col6,bins="doane", density=True)

#column0 = np.digitize(col0, bin_edges0)
column1 = np.digitize(col1, bin_edges1)
#column2 = np.digitize(col2, bin_edges2)
#column3 = np.digitize(col3, bin_edges3)
#column4 = np.digitize(col4, bin_edges4)
#column5 = np.digitize(col5, bin_edges5)
#column6 = np.digitize(col6, bin_edges6)
print len(set(column1))

output = open("col7.txt", 'w')

for each in column1:
    output.write(str(each) + ",\n")

output.close()
