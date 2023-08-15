# Vazifa 1:

```text
>>> from users.models import Profile
>>> Profile.objects.get(user__username = 'Diyor')  
<Profile: Profile object (9)>
>>> diyor_profile = Profile.objects.get(user__username = 'Diyor') 
>>> diyor_profile.bio="lorem ipsum"
>>> diyor_profile.location="Toshkent sh. Mirzo Ulu'bek"
>>> diyor_profile.profile_image="portfolio/Diyor.png"
>>> diyor_profile.save()
>>>
>>> husniddin_profile = Profile.objects.get(user__username = 'Husniddin') 
>>> husniddin_profile                                                    
<Profile: Profile object (8)>
>>> husniddin_profile.bio="lorem ipsum"
>>> husniddin_profile.location="Toshkent v. Zagiota tumani"
>>> husniddin_profile.profile_image="portfolio/default_profile.webp"
>>> husniddin_profile.social_github="https://17husniddin.github.io/Potfolio/index.html"
>>> husniddin_profile.social_instagram="https://www.instagram.com/husnidd1n_17/"
>>> husniddin_profile.save()
```

# Vazifa 2

```text
>>> from projects.models import Message
>>> from users.models import Profile
>>> murod_f = Profile.objects.get(user__username = 'Murod')               
>>> murod_f
<Profile: Profile object (7)>
>>> asror_f = Profile.objects.get(user__username = 'Asror')      
>>> from projects.models import Message
>>> Message.objects.create(subject='Ish masalasida', body="Siz bilan qanday bog'lansak bo'ladi", sender=murod_f, receiver=asror_f)                             
<Message: Message object (6)>
```

# Vazifa 3

```text
>>> from projects.models import Skill
>>> from users.models import Profile
>>> asror_f = Profile.objects.get(user__username='Asror')
>>> Skill.objects.create(name='Python', user=asror_f) 
<Skill: Skill object (1)>
>>> Skill.objects.create(name='Django', user=asror_f) 
<Skill: Skill object (2)>
>>> Skill.objects.create(name='Django Rest Framework', user=asror_f) 
<Skill: Skill object (3)>

>>> murod_f = Profile.objects.get(user__username='Murod')      
>>> Skill.objects.create(name='Javascript', user=murod_f)            
<Skill: Skill object (4)>
>>> Skill.objects.create(name='React', user=murod_f)      
<Skill: Skill object (5)>

>>> husniddin_f = Profile.objects.get(user__username='Husniddin')  
>>> Skill.objects.create(name='CSS, HTML', user=husniddin_f)
<Skill: Skill object (6)>
>>> Skill.objects.create(name='Python', user=husniddin_f)    
<Skill: Skill object (7)>
>>> Skill.objects.create(name='Django', user=husniddin_f)    
<Skill: Skill object (8)>

>>> diyor_f = Profile.objects.get(user__username='Diyor')              
>>> Skill.objects.create(name='Javascript', user=diyor_f) 
<Skill: Skill object (9)>
>>> Skill.objects.create(name='React', user=diyor_f)      
<Skill: Skill object (10)>
>>> Skill.objects.create(name='NextJS', user=diyor_f) 
<Skill: Skill object (11)>
```

# Vazifa 4

```text
>>> from projects.models import Project
>>> from users.models import Profile

>>> asror_f = Profile.objects.get(user__username='Asror')      
>>> Project.objects.create(title='IT Academy online ta\'lim', image='projects/project-1.png', vote_count=100, vote_ratio=60, description="lorem ipsum", user=asror_f) 
<Project: Project object (3)>

>>> murod_f = Profile.objects.get(user__username='Murod')                                                                                           
>>> Project.objects.create(title='Kannas-textile', image='projects/project-5.png', vote_count=50, vote_ratio=90, description="lorem ipsum", user=murod_f)     
<Project: Project object (5)>

>>> husniddin_f = Profile.objects.get(user__username='Husniddin')      
>>> Project.objects.create(title='Alimax pro', image='projects/project-6.png', vote_count=300, vote_ratio=90, description="lorem ipsum", user=husniddin_f)   
<Project: Project object (6)>

>>> diyor_f = Profile.objects.get(user__username='Diyor')
>>> Project.objects.create(title='ePark.uz', image='projects/project-2.png', vote_count=150, vote_ratio=20, description="lorem ipsum", user=diyor_f)   
<Project: Project object (7)>
>>> Project.objects.create(title='ЧД - че думаеш?', image='projects/project-3.png', vote_count=200, vote_ratio=10, description="lorem ipsum", user=diyor_f)   
<Project: Project object (8)>
>>> Project.objects.create(title='Dolina capital', image='projects/project-4.png', vote_count=30, vote_ratio=70, description="lorem ipsum", user=diyor_f)
<Project: Project object (9)>
```

