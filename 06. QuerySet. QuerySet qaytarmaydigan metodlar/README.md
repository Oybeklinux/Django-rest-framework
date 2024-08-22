# Mavzu 6: QuerySet. QuerySet qaytarmaydigan metodlar
 
<!-- TOC -->
* [1 get](#1-get)
* [2 create](#2-create)
* [3 get_or_create](#3-get_or_create)
* [4 update_or_create](#4-update_or_create)
* [5 bulk_create](#5-bulk_create)
* [6 bulk_update](#6-bulk_update)
* [7 count](#7-count)
* [8 in_bulk](#8-in_bulk)
* [9 latest](#9-latest)
* [10 earliest](#10-earliest)
* [11 first](#11-first)
* [12 last](#12-last)
* [13 aggregate](#13-aggregate)
* [14 exists](#14-exists)
* [15 contains](#15-contains)
* [16 update](#16-update)
* [17 delete](#17-delete)
* [Amaliyot](#amaliyot)
<!-- TOC -->


# 1 get

1. username='Asror' bo'lgan foydalanuvchi avtobiografiyasini chiqaring

```text
>>> Profile.objects.get(user__username='Asror').bio

'lorem ipsum'
```


# 2 create

2. username=Asror bo'lgan foydalanuvchiga yana bitta malaka qo'shing: FastAPI

```text
>>> Skill.objects.create(name='Fast API', user=Profile.objects.get(user__username='Asror'))

<Skill: Fast API>
```
Endi tekchirib ko'ramiz:

```text
>>> for skill in Skill.objects.all(): print(skill.name, skill.user)

Python Asror
Django Asror
Django Rest Framework Asror
Javascript Murod
React Murod
CSS,HTML Husniddin
Python Husniddin
Django Husniddin
Javascript Diyor
React Diyor
NextJs Diyor
Fast API Asror
```
# 3 get_or_create

Agar berilgan hamma parametrlarga mos obyekt bo'lsa, qaytaradi, aks holda bazaga qo'shib, qaytaradi
Avval get() metodini eslab olamiz: <br>

3. Agar usernaxme='Asror', first_name='Asror', last_name='Abduvosiqov' bo'lgan foydalanuvchini chiqaring

```text
>>> User.objects.get(username='Asror', first_name='Asror', last_name='Abduvosiqov')

<User: Asror>
```

4. Agar username='Mahmud', first_name='Mahmud', last_name="Yusup o'g'li" bo'lgan foydalanuvchi bo'lsa, ushani chiqaring, agar bazada mavjud bo'lmasa,  u holda avval kiritib, keyin uni qiymatlarini chiqaring

Agarda get() metodi yordamida amalga oshirsak, u holda bazada bo'lmasa xatolik bo'ladi:

```text
>>> User.objects.get(username='Mahmud', first_name='Mahmud', last_name='Yusup')

...
django.contrib.auth.models.User.DoesNotExist: User matching query does not exist.
```

Agar get_or_create() metodidan foydalansak, u holda agar bazada bo'lmasa, o'zi kiritib qo'yadi:

```text
>>> User.objects.get_or_create(username='Mahmud', first_name='Mahmud', last_name='Yusup')

(<User: Mahmud>, True)
```
Ikkinchi marta yana yozsak:

```text
>>> User.objects.get_or_create(username='Mahmud', first_name='Mahmud', last_name='Yusup')
(<User: Mahmud>, False)
```
Demak bu metoddan tuple() qaytadi: 
- Berilgan model obyekti(User)
- Bazada endi kiritilganligi (True), yok mavjudligini (False) bildiradigan bool qiymat   

# 4 update_or_create

5. Agar username='Yusuf' bo'lgan foydalnuvchi bazada bor bo'lsa, u holda uni first_name va last_name qiymatlarini o'zgartiring: first_name='Yusuf', last_name='Qobulov'. Agar topilmasa, yangi foydalanuvchi kiriting

```text
>>> User.objects.update_or_create(username='Yusuf', defaults={'first_name': 'Yusuf', 'last_name': 'Qobulov'})

(<User: Yusuf>, True)

>>> User.objects.get(username='Yusuf').first_name

'Yusuf'
```

Qaytarilgan ikkinchi qiymatdan (True) bilamizki bazada yo'q ekan, natijada kiritib qo'ydi

```text
>>> User.objects.update_or_create(username='Yusuf', defaults={'first_name': 'Yusufjon', 'last_name': 'Qobulov'})

(<User: Yusuf>, False)

>>> User.objects.get(username='Yusuf').first_name

'Yusufjon'
```

Ikkinchi marta boshqa qiymat bilan bergan edik, bazadan unique bo'lgan usernameni topib uni first_name va last_name qiymarlarini o'zgaritirib qo'ydi (False)

# 5 bulk_create

bulk_create() metodi birdaniga bir nechta qiymat berish uchun ishlatiladi

5. username='Husniddin' ga username='Asror'dan 2 ta habar jo'nating:
- body='matn 1', subject='1-habar'
- body='matn 2', subject='2-habar'

```text
>>> asror = Profile.objects.get(user__username='Asror')
>>> husniddin = Profile.objects.get(user__username='Husniddin')
>>> Message.objects.bulk_create([Message(sender=asror, receiver=husniddin, subject='1-habar',body='matn 1'), Message(s
ender=asror, receiver=husniddin, subject='2-habar',body='matn 2')])

[<Message: 1-habar>, <Message: 2-habar>]
```

# 6 bulk_update

bulk_update() metodi birdaniga bir qancha obyektlarni o'zgartirish uchun ishlatiladi. Bu metod yangilangan ob'yektlar sonini qaytaradi

6. Hamma loyihalarni vote_count qiymatini 10 balga oshirilsin. 

Avval hamma loyihalarga qanchadan bal berilganini ko'rib olamiz:

```text
>>> for pr in Project.objects.all(): print(pr, pr.vote_count)

IT Academy online ta'lim 100
ePark.uz 150
ЧД - че думаеш? 200
Dolina capital 30
Kannas-textile 50
Alimax pro 300
ePark 100
```

Endi o'zgartiramiz. Avval o'zgargan ob'yektlar ro'yxatini hosil qilib olamiz. So'ng bulk_update() metodiga parametr sifatida beramiz

```text
>>> for pr in Project.objects.all():
...    pr.vote_count += 10
...    projects.append(pr)

>>> Project.objects.bulk_update(projects, ['vote_count'])

7
```

# 7 count

Qaytgan QuerySetdagi obyektlar sonini qaytaradi

7. 30 dan ortiq ovoz olgan loyihalarni sonini chiqaring

```text
>>> Project.objects.filter(vote_count__gte=30).count()

7
```   
Demak 30 dan ortiq ovoz olgan loyihalarni soni 7 ta ekan


# 8 in_bulk

in_bulk() metodi bittada bir nechta obyektlarni qaytarish uchun ishlatiladi. U dict() qaytaradi

8. Hamma malakalarni id si bilan dict ko'rinishida chiqaring

```text
>>> Skill.objects.in_bulk()

{9: <Skill: Python>, 10: <Skill: Django>, 11: <Skill: Django Rest Framework>, 12: <Skill: Javascript>, 13: <Skill: Rea
ct>, 14: <Skill: CSS,HTML>, 15: <Skill: Python>, 16: <Skill: Django>, 17: <Skill: Javascript>, 18: <Skill: React>, 19:
 <Skill: NextJs>, 20: <Skill: Fast API>}
```

9. id=10 va id=11 bo'lgan malakalarni  dict ko'rinishida chiqaring

```text
>>> Skill.objects.in_bulk([10,11])

{10: <Skill: Django>, 11: <Skill: Django Rest Framework>}
```

# 9 latest

latest() metodi berilgan hususiyat bo'yicha eng ohirgisini olib beradi

10. Eng ohirgi ro'yxatdan o'tgan foydalanuvchi

```text
>>> User.objects.latest('date_joined')

<User: Yusuf>
```

# 10 earliest

earliest() metodi berilgan hususiyat bo'yicha eng boshidagini olib beradi

10. Eng avval ro'yxatdan o'tgan foydalanuvchi

```text
>>> User.objects.earliest('date_joined')

<User: admin>
```

# 11 first

first() metodi shunchaki QuerySetda turgan eng birinchisini qaytaradi


11. Foydalanuvchi tarafidan qilingan loyihani soni bo'yicha tartiblab chiqarng. Ro'yxatda eng birinchisini chiqaring

```text
>>> users = Profile.objects.annotate(total=Count('user_project')).filter(total__gt=0).order_by('-total')
>>> for user in users: print(user, user.total)

Diyor 3
Asror 2
Murod 1
Husniddin 1
```

Endi shu ro'yxatdan birnchisini chiqaramiz:

```text
>>> users[0]

<Profile: Diyor>
```
yoki
```text
>>> users.first()

<Profile: Diyor>
```


# 12 last

12. last() metodi first() dan farqi shuki, u eng ohirgisini olib beradi

```text
>>> users.last()
<Profile: Husniddin>
```

lekin indexga -1 berib bo'lmaydi
```text
>>> users[-1]
Traceback (most recent call last):
  File "<console>", line 1, in <module>
  File "C:\Users\oybek\AppData\Local\Programs\Python\Python310\lib\site-packages\django\db\models\query.py", line 341,
 in __getitem__
    raise ValueError("Negative indexing is not supported.")
ValueError: Negative indexing is not supported.
```

# 13 aggregate
aggregate() metodi annotate dan farqi shuki, u hamma jadvaldagi qiymatlar bo'yicha ishlaydi, annotate esa har bir guruh qiymatlar bilan alohida ishlaydi. aggregate dan bitta natijaviy qiymat qaytadi va u dict() ko'rinishida bo'ladi

13. Hamma loyihalar soni

```text
>>> Project.objects.aggregate(Count('id'))

{'id__count': 7}
```

14. Loyihaga berilgan eng katta baho

```text
>>> Project.objects.aggregate(max_vote=Max('vote_count'))

{'max_vote': 310}
```

# 14 exists
exists() metodi asosan qidirilganda bor yo'qligni bilish uchun ishlatiladi. Agar QuerySet bo'sh bo'lsa, False, aks holda True qaytaradi

15. username='Anvar' foydalanuvchi bazada borligini aniqlang

```text
>>> User.objects.filter(username='Anvar').exists()

True
```
Bor ekan

16. title='ecommerce' loyihasi mavjudligini aniqlang

```text
>>> Project.objects.filter(title='ecommerce').exists()

False
```
Yo'q ekan

# 15 contains

contains() metodi QuerySet ichida berilgan obyekt bor yo'qligini aniqlab beradi. True/False qaytaradi

17. Asror obyekti bazada bormi?

Avval asror o'zgaruvchisini ko'ramiz
```text
>>> asror

<Profile: Asror>
```
Endi bazada bor yo'qligini ko'ramiz

```text
>>> Profile.objects.all().contains(asror)

True
```
Demak bazada bor ekan

# 16 update
update() metodi QuerySetdagi hamma obyektlarni o'zgartiradi. O'zgargan ob'yektlar sonini qaytaradi

18. Hamma foydalanuvchilarni avtobiografiyasini o'zgartiring:
- bio = 'Mening karyeram 2022 yildan boshlandi'

```text
>>> Profile.objects.all().update(bio='Mening karyeram 2022 yildan boshlandi')

10

>>> for user in Profile.objects.all(): print(user.bio)

Mening karyeram 2022 yildan boshlandi
Mening karyeram 2022 yildan boshlandi
Mening karyeram 2022 yildan boshlandi
Mening karyeram 2022 yildan boshlandi
Mening karyeram 2022 yildan boshlandi
Mening karyeram 2022 yildan boshlandi
Mening karyeram 2022 yildan boshlandi
Mening karyeram 2022 yildan boshlandi
Mening karyeram 2022 yildan boshlandi
Mening karyeram 2022 yildan boshlandi
```

# 17 delete
delete() metodi QuerySetdagi hamma obyektlarni bazadan o'chiradi. O'chirildan ob'yektlar sonini qaytaradi

19. username=Husniddin ga yuborilgan hamma habarlarni o'chiring

```text
>>> Message.objects.filter(receiver=husniddin)

<QuerySet [<Message: Ish masalasida>, <Message: 1-habar>, <Message: 2-habar>]>
```
Demak Husniddinga 3 habar jo'natilgan ekan

```text
>>> Message.objects.filter(receiver=husniddin).delete()

(3, {'projects.Message': 3})
```

3 ta habarni o'chirdik, endi tekshirib ko'ramiz

```text
>>> Message.objects.filter(receiver=husniddin)
<QuerySet []>
```

# Amaliyot
1. username='Diyor' bo'lgan foydalanuvchining hamma loyihalarini chiqaring
2. username='Asror' bo'lgan foydalanuvchining hamma malakalarini (skill) chiqaring
3. username='Murod' bo'lgan foydalanuvchining yuborgan hamma habarlarini chiqaring
4. username='Husniddin' bo'lgan foydalanuvchiga yana bitta loyiha qo'shing: Online school
5. username='Murod' bo'lgan foydalanuvchi username='Asror' ga habar jo'natsin: subject="Do'sting Muroddan", body="Online ta'lim loyihasi juda ajoyib bo'libdi"   

6. title='Online kindergarden' bo'lgan loyihani chiqaring, agar bazada bo'lmasa, u holda avval uni kiriting: vote_count=100, vote_ratio=50 
7. title='ePark' nomli loyihani topib qiymatlarni o'zgartiring: vote_count=10, vote_ratio=30 . Agar bazada bo'lmasa, u holda yangi kiritib, keyin chiqaring 

5. username='Asror'ga bittada 4 ta malaka kiriting
6. Hamma foydalanuvchi first_name qiymatini katta harflar bilan yozib o'zgartirib chiqing. (M: Asror -> ASROR)
7. Hamma skill jadvalidagi definition atributini 'lorem ipsum' deb o'zgartiring
8. Pythonni biladiganlar sonini chiqaring
9. Django va pythondan kamida bittasini biladiganlar sonini chiqaring
10. Eng ohirgi yuborilgan habar
11. Eng avval yuborilgan habar
12. Eng birinchi ro'yxatdan o'tgan foydalanuvchi
13. Eng katta ovoz olgan loyiha
14. Eng ko'p habar olgan dasturchi
15. Eng ko'p fikr bildirilgan loyiha
16. Eng ohirgi ro'yxatdan o'tgan foydalanuvchi
17. Eng kam ovoz olgan loyiha
18. Eng kam habar olgan dasturchi
19. Eng kam fikr bildirilgan loyiha
20. Hamma foydalanuvchilar soni
21. Loyihaga berilgan eng kichik baho
22. Loyihaga berilgan o'rtacha baho
23. "Lug'at" nomli loyiha borligini aniqlang
24. 'Asror' habar yuborganligini aniqlang
25. Loyihaga berilgan hamma ovozlarni ikki barobar oshiring
