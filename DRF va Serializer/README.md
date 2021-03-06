 # Mavzu 4: DRF va Serializer
 
## Reja:
- [1 Terminlar](#1-terminlar)
- [2 Nazariya](#2-nazariya)

## 1 Terminlar
```
DRF - Django Rest Framework
```

## 2 Nazariya
**Reja**
- [2.1 Django Rest Framework]
  - [2.1.1 O'rnatish]
  - [2.1.2 Tushunchalar]
- [2.2 Serializer]  
- [2.3 Amaliyot]

### 2.1 Django Rest Framework 
[DRF hujjati](https://www.django-rest-framework.org/)

#### 2.1.1 O'rnatish 
```commandline
pip install djangorestframework
```

Python va django versiyalariga e'tibor bering. Talablarga muvofiq bo'lishi kerak

```commandline
python --version
django-admin --version
```
Loyihaga DRF ni qo'shish

```text

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'watchlist.apps.WatchlistConfig',
    'rest_framework'
]
```

### 2.1.2 Tushunchalar

![](images/img.png)

Serialize - Murakkab obyektni JSON formatiga mos bo'lgan dict toifasiga o'girib berish
<br>

![](images/img_1.png)

<br>
Serialize - so'rov jo'natganda (Request) ishlatiladi <br>
Deserialize - so'rovga javob kelgan (Response) ishlatiladi
<br>



![](images/img_2.png)
<br>
##### [Serializer](https://www.django-rest-framework.org/tutorial/1-serialization/):
- serializers.Serializer
- serializers.ModelSerializer

##### [Views](https://www.django-rest-framework.org/api-guide/views/)
- Class based
- Function based

##### API bilan ishlash

- DRF Browser API
- Postman
- HTTPie


### 2.3 Amaliyot
