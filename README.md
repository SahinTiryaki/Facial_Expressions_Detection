# Facial Expressions Detection 

Bu çalışma insan yüz görüntülerinden hangi duyguya sahip olduklarının  (sinirli-şaşkın-mutlu vb.) tespiti  ve bu işlemlerin bir web arayüzünde çalıştırılmasını içermektedir. 
## Veri seti
Veri setinde  angry, disgust, fear, happy, neutral, sad ve suprise olmak üzere  7 adet sınıf içermektedir. Veri seti hali hazırda  train-valid-test olmak üzere 3 parça olarak yer almaktadır.
Görselde train, validation ve test parçalarında buluann sınıfların sayısal dağılımları gösterilmiştir. Neutral sınıfından sonra tüm parçalarda happy sınıfının baskın olduğu gözlemlenmiştir. **Aynı zamanda verilerin sadece sayısal olarak fazla olması model geliştirmek için iyi düşünceler oluşturmaktadır (ki sadece verilerin sayısı önemli değil)**. 
![classDistrubitaion](https://user-images.githubusercontent.com/59391291/166070538-86aa5e87-7b33-4d57-9559-e3c1db6ae67f.png)
Train veri setinde 92968 adet, validation setinde 17356 ve test veri setinde de 17356 adet görüntü yer almaktadır. 

#### Veri setinden birkaç görüntü

![faces](https://user-images.githubusercontent.com/59391291/166071305-1e4e25c7-9d25-4bf4-99f3-d744dec8818c.png)

## Yöntem
<ul>
  
  <li> Yüz bölgesini model olarak BlazeFace (https://arxiv.org/abs/1907.05047) modelini kullanan  MediaPipe kütüphanesi ile tespit et (https://google.github.io/mediapipe/) </li>
  <li> Yüz var mı? Birden fazla yüz var mı ? kontrol et. Varsa direkt olarak birden fazla yüz veya  hiç yüz yoktur mesajı döndür. Tekrar başa dön </li>    
  <li> BGR-RGB dönüşümü ve boyutu 150x150 boyutuna getir  </li>
  <li> Yakalanan yüz bölgesini veri seti kullanarak eğitilen VGG19 modeli ile sınıflandır. </li>
  <li> Sonuçlanan görüntüyü arayüze aktar </li>
  </ul>
  
  Arayüz olarak kullanımının uygun ve hızla geliştirilebilmesi nedeniyle streamlit (https://streamlit.io/) kullanılmıtır. Kameraya erişebilmek içinse opencv kullanıştır. Gelen her görüntü web arayüzünde sonuçlarıyla beraber gösterilecektir.

### Demo

<div align="center">
<img src="media/webInterface.gif" width="80%"/> 
</div>
<br>

**Demo görüntüsünden de anlaşılacağı üzere veri setinin etiketlenmesinden kaynaklanan duygu karıştırması gerçekleşmektedir.  Bir model geliştirilirken başarısı sadece modelin iyi bir mimariye sahip olması veya veri sayısnın sayıca fazla olmasından dolayı değildir. Asıl önemli olan verilerin ve etiketlenmesinin olabildiğince kaliteli olmasıdır.  Bu çalışmadan sadece  veri sayısnın fazla olması değil kaliteli etiketlenmiş veri olması sonucuna ulaşılmıştır..**

**Aynı zamanda 3 kanallı bir görüntü yerine  tek kanallı bir girdi alan model kurulmasıyla daha doğru sonuç alınabilir. Fakat bu veri setinde bulunan tartışmalı olabilecek görüntülerin yapıyı bozacağı açıktır.**

