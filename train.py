with open ('input.txt', 'r', encoding = 'utf-8') as f:
    text = f.read()
chars = sorted(list(set(text)))
vocab = len(chars)
print(''.join(chars))
print(vocab)
#create char to integer map
stoi = { ch:i for i, ch in enumerate(chars)}
itos = { i:ch for i, ch in enumerate(chars)}
encode = lambda s: [stoi[c] for c in s] #takes string outputs integers
decode = lambda l: ''.join([itos[i] for i in l]) #takes integeres outputs string
print(encode('hello my name is charan'))
print(decode(encode('hello my name is charan')))

import torch
data = torch.tensor(encode(text), dtype = torch.long)
print(data.shape, data.dtype)
print(data[:1000])