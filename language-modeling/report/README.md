# Loss Graph
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


# different samples generated from different seed characters with different T
## T = 0.1 
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

## T = 1
## Vanilla RNN Generated Samples:

### Seed: I

Generated:
I am our bear blood
Sorrow
And worth.
Thou scarcely can rest be her; but I shautenant. 

DUCHESS OF Y

### Seed: love

Generated:
love
And thus remafest;
While stood to:
This, our appetited
In Richard I have there!
The ghost:
That

### Seed: should

Generated:
should we may of manner,
Sem!

MARCIUS:
Go evided
As the fearful for myself.

BUCKINGHAM:
Stier'd
mi

### Seed: the

Generated:
the man and swearing that I will not yet.

MENENIUS:
I'll take do thy day, it. Prown out of the comm

### Seed: happy

Generated:
happy of put in mine
Mass'd,
And tulgle house of hands and revenge
Of my rage; but their Lastant aft

## LSTM Generated Samples:

### Seed: I

Generated:
INCE EDWARD:
God keep me from the place,
And that his grace, on sin to come upon a day, Hastings, le

### Seed: love

Generated:
loves you well:
So shouldst down, standing to answer.

AUFIDIUS:
Even so
As well for our fath Axdian

### Seed: should

Generated:
should consul!

Chidd till on perpetual bound to him and make the Roman lies blenefier.

Lords:
You

### Seed: the

Generated:
ther of Rome. You are to know.' 'His nurse
I'ld say 'This ill from him.

CLARENCE:
Bid you my good a

### Seed: happy

Generated:
happy days!

PRINCE EDWARD:
If I could Hastings, good friends, most cannot live, but mine ears, pres

## T = 2
## Vanilla RNN Generated Samples:

### Seed: I

Generated:
IZAuchend!
'I inforive?
I hires' I am: Enshic-pe?

AUFIDIUS:
Not
Abisain; and stretching; spuiltecus

## Seed: love

Generated:
love York: a trich, safle pove to gettroup but thin!
I am Rome;'
Wigsolved.
So, willy! Goome rather?

### Seed: should

Generated:
should reldmins'?

VOLUMARCIUS:
Thich.

KINGE:
Dig?
For my live: arm sew several gidome toounn being

### Seed: the

Generated:
they
Slet come.
If in Comean ed'st doihts;
But
thee eniffecce-dards: he't,
Oufictoling.' Bid? as Itt

### Seed: happy

Generated:
happy is!
Ty Mo Ladse, desbar; serve
Madam toe.

DUCHEDWARD IV: you hads by lidier!
This Awazknentn'

## LSTM Generated Samples:

### Seed: I

Generated:
Is, cry's fair bling capakerly: curst well store of knave
The which was not Caiss it is:
Calment, lo

### Seed: love

Generated:
love him moght that he will measure. Undee, his atsewly.

MARCIUS:
Withal, but icceal Cleasing nay.

### Seed: should

Generated:
shouldwnoon,
How accompostuct difit.

SICINIUS:
O do you serve, ind capaft toy:
The night me out of

### Seed: the

Generated:
theirs, is ilnoth always,--
As much umoun:
Thou hasb on my praise me little earled
In yours is rashn

### Seed: happy

Generated:
happy brokehile out.

SICINIUS:
Than a whey have no weech.
Ine:
Droy! it is your voices!

MENENIUS:

# Analysis for selecting temperature value

The temperature value of the text generation process controls the randomness of the predictions.
If the temperature is low, we try to select the next character with the highest probability. On the other hand, if the temperature is high, there is a high possibility of selecting the next character with a low probability. This means that generally, the cooler the temperature, the more consistent and logical the text will remain.

In this case, lower temperatures seem to provide better performance.

