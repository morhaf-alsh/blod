from django.db import models
import string, random
from accounts.models import User
# Create your models here.
categories = {
    ("General","General"),
    ("DevOps","DevOps"),
    ("Networking","Networking")
}
class Blog(models.Model):
    title = models.CharField(max_length=75)
    slug = models.SlugField(default=''.join(random.sample(string.ascii_lowercase, 10)))
    image = models.ImageField(upload_to ='blogs/static/blogs/', null=True, default='static/E Card.jpg')
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True) #temporary
    data_posted = models.DateTimeField(auto_now_add=True)
    data_modified = models.DateTimeField(auto_now=True)
    category = models.CharField(choices=categories, default="General", null=False,max_length=100)
    text = models.TextField()
    likes = models.IntegerField()

    class Meta:
        verbose_name = 'blog'
        verbose_name_plural = 'Blogs'
    def __str__(self):
        return self.title
    def get_number_of_likes(self):
        return self.likes.count()