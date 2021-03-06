import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.svm import SVC
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
from matplotlib import pyplot as plt

rs=30
df = pd.read_csv("D:\Triyana\hepatitis\hepatitis01.csv")
print(df.shape)

features = ['AGE','SEX','STEROID','ANTIVIRALS','FATIGUE','MALAISE','ANOREXIA','LIVER_BIG','LIVER_FIRM','SPLEEN_PALPABLE','SPIDERS','ASCITES','VARICES','BILIRUBIN','ALK_PHOSPHATE','SGOT','ALBUMIN','PROTIME','HISTOLOGY']
# Separating out the features
X = np.array(df.drop(['Class'],1))
# Separating out the target
y = np.array(df['Class'])

# Standardizing the features - standar scaling
scaler = StandardScaler()
X = scaler.fit_transform(X)

pca = PCA(n_components=10, random_state=None) #We will set it none so that we can see the variance explained and then choose no of component.

X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.2, random_state=rs)

X_train = pca.fit_transform(X_train)
X_test = pca.transform(X_test)

clf = SVC(C=1.0,  gamma='auto', random_state=rs)
clf.fit(X_train,y_train)
y_pred = clf.predict(X_test)
cm = confusion_matrix(y_test,y_pred)
print(cm)
print(classification_report(y_test,y_pred))
skor = accuracy_score(y_test, y_pred)
print('akurasi:', skor)

explained_variance = pca.explained_variance_ratio_
print ('explained variances:', explained_variance*100)
per_var = np.round(pca.explained_variance_ratio_ * 100, decimals=1)
labels = ['PC' + str(x) for x in range(1, len(per_var) + 1)]
plt.bar(x=range(1, len(per_var)+1), height=per_var,
tick_label=labels)
plt.ylabel('percentange of explained variance')
plt.xlabel('principal component')
plt.title('scree plot')
plt.show()
