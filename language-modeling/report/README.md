### Loss Graph
![losses](losses.png)

1. Handling Long-Term Dependencies
LSTM: LSTMs are designed to capture long-term dependencies in sequences. They use a gating mechanism (input gate, forget gate, and output gate) to control the flow of information and maintain long-term memory. This allows LSTMs to remember important information over long periods and forget irrelevant information, leading to more effective learning, especially for sequences with long-term dependencies.

RNN: Vanilla RNNs struggle with long-term dependencies due to the vanishing gradient problem. When training with backpropagation through time (BPTT), gradients can diminish exponentially, making it difficult for RNNs to learn dependencies that span many time steps.

2. Gradient Flow
LSTM: The architecture of LSTMs includes mechanisms to preserve gradients over long sequences. The cell state and gated architecture help in maintaining a more stable gradient flow during training, which mitigates the vanishing gradient problem.

RNN: In contrast, RNNs without any gating mechanisms are more prone to the vanishing gradient problem, leading to ineffective learning over long sequences. This results in higher training and validation losses as the model fails to learn long-term dependencies effectively.

3. Flexibility and Complexity
LSTM: LSTMs have more parameters and a more complex architecture compared to vanilla RNNs. This complexity allows LSTMs to model more nuanced relationships in the data. The added flexibility comes from the additional gates and cell state, which enhance the model's capacity to learn from complex sequential data.

RNN: Vanilla RNNs have a simpler architecture with fewer parameters. While this simplicity can be advantageous in terms of computational efficiency, it limits the model's ability to capture complex patterns in the data, especially when dealing with long sequences.


### different samples generated from different seed characters with different T
## Vanilla RNN Generated Samples:

### Seed: I

Generated:
I see her beauty in the supple the corn of my son, my lord, like and so do I mean to see him soul, t

### Seed: love

Generated:
love to Rome, and the common men the senate, who three, the senate, what I will not stay have see hi

### Seed: should

Generated:
should be so die the consul, and the common for me to my lord, your country's prove a proud as the s

### Seed: the

Generated:
the common for than the senate, which the senate, what I will not sleeping, and the common men the s

### Seed: happy

Generated:
happy in the suppliant me to the people,
Because the consul, when he shall be so much many my son, m

## LSTM Generated Samples:

### Seed: I

Generated:
I have done't?

CORIOLANUS:
What must I say?
'I Pray, sir'--Plague upon't! I cannot bring
My tongue

## Seed: love

Generated:
love him: lend you you say, my lord, your son, the melancholy face to stake on you this?

VOLUMNIA:

## Seed: should

Generated:
should be my name is Marcius.

MENENIUS:
What is become of Marcius 'O if he
Had borne the bastards d

## Seed: the

Generated:
the city and
Be every man himself?

SICINIUS:
Peace!

MENENIUS:
What is about to be? I am out of bre

## Seed: happy

Generated:
happy day set to stay him, overboard,
Into the gods!

CORIOLANUS:
Ay, but not mine own desire.

Thir
