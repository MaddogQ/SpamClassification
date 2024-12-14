# SpamClassification

A comparative analysis of spam classification

# Quickstart

Install the packages:

`pip install -r requirements.txt`

Or if you're using conda, run

`conda install --yes --file requirements.txt`

# Dataset

[Ott Dataset](https://www.kaggle.com/datasets/rtatman/deceptive-opinion-spam-corpus): 1,600 reviews split evenly between "deceptive" and "truthful"

Augmented Ott Dataset: 3,200 reviews split evenly between "deceptive" and "truthful", with 1,600 using **back translation** and the other 1,600 using **synonym replacement**

# Improvements & Changes

- Split dataset into training, development, and testing sets
- Added learning rate scheduling
- Added class weights
- Added ReduceLROnPlateau
- Added confusion matrix and classification report
- Fixed checkpoint
- Changed early stopping patience from 10 to 5
- Changed custom `Attention` class implementation to use Keras' built-in `AdditiveAttention` layer

# Results

| Model                      | Num Shots | Dataset   | Train Accuracy | Val Accuracy | Test Accuracy | Precision | Recall | F1 Score |
| -------------------------- | --------- | --------- | -------------- | ------------ | ------------- | --------- | ------ | -------- |
| BiLSTM-attention-glove100D | N/A       | original  | 1.000          | 0.8500       | 0.8167        | 0.82      | 0.82   | 0.82     |
| BiLSTM-attention-glove100D | N/A       | augmented | 1.0            | 0.9561       | 0.9434        | 0.94      | 0.94   | 0.94     |
| LSTM-Conv1D-glove100D      | N/A       | original  | 0.9848         | 0.5250       | 0.8625        | 0.86      | 0.86   | 0.86     |
| LSTM-Conv1D-glove100D      | N/A       | augmented | 0.9438         | 0.5229       | 0.8938        | 0.90      | 0.89   | 0.89     |
| CNN-glove100D              | N/A       | original  | 0.9804         | 0.8333       | 0.8333        | 0.83      | 0.83   | 0.83     |
| CNN-glove100D              | N/A       | augmented | 0.9978         | 0.9396       | 0.9396        | 0.94      | 0.94   | 0.94     |
| 2-layer-LSTM-glove100D     | N/A       | original  | 0.9982         | 0.8625       | 0.8625        | 0.86      | 0.86   | 0.86     |
| 2-layer-LSTM-glove100D     | N/A       | augmented | 0.9978         | 0.9396       | 0.9417        | 0.94      | 0.94   | 0.94     |
| LLM-GPT4o-mini             | 0         | original  | 0.82           | 0.82         | 0.8167        | 0.82      | 0.82   | 0.82     |
| LLM-GPT4o-mini             | 1         | original  | 0.82           | 0.82         | 0.8167        | 0.82      | 0.82   | 0.82     |
| LLM-GPT4o-mini             | 2         | original  | 0.82           | 0.82         | 0.8167        | 0.82      | 0.82   | 0.82     |
| LLM-GPT4o-mini             | 3         | original  | 0.82           | 0.82         | 0.8167        | 0.82      | 0.82   | 0.82     |

Achieved overall **10%** improvement in test accuracy with augmentation.

# Error Analysis

#TO-DO

# Reference

[Detection of Fake Reviews on Online Review Platforms using Deep Learning Architectures
](https://github.com/ashishsalunkhe/DeepSpamReview-Detection-of-Fake-Reviews-on-Online-Review-Platforms-using-DeepLearning-Architectures)

Salunkhe, Ashish. "Attention-based Bidirectional LSTM for Deceptive Opinion Spam Classification." arXiv preprint arXiv:2112.14789 (2021).
