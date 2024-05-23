import torch
from torch.utils.data import Dataset

class Shakespeare(Dataset):
    def __init__(self, input_file):
        with open(input_file, 'r') as f:
            text = f.read()

        self.chars = sorted(list(set(text)))

        self.char_to_idx = {char: idx for idx, char in enumerate(self.chars)}
        self.idx_to_char = {idx: char for idx, char in enumerate(self.chars)}

        text_indices = [self.char_to_idx[char] for char in text]
        self.seq_len = 30

        self.data = []
        self.targets = []
        for i in range(len(text_indices) - self.seq_len):
            self.data.append(torch.tensor(text_indices[i:i + self.seq_len], dtype=torch.long))
            self.targets.append(torch.tensor(text_indices[i + 1:i + self.seq_len + 1], dtype=torch.long))

    def __len__(self):
        return len(self.data)

    def __getitem__(self, idx):
        input = self.data[idx]
        target = self.targets[idx]
        return input, target

if __name__ == '__main__':
    dataset = Shakespeare('../data/shakespeare_train.txt')
    print(len(dataset))
    print(dataset.char_to_idx)
    print(dataset.idx_to_char)
