import six.moves.cPickle as Pickle
import os


dataset_dir = '../data/lookbook/data/'
models = []
clothes = []

for filename in os.listdir(dataset_dir):
    if filename.endswith('.jpg'):
        if filename.split('_')[1].endswith('0'):
            models.append(filename)
        else:
            clothes.append(filename)

print(len(models))
print(len(clothes))

i = 0
match = []
while i < len(clothes):
    pid = clothes[i][3:9]
    match_i = []
    j = 0
    while j < len(models):
        if models[j][3:9] == pid:
            match_i.append(models[j])
        j += 1
    match.append(match_i)
    i += 1

with open('cloth_table.pkl', 'wb') as cloth_table:
    Pickle.dump(clothes, cloth_table)
with open('model_table.pkl', 'wb') as model_table:
    Pickle.dump(match, model_table)

print('done')
