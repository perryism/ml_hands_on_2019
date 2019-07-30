from toolz import curry

@curry
def is_rotten(rotten_words, quote):
    lower_quote = quote.lower()
    for rotten_word in rotten_words:
        if rotten_word.lower() in lower_quote:
            return 1

    return 0

def predict(df, rotten_words):
    rotten = is_rotten(rotten_words)
    return df.apply(rotten)

import pylab as plt
import numpy as np

def plot_confusion_matrix(cm, title='Confusion matrix', cmap=plt.cm.Blues):
    plt.imshow(cm, interpolation='nearest', cmap=cmap)
    plt.title(title)
    plt.colorbar()
    types = ['positive', 'negative']
    tick_marks = np.arange(len(types))
    plt.xticks(tick_marks, types, rotation=45)
    plt.yticks(tick_marks, types)
    plt.tight_layout()
    plt.ylabel('True label')
    plt.xlabel('Predicted label')

import pickle
class Sentiment:
    @staticmethod
    def save_demo(vec, clf):
        with open('data/vectorizer.pkl', 'wb') as f:
            f.write(pickle.dumps(vec))

        with open('data/logreg.pkl', 'wb') as f:
            f.write(pickle.dumps(clf))


    @staticmethod
    def demo():
        return Sentiment.load('data/vectorizer.pkl', 'data/logreg.pkl')

    @staticmethod
    def load(vec_path, clf_path):
        vec = None
        clf = None

        with open(vec_path, 'rb') as f:
            vec = pickle.loads(f.read())

        with open(clf_path, 'rb') as f:
            clf = pickle.loads(f.read())

        return Sentiment(vec, clf)

    def __init__(self, vectorizer, clf):
        self.vectorizer = vectorizer
        self.clf = clf

    def predict(self, text):
        X = self.vectorizer.transform([text])
        return self.clf.predict(X)[0]



