import torch
import torch.nn as nn
from torch.utils.data import DataLoader, SubsetRandomSampler
import numpy as np
from dataset import Shakespeare
from model import CharRNN, CharLSTM
from tqdm import tqdm

def train(model, trn_loader, device, criterion, optimizer, clip=1):
    model.train()
    epoch_loss = 0
    for inputs, targets in tqdm(trn_loader):
        inputs, targets = inputs.to(device), targets.to(device)
        hidden = model.init_hidden(inputs.size(0), device)
        optimizer.zero_grad()
        
        outputs, hidden = model(inputs, hidden)
        loss = criterion(outputs.view(-1, outputs.size(-1)), targets.view(-1))
        loss.backward()
        nn.utils.clip_grad_norm_(model.parameters(), clip)
        optimizer.step()
        
        epoch_loss += loss.item()
        
    return epoch_loss / len(trn_loader)

def validate(model, val_loader, device, criterion):
    model.eval()
    epoch_loss = 0
    with torch.no_grad():
        for inputs, targets in val_loader:
            inputs, targets = inputs.to(device), targets.to(device)
            hidden = model.init_hidden(inputs.size(0), device)
            outputs, hidden = model(inputs, hidden)
            loss = criterion(outputs.view(-1, outputs.size(-1)), targets.view(-1))
            epoch_loss += loss.item()
            
    return epoch_loss / len(val_loader)

def split_dataset(dataset, validation_split=0.2, shuffle=True, random_seed=42):
    dataset_size = len(dataset)
    indices = list(range(dataset_size))
    split = int(np.floor(validation_split * dataset_size))
    if shuffle:
        np.random.seed(random_seed)
        np.random.shuffle(indices)
    train_indices, val_indices = indices[split:], indices[:split]
    return train_indices, val_indices

def main(batch_size=128, num_epochs=100, learning_rate=0.001):
    dataset = Shakespeare('../data/shakespeare_train.txt')
    
    train_indices, val_indices = split_dataset(dataset)
    
    train_sampler = SubsetRandomSampler(train_indices)
    val_sampler = SubsetRandomSampler(val_indices)
    trn_loader = DataLoader(dataset, batch_size=batch_size, sampler=train_sampler)
    val_loader = DataLoader(dataset, batch_size=batch_size, sampler=val_sampler)

    input_size = len(dataset.chars)
    hidden_size = 256
    output_size = input_size

    rnn = CharRNN(input_size, hidden_size, output_size).to(device)
    lstm = CharLSTM(input_size, hidden_size, output_size).to(device)

    criterion = nn.CrossEntropyLoss()
    rnn_optimizer = torch.optim.Adam(rnn.parameters(), lr=learning_rate)
    lstm_optimizer = torch.optim.Adam(lstm.parameters(), lr=learning_rate)

    best_rnn_val_loss = float('inf')
    best_lstm_val_loss = float('inf')
    best_rnn_model = None
    best_lstm_model = None

    rnn_train_losses, rnn_val_losses = [], []
    lstm_train_losses, lstm_val_losses = [], []
    for epoch in range(num_epochs):
        rnn_train_loss = train(rnn, trn_loader, device, criterion, rnn_optimizer)
        lstm_train_loss = train(lstm, trn_loader, device, criterion, lstm_optimizer)
        
        rnn_val_loss = validate(rnn, val_loader, device, criterion)
        lstm_val_loss = validate(lstm, val_loader, device, criterion)
        
        rnn_train_losses.append(rnn_train_loss)
        rnn_val_losses.append(rnn_val_loss)
        lstm_train_losses.append(lstm_train_loss)
        lstm_val_losses.append(lstm_val_loss)
        
        print('-'*30, f'Epoch {epoch+1}', '-'*30)
        print(f'RNN: Train Loss {rnn_train_loss:.4f}, Val Loss {rnn_val_loss:.4f}')
        print(f'LSTM: Train Loss {lstm_train_loss:.4f}, Val Loss {lstm_val_loss:.4f}')

        if rnn_val_loss < best_rnn_val_loss:
            best_rnn_val_loss = rnn_val_loss
            best_rnn_model = rnn.state_dict()
        
        if lstm_val_loss < best_lstm_val_loss:
            best_lstm_val_loss = lstm_val_loss
            best_lstm_model = lstm.state_dict()

    np.save('../report/rnn_train_losses.npy', rnn_train_losses)
    np.save('../report/rnn_val_losses.npy', rnn_val_losses)
    np.save('../report/lstm_train_losses.npy', lstm_train_losses)
    np.save('../report/lstm_val_losses.npy', lstm_val_losses)

    torch.save(best_rnn_model, '../models/best_rnn_model.pth')
    torch.save(best_lstm_model, '../models/best_lstm_model.pth')

if __name__ == '__main__':
    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
    main()
