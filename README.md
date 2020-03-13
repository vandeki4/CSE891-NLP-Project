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

