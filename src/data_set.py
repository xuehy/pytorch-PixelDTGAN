import six.moves.cPickle as Pickle
import torch as th
import cv2
import numpy as np


def loadImage(path):
    inImage_ = cv2.imread(path)
    inImage = cv2.cvtColor(inImage_, cv2.COLOR_RGB2BGR)
    info = np.iinfo(inImage.dtype)
    inImage = inImage.astype(np.float) / info.max

    iw = inImage.shape[1]
    ih = inImage.shape[0]
    if iw < ih:
        inImage = cv2.resize(inImage, (64, int(64 * ih/iw)))
    else:
        inImage = cv2.resize(inImage, (int(64 * iw / ih), 64))
    inImage = inImage[0:64, 0:64]
    return th.from_numpy(2 * inImage - 1).transpose(0, 2).transpose(
        1, 2
    )


class LookbookDataset():
    def __init__(self, data_dir, index_dir):
        self.data_dir = data_dir
        with open(index_dir+'cloth_table.pkl', 'rb') as cloth:
            self.cloth_table = Pickle.load(cloth)
        with open(index_dir+'model_table.pkl', 'rb') as model:
            self.model_table = Pickle.load(model)

        self.cn = len(self.cloth_table)
        self.path = data_dir

    def getbatch(self, batchsize):
        batch1 = []
        batch2 = []
        batch3 = []
        for i in range(batchsize):
            seed = th.randint(1, 100000, (1,)).item()
            th.manual_seed((i+1)*seed)
            r1 = th.randint(0, self.cn, (1,)).item()
            r2 = th.randint(0, self.cn, (1,)).item()
            r1 = int(r1)
            r2 = int(r2)
            mn = len(self.model_table[r1])
            r3 = th.randint(0, mn, (1,)).item()
            r3 = int(r3)

            path1 = self.cloth_table[r1]
            path2 = self.cloth_table[r2]
            path3 = self.model_table[r1][r3]
            img1 = loadImage(self.path + path1)
            img2 = loadImage(self.path + path2)
            img3 = loadImage(self.path + path3)
            batch1.append(img1)
            batch2.append(img2)
            batch3.append(img3)
        return th.stack(batch1), th.stack(batch2), th.stack(batch3)
