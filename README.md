# Starbucks Ürünleri Besin Değeri Analizi ve Sınıflandırma 
Bu proje, Starbucks menüsündeki çeşitli yiyecek ve içeceklerin besin değerlerini (kalori, yağ, protein, karbonhidrat, lif) detaylı bir şekilde incelemek ve görselleştirmek amacıyla oluşturulmuştur. Ayrıca, bir ürünün besin değerlerine bakarak hangi kategoriye (type) ait olduğunu tahmin eden bir makine öğrenmesi modeli geliştirilmiştir.

## Veri Kaynağı ve Araçlar
**Veri Seti:** Analizde kullanılan veri seti, Kaggle'dan elde edilen starbucks.csv dosyasıdır.

**Kullanılan Kütüphaneler:** Pandas, NumPy, Matplotlib, Seaborn, Scikit-learn (sklearn).

## Analizler ve Görselleştirmeler
Proje kapsamında çeşitli analizler ve görselleştirmeler yapılmıştır. Öne çıkan bulgular aşağıdadır:

**1. Ürün Türleri Dağılımı**
<p>En fazla ürün çeşidine sahip kategorinin "Bakery" olduğu görülmüştür.
<div style="display: flex; gap: 10px;">
  <img src="assets/urun_sayilari.png" alt="Ürün Sayıları" width="350"/>
  <img src="assets/urun_turleri.png" alt="Ürün Türleri" width="330"/>
</div>
**2. Kalori ve Protein Değerleri**
<p>Ortalama kalori değeri en yüksek ürün kategorileri "Bakery" ve "Sandwiches" olarak belirlenmiştir.

<p>Protein değeri açısından "Sandwiches" ve hemen ardından "Bistro box" kategorileri diğer kategorilere kıyasla daha zengindir.
<p>En fazla ürün çeşidine sahip kategorinin "Bakery" olduğu görülmüştür.
<div style="display: flex; gap: 10px;">
  <img src="assets/kalori_dagilimi.png" alt=Kalori Dağılımları" width="350"/>
  <img src="assets/karbonkidrat.png" alt="Karbonhidrat Dağılımı" width="340"/>
</div>

## 3. Korelasyon Analizi
<p>Sayısal değişkenler arasındaki korelasyonlar incelenmiştir. 
<div>
  <img src="assets/korelasyon.png" alt=Isı Haritası" width="350"/>
</div>
## Makine Öğrenmesi Modeli
**Amaç:** 
Bir ürünün kalori, yağ, karbonhidrat, lif ve protein değerlerine bakarak hangi type (kategori) olduğunu tahmin eden bir makine öğrenmesi modeli geliştirilmiştir.

**Model Tipi:** 
Karar Ağacı Sınıflandırıcısı (DecisionTreeClassifier) kullanılmıştır.

**Model Başarısı:** 
Model, test verileri üzerinde %75'lik bir doğruluk oranı (accuracy) elde etmiştir.

## Modelin Görselleştirilmesi
Aşağıda, eğitilmiş olan Karar Ağacı modelinin görsel bir temsilini bulabilirsiniz. Bu görsel, modelin hangi özelliklere (calories, fat, carb, fiber, protein) göre nasıl kararlar verdiğini ve ürünleri farklı kategorilere ayırdığını net bir şekilde göstermektedir.
<img src="assets/karar_agaci.png" alt="Karar Ağacı" width="500"/>

