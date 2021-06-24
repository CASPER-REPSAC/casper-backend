from django.db import models


class Post(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey('auth.User', related_name='posts', on_delete=models.CASCADE)
    board = models.ForeignKey('Board', related_name='posts', on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    content = models.TextField()
    viewer_num = models.IntegerField(default=0)

    class Meta:
        ordering = ['created']


class Board(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name
