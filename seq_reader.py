from ohv import get_rep_mats, conv_labels

def load_data(fname):
    seqs = []
    labels = []
    f = open(fname)
    for line in f:
        sp = line.replace(" ","")
        nw = sp.replace("\n","")
        line_arr = nw.split(",")
        label = line_arr[0]
        str= line_arr[2]
        str= str.upper()  
        str= str.replace("\t","")      
        str= str.replace("N","A")  
        str= str.replace("D","G")
        str= str.replace("S","C")
        str= str.replace("R","G")
        labels.append(label)
        seqs.append(str)
    f.close()
    return seqs, labels

if __name__ == "__main__":
    seqs, labels = load_data("E:/3/Package/ML/cnn/data.txt")
    lb = conv_labels(labels)
    st = get_rep_mats(seqs)    
    print (len(lb))
    print (len(st))
