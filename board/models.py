from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Post(models.Model):
    author = models.ForeignKey('accounts.User', related_name='posts', on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    viewer_num = models.IntegerField(default=0)
    category = models.ForeignKey('board.Category', related_name='posts', on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    content = models.TextField()

    class Meta:
        ordering = ['created_date']


class Suggestion(models.Model):
    SUGGESTION_TYPE = (
        ('S', 'Study'),
        ('P', 'Project'),
        ('C', 'CTF')
    )
    author = models.ForeignKey('accounts.User', related_name='suggestions', on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    type = models.CharField(max_length=1, choices=SUGGESTION_TYPE)
    title = models.CharField(max_length=100)
    content = models.TextField()

    class Meta:
        ordering = ['created_date']

    def __str__(self):
        return "[" + self.type + "] " + self.title


class Chat(models.Model):
    author = models.ForeignKey('accounts.User', related_name='chats', on_delete=models.CASCADE)
    suggestion = models.ForeignKey('board.Suggestion', related_name='chats', on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    content = models.TextField()

    class Meta:
        ordering = ['created_date']


class Question(models.Model):
    QUESTION_STATUS = (
        ('U', 'Unsolved'),
        ('S', 'Solved')
    )
    author = models.ForeignKey('accounts.User', related_name='questions', on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    expiration_date = models.DateTimeField(null=True)
    question_category = models.CharField(max_length=100)
    status = models.CharField(max_length=1, choices=QUESTION_STATUS)
    title = models.CharField(max_length=100)
    content = models.TextField()

    class Meta:
        ordering = ['created_date']

    def __str__(self):
        return '[' + self.status + '] ' + self.title


class Answer(models.Model):
    author = models.ForeignKey('accounts.User', related_name='answers', on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    question = models.ForeignKey('board.Question', related_name='answers', on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    content = models.TextField()

    class Meta:
        ordering = ['created_date']
