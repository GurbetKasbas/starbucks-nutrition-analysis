#####################################################
#      Starbucks Ürünleri Besin Değeri Analizi
#####################################################

# Gerekli kütüphanelerin import edilmesi
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_style("darkgrid")

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
# DataFrame'i oluşturma
df = pd.read_csv("starbucks/starbucks.csv",index_col=0)


df.head()

df.info()

df.describe().T

# Kaç farklı ürün çeşidi var
df["item"].nunique()

# Bu uniq değerler nelerdir?
df["item"].unique()

df["type"].nunique()

df["type"].unique()

# type değişkenine göre gruplandır ve her gruptan kaçar tane olduğunu say
df.groupby("type")["item"].count()

# Yukarıda yaptığımız işlemi grafik üzerinde görelim
df.groupby("type")["item"].count().plot()
plt.title("Ürün Türleri")
plt.text(0.,47,"Ürün Kategori Yelpazesi",bbox=dict(facecolor="yellow"),alpha=0.5)
plt.xlabel("Ürün Tipleri")
plt.ylabel("Adet Sayısı")
plt.show()


# Sütun grafiğini olşturalım
sns.countplot(x="type",data=df,palette="Set1")
plt.title("Ürün Sayıları")
plt.show()


# Type sutununa gore içerdiği kalori miktarını  veren grafik
sns.catplot(kind="bar",x="type",y="calories",data=df , palette="Set2")
plt.title("Ürünlerin Kalori Değerleri",pad=0)
plt.show()


# Protein değerlerini grafik üzerinde gösterelim

sns.catplot(kind="bar" , x="type",y="protein",data=df,palette="Set3")
plt.title("Ürünlerin Protein Değerleri" ,pad=0)
plt.show()

# Karbonhidrat değerlerini grafik üzerinde gösterelim

sns.catplot(kind="bar",x="type",y="carb" , data=df,color="r")
plt.title("Karbonhidrat Değerleri",pad=0)
plt.show()

# Sayısal Değerlerin Korelasyonuna Bakalım

# Korelesyon için Veri tipi float ve int olanları seçiyoruz
num_cols = [col for col in df.columns if df[col].dtype in ["int","float"]]

# Korelasyon bilgisi
corr=df[num_cols].corr()

# Isı Haritası
sns.heatmap(corr ,annot=True)
plt.show()



# Kalori ve yağ için bir saçılım grafiği oluşturalım

plt.title("Kalori ve Yağ" , pad=3)
sns.scatterplot(x="calories", y="fat", data=df,s=100 ,edgecolor="red",color="yellow") # s argümanı dairelerin boyut bilgisini alır
plt.show()


# yiyecek ve içeceklerin kalori dağılımı
sns.displot(x="calories",data=df,color="red",kde=True)
plt.title("Kalori Grafiği",pad=0)
plt.show()


# yiyecek ve içeceklerin protein dağılımı
sns.displot(x="protein",data=df,color="green",kde=True)
plt.title("Protein Grafiği",pad=0)
plt.show()

# Yiyecek ve içeceklerin yağ grafiği
sns.displot(x="fat",data=df,kde=True,color="purple")
plt.title("Yağ Grafiği",pad=0)
plt.show()



# Bir ürünün hangi type'a sahip olduğunu tahmin etmeye çalışalım


df.columns
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

# x bağımsız değişkeni :  giriş verilerini tutar
x=df[[ 'calories', 'fat', 'carb', 'fiber', 'protein']]

# hedef değişken :Tahmin edilecek 
y=df["type"]

# x_train ve y_train: modelin eğitilmesi içşin kullanılan veriler

x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.1,random_state=28)
model= DecisionTreeClassifier()
# modeli eğitme işi
model.fit(x_train,y_train)


# test verileri uzerindeki tahmınleri bir değişkene atadık
y_pred = model.predict(x_test)

# tahminleri gerçek veriyle karşılaştırma
accuracy=accuracy_score(y_test,y_pred)

print("Doğruluk: " , accuracy)

# Tahmın
prediction = model.predict([[250,2,40,7,9]])
print(prediction)


prediction = model.predict([[450,2,45,7,29]])
print(prediction)


import matplotlib.pyplot as plt
from sklearn.tree import plot_tree
plt.figure(figsize=(15,10))
plot_tree(model,feature_names=x.columns,class_names=model.classes_,filled=True)
plt.show()

