# CSE891 NLP Project

## Prerequisites:

```
tensorflow>=2.0
spacy>=2.2.3
nltk
```

## Downloading the Dataset

See the [dataset/](dataset) folder for download scripts.

## Baseline Model
We used the baseline model described in this [official Tensorflow tutorial](https://www.tensorflow.org/tutorials/text/nmt_with_attention).
We had a lot of issues with the dataset size; the tutorial uses a much smaller translation dataset, especially in vocabulary size.
When we modified the tutorial code to use the Europarl dataset, it used a large amount of memory. We had to cut down on the model complexity
to make it runnable on our local machine, so it didn't perform very well. That said, the entire pipeline for preprocessing, training, and evaluation
is all in place, so it should be fairly straightforward to iterate on the model.

### Average BLEU Score (Baseline as of 3/12/2020):
_From 0.0 to 1.0, higher is better._

```0.00825 (training)```

```0.00759 (validation)```

## About ##
Machine Translation is used to convert text from one language into another. Modern methods for solving this problem often use recurrent and/or convolutional neural networks to handle the sequential sentence structure. Recent advances have shown that attention mechanisms to handle sentence structure are sufficient to match or exceed the performance of recurrent and convolutional methods. Most MT methods use a form of beam search for efficient inference.

Sequence modeling problems, including machine translation, involve generating a sequence of hidden states from an input text in one language to another series of hidden states andoutput text in another language. In this work, we will explore attention-based English to Spanish translation and vice-versa in a supervised setting on a parallel corpus of English and Spanish translations for European Parliamentary proceedings.

The initial baseline has a classic gated recurrent unit structure. The sentences for training and testing are preprocessed and tokenized by word and punctuation with special start and end tokens padding the sequence. Each language has an indexable vocabulary, or dictionary, of known words that are represented with a high-dimensional vector, and the indices for the tokens are also stored sequentially.
