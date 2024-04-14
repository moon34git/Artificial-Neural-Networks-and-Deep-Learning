import tarfile
import os
import torch
from torch.utils.data import Dataset
from torchvision import transforms
from PIL import Image

class MNIST(Dataset):

    def __init__(self, data_dir):
        self.data_dir = data_dir
        root, _ = os.path.splitext(data_dir)
        tar = tarfile.open(data_dir, 'r')
        data_dir = os.path.dirname(data_dir)
        tar.extractall(data_dir)
        self.files = [os.path.join(root, f) for f in os.listdir(root) if f.endswith('.png')]
        self.transform = transforms.Compose([
            transforms.ToTensor(),  
            transforms.Normalize((0.1307,), (0.3081,))  
        ])

    def __len__(self):
        return len(self.files)

    def __getitem__(self, idx):
        file_path = self.files[idx]
        img = Image.open(file_path).convert('L') 
        img = self.transform(img)
        label = int(file_path.split('_')[-1].split('.')[0]) 
        return img, label

if __name__ == '__main__':
    train_dataset = MNIST('../data/train.tar')
    test_dataset = MNIST('../data/test.tar')
    print('-'*20, 'train_dataset', '-'*20)
    print(len(train_dataset))
    print(train_dataset[0][0].shape)
    print(train_dataset[0][1])

    print('-'*20, 'Test_dataset', '-'*20)
    print(len(test_dataset))
    print(test_dataset[0][0].shape)
    print(test_dataset[0][1])