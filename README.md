# Amazon-review-sentiment-analysis

**Data** : https://www.kaggle.com/bittlingmayer/amazonreviews (400K text reviews)

**Preprocessing**: TFIDF-Vectorizer

**Selected Models**: Decision Tree, Logistic Regression, Neural Network(10 * 10), Random Forest, Ensemble(hard voting: LR+NN+RF)

## Evaluate the result

**Performance:**

**Decision Tree:**

training accuracy: 93.4%  testing accuracy: 76.2%

precision: 75.6%  recall: 77.0%  f1: 76.3%

**Logistic Regression:**

training accuracy: 93.2%  testing accuracy: 90.1%

precision: 91.8%  recall: 88.1%  f1: 89.9%

**Neural Network:**

training accuracy: 92.0%  testing accuracy: 90.4%

precision: 90.3%  recall: 90.5%  f1: 90.4%

**Random Forest:**

training accuracy: 99.4%  testing accuracy: 78.5%

precision: 83.1%  recall: 71.4%  f1: 76.8%

**Ensemble:**

training accuracy: 95.8%  testing accuracy: 90.4%

precision: 91.3%  recall: 89.3%  f1: 90.3%


<img src="https://github.com/bill9800/Amazon-review-sentiment-analysis/raw/master/Performance.png" width="600">

**Training time:**

<img src="https://github.com/bill9800/Amazon-review-sentiment-analysis/raw/master/training_time.png" width="600">

**ROC:**

<img src="https://github.com/bill9800/Amazon-review-sentiment-analysis/raw/master/ROC.png" width="600">

## Word counting vs. TF-IDF

<img src="https://github.com/bill9800/Amazon-review-sentiment-analysis/raw/master/count_vs_tfidf.png" width="600">

<img src="https://github.com/bill9800/Amazon-review-sentiment-analysis/raw/master/count_vs_tfidf_imp.png" width="600">

## Summary

1. High frequency words are not necessarily important

2. Tree base model is likely to overfitting

3. For sentiment analysis, logistic regression is a good model to try first. (fast and high accuracy)

4. Good feature transformation can have a better prediction. (Tfidf > wordCount)

5. Further improvement? Maybe try Sequence model
