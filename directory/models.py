from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    users_followed = models.ManyToManyField(to=User, through="Follow", through_fields=("follower", "following"), related_name="followers",)

class Post(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    description = models.CharField(max_length=280)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    favorited_users = models.ManyToManyField(to=User, through="Favorite", related_name="favorite_posts")

    def __str__(self):
        return self.title

class Comment(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    post = models.ForeignKey(to=Post, on_delete=models.CASCADE, related_name='comments')
    new_comment = models.TextField("", max_length=1000)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    
    def __str__(self):
        return self.new_comment

class Favorite(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    post = models.ForeignKey(to=Post, on_delete=models.CASCADE, related_name='favorites')


    class Meta:
        unique_together = ('post', 'user',)

class Follow(models.Model):
    follower = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name='follows_from')
    following = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name='follows_to')
    created_at = models.DateTimeField(auto_now_add=True, null=False)
