# hack-tools

Proje Açıklaması: Kali Linux üzerinde yaygın olarak kullanılan araçların bir arada toplandığı ve daha hızlı işlem için yazılmış hack aracı.

---

## Kullanım Kılavuzu

Bu projeyi kullanmak için aşağıdaki adımları takip edebilirsiniz.

1. **Gereksinimlerin Kurulumu:** Kullanılan araçlar Kali Linux işletim sisteminde hazır olarak gelen araçlardır. Bazı araçların çalışması için ek gereksinimler olabilir. Örneğin, `pyfiglet` modülünü kurmak için:
`pip3 install pyfiglet`

2. **Root Yetkisi:** Bazı araçlar için root yetkisi gerektirebilir. Root yetkisi almak için terminalde bu komutu kullanabilirsiniz: `sudo su`


---

### Dahil Olan Araçlar

Bu proje, Kali Linux ile birlikte gelen ve kullanıma hazır olan bazı araçları içermektedir. Ayrıca, ek olarak kurulum gerektirmeyen araçları da içerebilir.

1. **MacChanger:** MacChanger, Linux tabanlı işletim sistemlerinde MAC (Media Access Control) adresini değiştirmenizi sağlayan bir araçtır. MAC adresi, ağ cihazlarını tanımlamak için kullanılır.

2. **Dmitry:** Dmitry, hedef bir sunucu veya ağ hakkında bilgi toplamak için kullanılan bir istihbarat toplama aracıdır. IP adresleri, açık portlar, servisler ve daha fazlası gibi bilgileri toplayabilir.

3. **TheHarvester:** TheHarvester, açık kaynaklı bir bilgi toplama aracıdır. Hedefe yönelik e-posta adresleri, alt alanlar, açık portlar ve daha fazla bilgi toplamak için kullanılır.

4. **NetDiscover:** NetDiscover, aynı ağdaki cihazları keşfetmek için kullanılan bir ağ keşif aracıdır. Ağdaki IP adreslerini ve MAC adreslerini bulabilir.

5. **Wafwoof:** Wafwoof, web uygulama güvenlik duvarı (WAF) dedektörüdür. Bir web sitesinin hangi WAF'ı kullandığını tespit etmek için kullanılır.

6. **Nmap:** Nmap, ağdaki açık portları ve hedef sistem hakkında detaylı bilgi sağlayan güçlü bir açık kaynaklı ağ tarama aracıdır.

7. **Searchsploit:** Searchsploit, Exploit Veritabanı'nda bulunan güvenlik açıklarını aramak ve bunlara yönelik exploit kodlarını bulmak için kullanılır.

8. **Nikto:** Nikto, web sunucularının güvenlik zafiyetlerini taramak için kullanılan açık kaynaklı bir web tarayıcıdır. Potansiyel güvenlik açıklarını tespit edebilir.

9. **Exiftool:** Exiftool, dijital fotoğraf ve görüntü dosyalarının içinde bulunan EXIF (Exchangeable Image File Format) bilgilerini okumak ve düzenlemek için kullanılan bir araçtır.

10. **WPScan:** WPScan, WordPress tabanlı web sitelerinin güvenlik açıklarını taramak ve sızma testleri yapmak için kullanılan bir araçtır.

11. **Crunch:** Crunch, özelleştirilebilir parola listeleri oluşturmanızı sağlayan bir araçtır. Parola kuvvet saldırıları için kullanılabilir.

---

### Katkıda Bulunma

Bu projeye katkıda bulunmak isterseniz, lütfen forklayın ve geliştirmelerinizi yapın. Ardından bir pull isteği gönderin. Projeye katkıda bulunmak için aşağıdaki yolları düşünebilirsiniz:

- Yeni araçlar eklemek
- Mevcut araçları güncellemek
- Hata düzeltmeleri yapmak

Her türlü katkıya açığım.

---