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
We had a lot of issues with the dataset size; the tutorial uses a much smaller translation dataset, especially in vocabulary size and sentence length.
When we modified the tutorial code to use the Europarl dataset, it used a large amount of memory and crashed. It turns out that this was primarily due to the sentence length;
after we limited the sentences to only those with 80 tokens or less, this was less of an issue. The accuracy still isn't amazing, but this might just be
a challenging dataset. We definitely could have trained longer too, but the whole process is fairly slow. 
That said, the entire pipeline for preprocessing, training, and evaluation is all in place, so it should be fairly straightforward to iterate on the model.

### Average BLEU Score (Baseline as of 3/13/2020):
_From 0.0 to 1.0, higher is better._

```0.1514 (training)```

```0.0405 (validation)```

