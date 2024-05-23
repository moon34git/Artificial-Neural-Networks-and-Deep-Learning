import torch
from model import CharRNN, CharLSTM
from dataset import Shakespeare

def generate(model, seed_characters, temperature, device, char_to_idx, idx_to_char, length=100):
    model.eval()
    input_seq = torch.tensor([char_to_idx[char] for char in seed_characters], dtype=torch.long).unsqueeze(0).to(device)
    hidden = model.init_hidden(1, device)
    generated = seed_characters

    epsilon = 1e-8

    for _ in range(length - len(seed_characters)):
        output, hidden = model(input_seq, hidden)
        output = output[:, -1, :]
        output = output.view(-1)
        scaled_logits = output / temperature
        softmax_probs = torch.softmax(scaled_logits, dim=0) + epsilon
        softmax_probs /= torch.sum(softmax_probs)

        top_char_idx = torch.multinomial(softmax_probs, 1).item()
        
        generated_char = idx_to_char[top_char_idx]
        generated += generated_char
        input_seq = torch.tensor([char_to_idx[generated_char]], dtype=torch.long).unsqueeze(0).to(device)

    return generated

if __name__ == '__main__':
    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

    dataset = Shakespeare('../data/shakespeare_train.txt')

    model_rnn = CharRNN(len(dataset.char_to_idx), 256, len(dataset.char_to_idx)).to(device)
    model_rnn.load_state_dict(torch.load('../models/best_rnn_model.pth'))
    
    model_lstm = CharLSTM(len(dataset.char_to_idx), 256, len(dataset.char_to_idx)).to(device)
    model_lstm.load_state_dict(torch.load('../models/best_lstm_model.pth'))

    seed_characters_list = ['I','love','should','the','happy']
    temperature = 0.9
    length = 100

    print("Vanilla RNN Generated Samples:")
    for seed in seed_characters_list:
        print('-'*30)
        generated_text = generate(model_rnn, seed, temperature, device, dataset.char_to_idx, dataset.idx_to_char, length)
        print(f'Seed: {seed}\n\nGenerated:\n {generated_text}')

    print("LSTM Generated Samples:")
    for seed in seed_characters_list:
        print('-'*30)
        generated_text = generate(model_lstm, seed, temperature, device, dataset.char_to_idx, dataset.idx_to_char, length)
        print(f'Seed: {seed}\n\nGenerated:\n {generated_text}')
