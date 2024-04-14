import torch
import torch.nn.functional as F
from torch.utils.data import DataLoader
from dataset import MNIST
from model import LeNet5, LeNet5_v2, CustomMLP
from tqdm import tqdm
import numpy as np

def train(model, train_loader, device, criterion, optimizer):
    model.train()  
    
    trn_loss = 0
    correct = 0
    total = 0

    for _, (inputs, targets) in enumerate(train_loader):
        inputs, targets = inputs.to(device), targets.to(device)
        optimizer.zero_grad()
        outputs = model(inputs)
        loss = criterion(outputs, targets)
        loss.backward()
        optimizer.step()

        trn_loss += loss.item()
        _, predicted = outputs.max(1)
        total += targets.size(0)
        correct += predicted.eq(targets).sum().item()

    trn_loss /= len(train_loader)
    acc = 100. * correct / total
    return trn_loss, acc

def test(model, test_loader, device, criterion):
    model.eval()  

    tst_loss = 0
    correct = 0
    total = 0

    with torch.no_grad():
        for _, (inputs, targets) in enumerate(test_loader):
            inputs, targets = inputs.to(device), targets.to(device)
            outputs = model(inputs)
            loss = criterion(outputs, targets)

            tst_loss += loss.item()
            _, predicted = outputs.max(1)
            total += targets.size(0)
            correct += predicted.eq(targets).sum().item()

    tst_loss /= len(test_loader)
    acc = 100. * correct / total
    return tst_loss, acc

def main():
    batch_size = 64
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

    train_dataset = MNIST('../data/train.tar')
    test_dataset = MNIST('../data/test.tar')

    train_loader = DataLoader(train_dataset, batch_size=batch_size, shuffle=True)
    test_loader = DataLoader(test_dataset, batch_size=batch_size, shuffle=False)

    # model = LeNet5().to(device)
    model = LeNet5_v2().to(device)
    # model = CustomMLP().to(device)


    optimizer = torch.optim.SGD(model.parameters(), lr=0.01, momentum=0.9)
    criterion = torch.nn.CrossEntropyLoss()

    train_loss_hist, test_loss_hist = [], []
    train_acc_hist, test_acc_hist = [], []

    for epoch in range(10):
        trn_loss, trn_acc = train(model, train_loader, device, criterion, optimizer)
        tst_loss, tst_acc = test(model, test_loader, device, criterion)

        train_loss_hist.append(trn_loss)
        test_loss_hist.append(tst_loss)
        train_acc_hist.append(trn_acc)
        test_acc_hist.append(tst_acc)

        print(f'Epoch: {epoch+1}, Train Loss: {trn_loss:.4f}, Train Acc: {trn_acc:.2f}%, Test Loss: {tst_loss:.4f}, Test Acc: {tst_acc:.2f}%')
    
    ## Save the results (LeNet5)
    # np.save('../report/results/lenet5/train_loss_hist.npy', train_loss_hist)
    # np.save('../report/results/lenet5/test_loss_hist.npy', test_loss_hist)
    # np.save('../report/results/lenet5/train_acc_hist.npy', train_acc_hist)
    # np.save('../report/results/lenet5/test_acc_hist.npy', test_acc_hist)
    
    # # Save the results (CustomMLP)
    # np.save('../report/results/custommlp/train_loss_hist.npy', train_loss_hist)
    # np.save('../report/results/custommlp/test_loss_hist.npy', test_loss_hist)
    # np.save('../report/results/custommlp/train_acc_hist.npy', train_acc_hist)
    # np.save('../report/results/custommlp/test_acc_hist.npy', test_acc_hist)
        
    # Save the results (LeNet5_v2)
    np.save('../report/results/lenet5_v2/train_loss_hist.npy', train_loss_hist)
    np.save('../report/results/lenet5_v2/test_loss_hist.npy', test_loss_hist)
    np.save('../report/results/lenet5_v2/train_acc_hist.npy', train_acc_hist)
    np.save('../report/results/lenet5_v2/test_acc_hist.npy', test_acc_hist)

if __name__ == '__main__':
    main()