# Vazifa 5
```text
# Talaba qilgan loyihalar
class Project(models.Model):
    # loyiha nomi
    title = models.CharField(max_length=100)  # Majburiy
    # loyiha haqida qisqacha ma'lumot
    description = models.TextField(blank=True, null=True)  # Majburiy emas
    # loyiha ko'rinishi
    image = models.ImageField(upload_to='projects', default='projects/empty.png')
    # loyihaga demo havola
    demo_link = models.CharField(max_length=200, blank=True, null=True)
    # loyihaning haqiqiy havolasi
    source_code = models.CharField(max_length=200, blank=True, null=True)
    # loyihaga berilgan ijobiy/salbiy hamma ovozlar soni
    vote_count = models.IntegerField(default=0)
    # loyihaga berilgan ijobiy ovozlar nisbati (foizda)
    vote_ratio = models.IntegerField(default=0)
    # loyiha kiritilgan sana
    created = models.DateField(auto_now_add=True)
    # edited = models.DateField(auto_now_add=True, null=True)
    user = models.ForeignKey(Profile, on_delete=models.SET_NULL, null=True)
    tag = models.ManyToManyField('Tag', blank=True, related_name="project_tag")

    def __str__(self) -> str: # yangi kiritilgan qator
        return self.title     # yangi kiritilgan qator
```

# Vazifa 6
Quyidagi ma'lumotlarni Review jadvaliga kiriting:

Fikr qaysidur profil/foydalanuvchi tarafigan qaysidur loyihaga beriladi, shuning uchun ularni obyektini o'qib saqlab keyin fikr (review) kiritamiz

```text
>>> from projects.models import Review
       
>>> asror_f = Profile.objects.get(user__username='Asror')         
>>> dolina_pr = Project.objects.get(title='Dolina capital')
>>> Review.objects.create(body="Zo'r loyiha bo'libdi", value=6, project=dolina_pr, user=asror_f)
<Review: Review object (1)>

>>> alimax_pr = Project.objects.get(title='Dolina capital')
>>> Review.objects.create(body="CSS, HTML da qilinganmi?", value=4, project=alimax_pr, user=asror_f) 
<Review: Review object (2)>

>>> academy = Project.objects.get(title='IT Academy online ta\'lim') 
>>> diyor_f = Profile.objects.get(user__username='Diyor')      
>>> Review.objects.create(body="Online ta'lim yaxshi chiqibdi", value=10, project=academy, user=diyor_f)
<Review: Review object (3)>

>>> ch_pr = Project.objects.get(id=7)
>>> murod_f = Profile.objects.get(user__username='Murod')
>>> Review.objects.create(body="Ajoyib loyiha ekan", value=3, project=ch_pr, user=murod_f)
<Review: Review object (4)>

>>> epark_pr = Project.objects.get(id=7)
>>> Review.objects.create(body="Dizayni chiroyli chiqibdi", value=10, project=epark_pr, user=murod_f)
<Review: Review object (5)>

>>> husniddin_f = Profile.objects.get(user__username='Husniddin')      
>>> Review.objects.create(body="Foydali va qiziqarli ekan", value=10, project=epark_pr, user=husniddin_f)
<Review: Review object (6)>

>>> academy = Project.objects.get(title='IT Academy online ta\'lim') 
>>> Review.objects.create(body="Bizga ham qilib bering", value=20, project=academy, user=husniddin_f)
<Review: Review object (7)>
```

