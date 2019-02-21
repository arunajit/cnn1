def word_seq(seq, k, stride=1):
    i = 0
    words = []
    while i <= len(seq) - k:
        words.append(seq[i: i + k])
        i += stride
    return words

def create_dict(nclt):
    vec_dict = {}
    pmu = k_len_perm(nclt, 3)
    pmu.sort()
    for idx, seq in enumerate(pmu):
        hot_vec = [ 0 for i in range(0, len(pmu))]
        hot_vec[idx] = 1
        vec_dict[seq] = hot_vec
    return vec_dict

def k_len_perm(letters, k):
    n = len(letters)
    pmu = []
    k_len_perm_hlpr(pmu, letters, "", n, k)
    return pmu

def k_len_perm_hlpr(pmu, letters, prefix, n, k):
    if (k == 0):
        pmu.append(prefix)
        return
    for i in range(0, n):
        newPrefix = prefix + letters[i]
        k_len_perm_hlpr(pmu, letters, newPrefix, n, k - 1)

def create_rep_mat(words, hot_vec_dict, r_size):
    mat_len = len(words) - r_size + 1
    mat = [[] for i in range(0, mat_len)]
    i = 0
    while i < mat_len:
        j = i
        while j < i + r_size:
            mat[i].append(hot_vec_dict[words[j]])
            j += 1
        i += 1
    return mat

def get_rep_mat(seq, hot_vec_dict, k=3, r_size=2):
    words = word_seq(seq, k)
    rep_mat = create_rep_mat(words, hot_vec_dict, r_size)
    return rep_mat

def get_rep_mats(seqs):
    rep_mats = []
    hot_vec_dict = create_dict('ACGT')
    for seq in seqs:
        rep_mat = get_rep_mat(seq, hot_vec_dict, k=3, r_size=1)
        rep_mats.append(rep_mat)
    return rep_mats

def conv_labels(labels, dataset='splice'):
    converted = []
    for label in labels:
        if label == 'EI':
            converted.append(0)
        elif label == 'IE':
            converted.append(1)
        elif label == 'N':
            converted.append(2)
    return converted

if __name__ == "__main__":
    seq = 'ACCGATTATGCA'
    words = word_seq(seq, 3)
    hot_vec_dict = create_dict('ACGT')
    rep_mat = create_rep_mat(words, hot_vec_dict, 2)


    