from django.conf import settings
import os
import sys
import pandas as pd
import numpy as np
np.set_printoptions(threshold=sys.maxsize)
from sklearn.multioutput import MultiOutputClassifier
from sklearn.tree import DecisionTreeClassifier

class Recommender():
    clf = ""
    classLabels = "Teknoloji-1 Teknoloji-2 Teknoloji-3 Gıda İnşaat Danışmanlık Giyim Online-Alışveriş Medya Banka-Sigorta Mobilya-Ev Eğitim Yemek Sanayi Otomobil Holding Market İçecek Kariyer-Planlama Kitap-Kırtasiye Kar-Amacı-Gütmeyen-Kuruluşlar Seyahat-Tatil Temizlik-Bakım Eskişehir-Yerel Düzce-Yerel Samsun-Yerel Osmaniye-Yerel Antalya-Yerel İstanbul-Yerel Ankara-Yerel Bursa-Yerel"
    def __init__(self, **kwargs):
        super(Recommender, self).__init__(**kwargs)
        file_path = os.path.join(settings.FILES_DIR, 'data_encoded.csv')
        X_train = pd.read_csv(file_path)
        file_path = os.path.join(settings.FILES_DIR, 'y.csv')
        y_train = pd.read_csv(file_path)
        self.classLabels = self.classLabels.split(" ")
        self.clf = MultiOutputClassifier(DecisionTreeClassifier()).fit(X_train, y_train)

    def recommend(self,X):
        preds = self.clf.predict([X])
        recommends = [item for item,pred in zip(self.classLabels,preds[0]) if pred == 1]
        return recommends