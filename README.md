# Amazon-review-sentiment-analysis

**Data** : https://www.kaggle.com/bittlingmayer/amazonreviews (400K text reviews)

**Preprocessing**: TFIDF-Vectorizer

**Selected Models**: Decision Tree, Logistic Regression, Neural Network(10 * 10), Random Forest, Ensemble(hard voting: LR+NN+RF)

## Evaluate the result

**Performance:**

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
