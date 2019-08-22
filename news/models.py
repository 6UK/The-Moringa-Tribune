from django.db import models
import datetime as dt 
# Create your models here.
# class Product(models.Models):
#     title           =models.TextField()
#     description     =models.TextField()
#     price           =models.TextField()
#     summary         =models.TextField(default='YESSIR')

class Editor(models.Model):
   first_name = models.CharField(max_length =30)
   last_name = models.CharField(max_length =30)
   email = models.EmailField()
   def __str__(self):
       return self.first_name
   class Meta:
       ordering = ['first_name']
class tags(models.Model):
   name = models.CharField(max_length =30)
   def __str__(self):
       return self.name
class Article(models.Model):
    @classmethod
    def search_by_title(cls,search_term):
        news = cls.objects.filter(title__icontains=search_term)
        return news
    title = models.CharField(max_length =60,default="title")
    post = models.TextField(default="post")
    editor = models.ForeignKey(Editor, on_delete=models.CASCADE,default="editor")
    tags = models.ManyToManyField(tags,default="tags")
    pub_date = models.DateTimeField(auto_now_add=True)  
    article_image = models.ImageField(upload_to = 'articles/',default="article_image")
    @classmethod
    def todays_news(cls):
        today = dt.date.today()
        news = cls.objects.filter(pub_date__date = today)
        return news
    @classmethod
    def days_news(cls,date):
        news = cls.objects.filter(pub_date__date = date)
        return news
