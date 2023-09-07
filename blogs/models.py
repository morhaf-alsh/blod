from django.db import models

# Create your models here.
categories = {
    ("General","General"),
    ("DevOps","DevOps"),
    ("Networking","Networking")
}
class Blog(models.Model):
    title = models.CharField(max_length=75)
    author = models.CharField(max_length=50) #temporary
    data_posted = models.DateTimeField(auto_now_add=True)
    data_modified = models.DateTimeField(auto_now=True)
    category = models.CharField(choices=categories, default="General", null=False,max_length=100)
    text = models.TextField()
    likes = models.IntegerField()