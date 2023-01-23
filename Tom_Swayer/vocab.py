def value_sort_dict(dict1):
    import numpy as np

    keys = list(dict1.keys())
    values = list(dict1.values())
    sorted_value_index = np.argsort(values)
    sorted_dict = {keys[i]: values[i] for i in sorted_value_index}
    return sorted_dict

def build_vocab(words):
    vocab = dict.fromkeys(list(set(words)),None)
    for word in vocab.keys():
        vocab[word]=words.count(word)
    #vocab=value_sort_dict(vocab)
    return vocab