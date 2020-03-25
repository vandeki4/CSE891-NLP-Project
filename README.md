# CSE891 NLP Project

## Prerequisites

```
tensorflow>=2.0
spacy>=2.2.3
nltk
```

## Downloading the Dataset

See the [dataset/](dataset) folder for download scripts.


## Results: Average BLEU-4 Scores
_From 0.0 to 1.0, higher is better._
|             |  Baseline      |  Transformer  |   |   |
|-------------|----------------|---------------|---|---|
| Training    | ```0.1514```   |      0.346    |   |   |
| Validation  | ```0.0405```   |   ```0.273```  |   |   |
| Updated     | 3/13/2020      | 3/24/2020     |   |   |

```Transformer Training Accuracy: 0.3```

### Discussion
The Transformer model achieves not only superior performance, but also trains in a fraction of the time compared to the baseline RNN model.

## About 
Machine Translation is used to convert text from one language into another. Modern methods for solving this problem often use recurrent and/or convolutional neural networks to handle the sequential sentence structure. Recent advances have shown that attention mechanisms to handle sentence structure are sufficient to match or exceed the performance of recurrent and convolutional methods. Most MT methods use a form of beam search for efficient inference.

Sequence modeling problems, including machine translation, involve generating a sequence of hidden states from an input text in one language to another series of hidden states andoutput text in another language. In this work, we will explore attention-based English to Spanish translation and vice-versa in a supervised setting on a parallel corpus of English and Spanish translations for European Parliamentary proceedings.

The initial baseline has a classic gated recurrent unit structure. The sentences for training and testing are preprocessed and tokenized by word and punctuation with special start and end tokens padding the sequence. Each language has an indexable vocabulary, or dictionary, of known words that are represented with a high-dimensional vector, and the indices for the tokens are also stored sequentially.

### Baseline Model
We used the baseline model described in this [official Tensorflow tutorial](https://www.tensorflow.org/tutorials/text/nmt_with_attention).

We had a lot of issues with the dataset size; the tutorial uses a much smaller translation dataset, especially in vocabulary size and sentence length.
When we modified the tutorial code to use the Europarl dataset, it used a large amount of memory and crashed. It turns out that this was primarily due to the sentence length;
after we limited the sentences to only those with 80 tokens or less, this was less of an issue. 

The accuracy still isn't amazing, but this might just be a challenging dataset. We definitely could have trained longer too, but the whole process is fairly slow. 

That said, the entire pipeline for preprocessing, training, and evaluation is all in place, so it should be fairly straightforward to iterate on the model.

### Transformer Model
Our transformer model is based on the attention-based neural network described in [*Attention is All You Need*]([https://arxiv.org/pdf/1706.03762.pdf]) and implemented following this [TensorFlow tutorial]([https://www.tensorflow.org/tutorials/text/transformer]). This model is able to achieve better results than recurrent or convolutional networks, and due to its architecture, it is more parallelizable and able to train in a fraction of the time.

We used a similar pipeline for preprocessing the Europarl dataset as before with the baseline; however, this model further extends the preprocessing steps to include subwords, which helps to mitigate the challenge of unknown/out of vocabulary words. 

---
Since the Transformer is not based on an RNN or CNN, the relative position of tokens in the sentence must also be embedded. The positional encoding follows this formula:
*PE<sub>(pos,2i)</sub> = sin(pos/10000<sup>2i/d<sub>model</sub></sup>)*
*PE<sub>(pos,2i+1)</sub> = cos(pos/10000<sup>2i/d<sub>model</sub></sup>)*

---
A look ahead masking scheme is used to prevent the model from "cheating" by looking at future tokens. To predict the *k<sup>th* word, only those from *1* to *k-1* can be used.

---
The Transformer uses multi-head attention with 8 heads. This has four parts: 
+ Dense linear layers split across the 8 heads
+ 8 scaled dot product attention modules
+ Concatenation 
+ Final linear layer

The input to the multi-head attention is a query, key, and value.

The scaled dot product attention also takes these three inputs. 
The attention weights are calculated by:
*softmax<sub>k</sub>(**QK<sup>T</sup>**/sqrt(d<sub>k</sub>)) **V*** 

---
The encoder layers consist of 2 sublayers, each with residual connections and layer normalization:
1. Multi-head attention
2. Point-wise feed forward network (2 fully-connected layers with ReLU activation)

The encoder consists of the input embedding that is summed with the position encoding which is followed by 4 of the encoder layers described above. The output of this encoder is fed to the decoder.

---
The decoder layers consist of 3 sublayers, each with residual connections and layer normalization:
1. Multi-head attention with look ahead masks
2. Multi-head attention with the value and key from the output of the encoder and the query from the output of the masked multi-head attention sublayer.
3. Point-wise feed forward network (2 fully-connected layers with ReLU activation)

The decoder consists of the input embedding, positional encoding, and 4 decoder layers. Basically, the output from the encoder is used to calculate the importance of the decoder input to predict the next word.

---
The Transformer consists of an encoder, the decoder, and a final dense layer.

---
During training, we use dropout to prevent over-fitting, Adam for optimization, a batch size of 64, and train over 20 epochs. The training objective is cross-entropy loss minimization.

Argmax is used during testing time, and each predicted word is appended to the previously predicted ones; however, using beam search for inference is a modification that could lead to better results. 