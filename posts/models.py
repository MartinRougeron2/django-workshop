from django.db import models

from users.models import BirddyTor


class Birddy(models.Model):
    title = models.CharField(verbose_name="Title", max_length=180, default="Title")
    desc = models.CharField(verbose_name="Description", max_length=180, blank=True)

    author = models.ForeignKey(BirddyTor, on_delete=models.PROTECT, related_name='author', null=True)
    liked_by = models.ManyToManyField(BirddyTor, related_name='likes', blank=True)
    disliked_by = models.ManyToManyField(BirddyTor, related_name='dislikes', blank=True)
    pub_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "{} # '{}' by {}".format(self.id, self.title, self.author)

    @property
    def comments(self):
        return Comment.objects.filter(post=self)


class Comment(models.Model):
    author = models.ForeignKey(BirddyTor, on_delete=models.PROTECT, null=True)
    pub = models.DateTimeField(auto_now=True)
    text = models.CharField(max_length=1000, default="")
    response = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True)
    post = models.ForeignKey(Birddy, on_delete=models.CASCADE, related_name='post', blank=True, null=True)

    def __str__(self):
        return self.text
