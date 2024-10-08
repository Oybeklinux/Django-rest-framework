﻿# Mavzu 1: API va REST API
 
## Reja:
- [1 Terminlar](#1-terminlar)
- [2 Nazariya](#2-nazariya)


## 1 Terminlar
```
API - application programming interface. API - bu ikki kompyuterni yoki ikki ilovani bog'lab turuvchi dasturdir. API boshqa ilovalarga hizmat ko'rsatuvchi dastur interfeysidir. Oddiy qilib aytganda u **habar yetkazuvchidir**
REST - Agar API REST arxitekurasi (qoidasi) bo'yicha tuzilgan bo'lsa, u holda u REST API deyiladi.
status code - serverdan qaytgan Response holatini bildiruvchi kodlar
CRUD - Creat (yangi tuzish) Read (o'qish) Update (o'zgartirish) Delete (o'chirish). http method turlariga qo'llaniladi
JSON - JavaScript Object Notation. REST API shu formatda ishlatiladi.
Host name - URLda o'zgarmaydigan qismi 
Endpoint - URLdagi o'zgaradigan qismi
```

## 2 Nazariya
**Reja**
- [2.1 API](#21-api)
  - [2.1.1 API nima?](#211-api-nima)
  - [2.1.2 API foydalari](#212-api-foydalari)
  - [2.1.3 API turlari](#213-api-turlari)
  - [2.1.4 API protokollari](#214-api-protokollari)
  - [2.1.5 API hujjati](#215-api-hujjati)
- [2.2 REST API](#22-rest-api)
  - [2.2.1 Terminlar](#221-terminlar)
  - [2.2.2 Misollar](#222-misollar)

### 2.1 API
#### 2.1.1 API nima?
[Manba](https://dev.to/ayushi7rawat/what-is-an-api-api-for-beginners-4mfh)
<p>API - bu ikki kompyuterni yoki ikki ilovani bog'lab turuvchi dasturdir. API boshqa ilovalarga hizmat ko'rsatuvchi dastur interfeysidir. Oddiy qilib aytganda u **habar yetkazuvchidir**
</p><p>
Keling tushunib olish oson bo'lishi uchun bitta real bo'lmagan misol ko'ramiz
</p><p>
Aytaylik, siz restoranga tashrif buyurdingiz, xizmatkor sizga menyuni taqdim etdi. Nima yeyishni o'zingiz hal bilasiz. Bu pitsa, makaron yoki kartoshka bo'lishi mumkin. Xizmatkor buyurtmangizni oshpazga olib boradi. Ovqatingiz tayyor bo'lgach, u yana sizga yetkazib beradi.
</p>

![](images/img.png)

<p>
Bu juda oddiy jarayon. Ovqat qanday tayyorlanishi yoki oshxona ichida sodir bo'ladigan boshqa narsalar haqida tashvishlanishingiz shart emas. Bu yerda xizmatkor API vazifasini bajaradi. U siz va oshxona o'rtasidagi aloqani o'rnatadigan vositadir.
</p><p>
API nimaligini haqida tasavvurga ega bo'ldik deb umid qilaman. Endi esa real misolni ko'ramiz
</p><p>
Deylik birorta ilovada ro'yxatdan o'tishingiz kerak, odatda ko'p ilovalarda Facebook yoki Google orqali ro'yxatdan o'tish imkoniyati bo'ladi. 
</p><p>
Bu qanday ishlashini hech o'ylab ko'rganmisiz?
</p>

![](images/img_1.png)

<p>
Facebook va Google allaqachon sizning ma'lumotlaringizga ega, shuning uchun har bir foydalanuvchining ma'lumotlarini qaytadan yozish kabi zerikarli vazifani bajarish o'rniga, ilova API orqali ularning ma'lumotlar bazasiga kirib, kerakli ma'lumotlarni olib, ro'yxatdan o'tkazib qo'yadi.
</p>

![](images/img_2.png)

<p>
Yana bir mashhur misol - ob-havo ilovasi. Agar siz uni dasturini yozmoqchi bo'lsangiz, siz jismonan borib, butun dunyo bo'ylab ma'lumotlarni yozib ololmaysiz. Buning o'rniga ob-havo ma'lumotlarini olish uchun tegishli API-dan foydalanishingiz mumkin.
</p>

![](images/img_3.png)

<p>
Xo'sh, bu o'g'irlik uchun eshiklarni ochadi. Shuning uchun API kalitlaridan foydalanadi. API kaliti identifikatsiya va avtorizatsiya uchun ishlatiladi, bu foydalanuvchilarni kuzatib borish uchun ishlatiladigan xavfsizlik kodidan boshqa narsa emas. Aytish joizki, har bir APIda ham kalit mavjud emas.
</p>

![](images/img_4.png)

<p>
Bundan tashqari, kompaniyalar odatda tashqi ilovalardan o'z xizmatlari va mahsulotlariga kirishni ta'minlash uchun ulardan foydalanadilar.
</p><p>
Ular ko'pincha mobil ilovalarni ishlab chiqishda ishlatiladi, lekin ular ikki xil veb-saytlarni ulash yoki uchinchi tomon dasturlari bilan integratsiya qilish uchun ham ishlatilishi mumkin.
</p>

![](images/img_5.png)


#### 2.1.2 API foydalari

- Ko'rinish va tirbandlikni oshirish
- Uzluksiz integratsiya
- Samaradorlikni oshirish
- Osonroq texnik xizmat ko'rsatish
- Kamaytirilgan xarajatlar
- Murakkablikni yashiradi

![](images/img_6.png)

- Request - so'rov bo'lib, mijozdan serverga yuboriladi. (Masalan "mahsulotlar ro'yxati" ni ko'rish uchun so'rov)
- Response - javob bo'lib, serverdan mijozga so'rovga javob sifatida yuboriladi. (Masalan "mahsulotlar ro'yxati" so'roviga tegishli ma'lumotlarni qaytarish)
<br>
API qaysi qurilmalar tomonidan ishlatiladi?

- Android
- iOS
- Browser
- Desktop

#### 2.1.3 API turlari

[Manba](https://www.erp-information.com/application-programming-interface.html)
<br><br>
**Maqsadiga ko'ra turlari:**

- **Ma'lumot API**. Bunday APIlar ma'lumotlar bazalari yoki veb-xizmatlar kabi turli manbalardan ma'lumotlarga kirish imkonini beradi. Ular ko'pincha ma'lumot olish yoki hisob-kitoblarni amalga oshirish uchun ishlatiladi.
- **Funksional API**. Masalan, ular yordamida hisobingizni boshqarishingiz yoki onlayn mahsulotlarni xarid qilishingiz mumkin.
- **Qayta ishlovchi API**. Masalan, faylni bir formatdan boshqasiga o'zgartirish yoki ziplab saqlash uchun siqib qo'yishlar misol bo'ladi.

<br>

**Ishlatilishiga ko'ra turlari:**

- **Ochiq**. Ular minimal cheklovlar bilan foydalanuvchilar uchun mavjud. Foydalanuvchilar HTTP protokoli orqali ularga kirishlari mumkin.
- **Hamkorlik**. Ular texnik jihatdan ochiq API bilan bir xil, lekin cheklangan kirishga ega
- **Yopiq**. Ular tashqi foydalanuvchilardan yashiringan. Ulardan kompaniya ichida foydalanish mumkin.

#### 2.1.4 API protokollari

- **HTML**. HTML veb-sahifaga asoslangan. Foydalanish oson, lekin imkoniyati cheklangan
- **XML**. HTMLga qaraganda imoniyati ko'p, ammo undan foydalanish murakkabroq bo'lishi mumkin.
- **JSON**. XML-ga nisbatan yengil bo'lib, uni o'qish va yozish oson. U RESTful API-larda  mashhur, chunki u tez va samarali.

#### 2.1.5 API hujjati

API hujjati bu APIdan qanday foydalanish haqidagi ma'lumotdir. 
<br>
<br>
Hujjatdan quyidagi savollarga javob berish mumkin:
- qanday API lar mavjud?
- qanday metod ishlatiladi (get,post,put,...)
- qanday ma'lumotlar mijoz tarafidan yuborish kerak
- qanday ma'lumotlar serverdan qaytib keladi
- nechta ma'lumot keladi
- ma'lumotlar qanday nom bilan keladi

![](images/img_7.png)
### 2.2 REST API
#### 2.2.1 Terminlar

REST - Representational state transfer.
<br>
Agar API REST arxitekurasi (qoidasi) bo'yicha tuzilgan bo'lsa, u holda u REST API deyiladi.

<br>
Terminlar bilan tanishamiz:

- endpoint 
- method (CRUD)
- Headers (status code)
- ma'lumot (JSON)

##### Endpoint va host name
![](images/img_8.png)

<br>Host name - URLda o'zgarmaydigan qismi 
<br>Endpoint - URLdagi o'zgaradigan qismi
<br>


![](images/img_11.png)


1-URL hamma ma'lumotlar uchun:
 - method GET bo'lsa, hamma kinolarni qaytaradi
 - method POST bo'lsa, yangi kino kiritadi
<br>

2-URL individual ma'lumot uchun:
 - method GET bo'lsa, id=127 bo'lgan kino haqida to'liq ma'lumotni qaytaradi
 - method PUT bo'lsa, id=127 bo'lgan kinoga tegishli ko'rsatilgan ma'lumotini o'zgartiradi
 - method DELETE bo'lsa, id=127 bo'lgan kinoni o'chiradi

##### [Serializer](https://www.django-rest-framework.org/tutorial/1-serialization/):

![](images/41.png)

Serialize - Murakkab obyektni JSON formatiga mos bo'lgan dict toifasiga o'girib berish
<br>

![](images/42.png)

Turlari:

- Serialize - Python dagi obyektni json formatiga moslab beradi. Bu jarayon so'rov jo'natganda (Request) ishlatiladi <br>
- Deserialize - Json formatni Python obyektiga o'girish. Bu jarayon so'rovga javob kelgan (Response) ishlatiladi
<br>


![](images/43.png)
<br>
Serializer turlari:

- serializers.Serializer
- serializers.ModelSerializer

##### [View](https://www.django-rest-framework.org/api-guide/views/)

Turlari:
- Class based
- Function based

API bilan ishlavchi dasturlar

- DRF Browser API
- Postman
- HTTPie

##### Method (CRUD)

![](images/img_9.png)
<p>
CRUD termini ko'p ishlatiladi. CRUD shunchaki boshqacha nomlanishi. Creat (yangi tuzish) Read (o'qish) Update (o'zgartirish) Delete (o'chirish) so'zlarining qisqartmasidir.
</p>
![](images/img_10.png)

##### Headers (Status code)
Umumiylashtirilgan ko'rinishi:
<br>
![](images/img_12.png)

<br>
To'liqroq:

![](images/img_13.png)

##### Ma'lumot (JSON)

![](images/img_14.png)

#### REST API

<div class="markdown prose w-full break-words dark:prose-invert light"><p>REST (Representational State Transfer) — bu web-servislar va API-lar uchun ishlatiladigan arxitektura uslubi. Bu uslub server va mijoz o'rtasidagi samarali, stateless (holatsiz) aloqani ta'minlaydi. Quyida REST API uchun asosiy qoida va tamoyillar keltirilgan:</p><h3>1. <strong>Mijoz-Server Arxitekturasi</strong></h3><ul><li><strong>Vazifalarni ajratish</strong>: Mijoz va server bir-biridan mustaqil rivojlana oladi.</li><li>Mijoz foydalanuvchi interfeysi (UI) bilan shug'ullanadi, server esa ma'lumotlar saqlash va biznes logikasini boshqaradi.</li></ul><h3>2. <strong>Stateless (holatsizlik)</strong></h3><ul><li>Har bir so'rov serverga to'liq kerakli ma'lumotni o'z ichiga olishi kerak.</li><li>Server mijozning holatini saqlamaydi, bu esa har bir so'rov mustaqil bo'lishini ta'minlaydi.</li><li>Mijoz tomonida sessiya holati saqlanadi.</li></ul><h3>3. <strong>Bir xil interfeys</strong></h3><ul><li>Resurslar bilan ishlashda bir xil, yaxlit interfeys qo'llaniladi. Bunga quyidagilar kiradi:<ul><li><strong>Resurslarni aniqlash</strong>: Har bir resurs yagona URI orqali aniqlanishi kerak.</li><li><strong>Resurslarni taqdimot orqali boshqarish</strong>: Mijozlar resurslarga bevosita emas, ularning taqdimoti orqali (masalan, JSON yoki XML formatida) ishlaydi.</li><li><strong>O'z-o'zini tushuntiruvchi xabarlar</strong>: Har bir xabar o'zida barcha kerakli ma'lumotlarni saqlashi kerak.</li><li><strong>HATEOAS</strong>: Mijoz resurs holatiga qarab kelgusidagi amallarni aniqlay olishi kerak.</li></ul></li></ul><h3>4. <strong>Stateless metodlar (HTTP Verblar)</strong></h3><ul><li>RESTful API HTTP metodlari orqali resurslar bilan ishlaydi:<ul><li><strong>GET</strong>: Resursni olish (o'qish).</li><li><strong>POST</strong>: Yangi resurs yaratish (yozish).</li><li><strong>PUT</strong>: Resursni yangilash (yangilash).</li><li><strong>PATCH</strong>: Resursni qisman yangilash.</li><li><strong>DELETE</strong>: Resursni o'chirish.</li></ul></li></ul><h3>5. <strong>Resurslarga asoslangan URI'lar</strong></h3><ul><li>Resurslar URI orqali taqdim etilishi kerak, bu harakatlar emas, resurslarni tasvirlaydi. Noun (ot)lar ishlatilib resurslar aniqlanadi, verb (fe’l) emas.</li><li>Misol:<ul><li><strong>To'g'ri</strong>: <code>/api/books/123</code> (123 ID ga ega kitob resursi).</li><li><strong>Noto'g'ri</strong>: <code>/api/getBook?id=123</code> (Harakatga asoslangan).</li></ul></li></ul><h3>6. <strong>Qatlamli tizim</strong></h3><ul><li>Tizim bir nechta qatlamlardan tashkil topgan bo'lishi kerak, har bir qatlam alohida vazifani bajaradi, masalan xavfsizlik, keshlash yoki yuk balanslash.</li><li>Har bir qatlam faqat o'ziga yaqin bo'lgan qatlam bilan o'zaro aloqada bo'ladi.</li></ul><h3>7. <strong>Keshlanuvchanlik</strong></h3><ul><li>Server javoblari keshlanishi yoki keshlanmasligi kerakligini aniqlab beradi.</li><li>Keshlash mexanizmlari tizimni tezlashtiradi va serverga tushadigan yukni kamaytiradi.</li></ul><h3>8. <strong>Talab bo'yicha kod (ixtiyoriy)</strong></h3><ul><li>Server mijozga kod (masalan, JavaScript) yuborishi va uni mijoz tomoni ishlatishi mumkin.</li><li>Bu talab majburiy emas, lekin qo'shimcha funksionallikni oshirishda foydali bo'lishi mumkin.</li></ul><h3>9. <strong>Versiyalash</strong></h3><ul><li>REST API-lar versiyalashni qo'llab-quvvatlashi kerak, bu esa API rivojlanayotganda orqaga moslikni ta'minlaydi.</li><li>Misol: <code>/api/v1/books/</code> yoki headersda <code>Accept-Version: v1</code> kabi versiya ko'rsatiladi.</li></ul><h3>10. <strong>Xatolarni boshqarish</strong></h3><ul><li>Mijoz va server o'rtasidagi so'rovlar HTTP status kodlari orqali boshqariladi:<ul><li><strong>200 OK</strong>: So'rov muvaffaqiyatli bajarildi.</li><li><strong>201 Created</strong>: Yangi resurs yaratildi.</li><li><strong>400 Bad Request</strong>: Yaroqsiz so'rov.</li><li><strong>401 Unauthorized</strong>: Mijoz autentifikatsiyadan o'tmadi.</li><li><strong>404 Not Found</strong>: Resurs topilmadi.</li><li><strong>500 Internal Server Error</strong>: Serverda xatolik yuz berdi.</li></ul></li></ul><h3>11. <strong>Hujjatlashtirish va izchillik</strong></h3><ul><li>REST API-lar yaxshi hujjatlashtirilgan bo'lishi kerak, bu foydalanuvchilarga API dan foydalanishni osonlashtiradi.</li><li>API nomlash konvensiyalari izchil bo'lishi kerak, masalan, snake_case yoki camelCase.</li></ul><h3>REST API bilan ishlash misoli:</h3><ul><li><strong>GET</strong> <code>/api/books/</code>: Barcha kitoblarni ro'yxatini qaytaradi.</li><li><strong>POST</strong> <code>/api/books/</code>: Yangi kitob yaratadi.</li><li><strong>GET</strong> <code>/api/books/123</code>: 123 ID ga ega kitobni qaytaradi.</li><li><strong>PUT</strong> <code>/api/books/123</code>: 123 ID ga ega kitobni yangilaydi.</li><li><strong>DELETE</strong> <code>/api/books/123</code>: 123 ID ga ega kitobni o'chiradi.</li></ul><h3>Xulosa:</h3><p>REST API-lar kengayuvchan, texnik xizmat ko'rsatish oson va ishlatish qulay bo'lishi uchun ushbu tamoyillarga amal qilishlari kerak. Resurslar tuzilishi aniq, metodlari aniqlangan, versiyalash va xatolarni boshqarish aniq bo'lishi lozim.</p></div>

#### 2.2.2 Misollar

Mahsulotlar ro'yxati uchun:

- https://www.api.movielist.com/movies/
- https://www.api.movielist.com/movies/list/

Individual mahsulot uchun

- https://www.api.movielist.com/movies/102/
- https://www.api.movielist.com/movies/102/reviews/
- https://www.api.movielist.com/movies/102/reviews/?limit=20
 
Kirish va ro'yxatdan o'tish uchun 

- https://www.api.movielist.com/movies/account/login/
- https://www.api.movielist.com/movies/account/register/
