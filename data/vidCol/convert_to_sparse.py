import numpy as np
import scipy as sp
from collections import defaultdict
from collections import Counter
from scipy.sparse import csr_matrix
import sys

def build_matrix(docs):
    r""" Build sparse matrix from a list of documents, 
    each of which is a list of word/terms in the document.  
    """
    nrows = len(docs)
    idx = {}
    tid = 0
    nnz = 0
    for d in docs:
        nnz += len(set(d))
        for w in d:
            if w not in idx:
                idx[w] = tid
                tid += 1
    ncols = len(idx)
    # set up memory
    ind = np.zeros(nnz, dtype=np.int)
    val = np.zeros(nnz, dtype=np.double)
    ptr = np.zeros(nrows+1, dtype=np.int)
    i = 0  # document ID / row counter
    n = 0  # non-zero counter
    # transfer values
    for d in docs:
        cnt = Counter(d)
        keys = list(k for k,_ in cnt.most_common())
        l = len(keys)
        for j,k in enumerate(keys):
            ind[j+n] = idx[k]
            val[j+n] = cnt[k]
        ptr[i+1] = ptr[i] + l
        n += l
        i += 1
            
    mat = csr_matrix((val, ind, ptr), shape=(nrows, ncols), dtype=np.double)
    mat.sort_indices()
    
    return mat

def save_sparse_csr(filename, array):
    np.savez(filename,data = array.data ,indices=array.indices,indptr =array.indptr, shape=array.shape )

def load_sparse_csr(filename):
    loader = np.load(filename)
    return csr_matrix((loader['data'], loader['indices'], loader['indptr']),shape = loader['shape'])

if __name__ == "__main__":
    if len(sys.argv)-1 < 2:
        print "missing input."
    else:
        in_f = open(sys.argv[1], 'r')
        #out_f = open(sys.argv[2], 'w')

        data = []
        for line in in_f:
            term = line.split()
            if len(term) > 1:
                print term
                break
            data.append(term)
        mat = build_matrix(data)
        save_sparse_csr(sys.argv[2], mat)
        #for x in mat:
        #    for element in x.toarray()[0]:
        #        out_f.write(str(int(element)) + ",")

        #    out_f.write("\n")
        in_f.close()
        #out_f.close()
        
