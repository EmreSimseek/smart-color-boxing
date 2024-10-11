# Smart Color Boxing

Renk ve Kontur Tespiti, OpenCV kullanarak belirli renkleri gerçek zamanlı video akışında tespit eden bir Python projesidir. Bu proje, etkileşimli bir şekilde farklı renkler seçmenize olanak tanır ve seçilen renge uyan nesnelerin etrafında sınır çizgileri (bounding box) çizer.

Gerçek Zamanlı Tespit: Canlı kamera akışındaki belirli renkteki nesneleri gerçek zamanlı olarak tespit eder.
Etkileşimli Renk Seçimi: Klavye üzerinden kırmızı, yeşil, mavi, sarı, camgöbeği, eflatun, turuncu, mor gibi renkler arasında kolayca geçiş yapabilirsiniz.
Nesne Boyutuna Göre Filtreleme: Küçük nesneleri tespit etmemek için minimum kontur alanını ayarlayabilir, böylece yalnızca büyük nesneler işaretlenir.
Basit Kullanıcı Arayüzü: Algılanan nesneler üzerinde çizilen sınır kutuları ile görsel geri bildirim sunar.


Kameranızın canlı video akışını gösteren bir pencere açılacaktır.

Bir Renk Seçin: Aşağıdaki tuşları kullanarak tespit etmek istediğiniz rengi seçebilirsiniz:

1: Kırmızı
2: Yeşil
3: Mavi
4: Sarı
5: Camgöbeği
6: Eflatun
7: Turuncu
8: Mor
Bir renk seçtikten sonra program, videodaki bu renkteki nesneleri tespit eder ve etraflarında sınır kutuları çizer.

Programdan Çıkış: Programdan çıkmak için q tuşuna basmanız yeterlidir.
