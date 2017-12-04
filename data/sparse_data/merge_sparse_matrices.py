import numpy as np
from scipy.sparse import csr_matrix, hstack, save_npz

def load_sparse_csr(filename):
    loader = np.load(filename)
    return csr_matrix((loader['data'], loader['indices'], loader['indptr']),shape = loader['shape'])

def save_sparse_csr(filename, array):
    np.savez(filename,data = array.data ,indices=array.indices,indptr =array.indptr, shape=array.shape )

if __name__ == "__main__":
    categories = "sparse_categories.txt.npz"
    titles = "sparse_title.txt.npz"
    tags = "sparse_tags.txt.npz"
    col1 = "sparse_col1.txt.npz"
    col2 = "sparse_col2.txt.npz"
    col3 = "sparse_col3.txt.npz"
    col4 = "sparse_col4.txt.npz"
    col5 = "sparse_col5.txt.npz"
    col6 = "sparse_col6.txt.npz"
    col7 = "sparse_col7.txt.npz"
    cat = load_sparse_csr(categories)
    tit = load_sparse_csr(titles)
    tag = load_sparse_csr(tags)
    one = load_sparse_csr(col1)
    two = load_sparse_csr(col2)
    three = load_sparse_csr(col3)
    four = load_sparse_csr(col4)
    five = load_sparse_csr(col5)
    six = load_sparse_csr(col6)
    seven = load_sparse_csr(col7)

    print "shape of categories: ", cat.get_shape()
    print "shape of titles: ", tit.get_shape()
    print "shape of tags: ", tag.get_shape()
    result = hstack([cat, tit, tag, one, two, three, four, five, six, seven])
    save_npz('main_data.npz', result)
    #save_sparse_csr("full_data", result)
    print "shape of result: ", result.get_shape()
