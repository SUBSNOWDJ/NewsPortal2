from django.db import models
from django.core.validators import MinValueValidator
from django.contrib.auth.models import User


class User(models.Model):
    # Встроенная модель пользователей Django
    pass


class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    rating = models.IntegerField(default=0)

    def update_rating(self):
        total_post_rating = sum(post.rating for post in self.post_set.all()) * 3
        total_comment_rating = sum(comment.rating for comment in self.comment_set.all())
        total_comment_rating_to_posts = sum(
            comment.rating for post in self.post_set.all() for comment in post.comment_set.all())
        self.rating = total_post_rating + total_comment_rating + total_comment_rating_to_posts
        self.save()


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name.title()


class Post(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    post_type_choices = [('article', 'Статья'), ('news', 'Новость')]
    post_type = models.CharField(max_length=10, choices=post_type_choices)
    created_at = models.DateTimeField(auto_now_add=True)
    categories = models.ManyToManyField(Category, through='PostCategory')
    title = models.CharField(max_length=255)
    content = models.TextField()
    rating = models.IntegerField(default=0)

    def preview(self):
        return self.content[:124] + '...' if len(self.content) > 124 else self.content

    def like(self):
        self.rating += 1
        self.save()

    def dislike(self):
        self.rating -= 1
        self.save()


class PostCategory(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    rating = models.IntegerField(default=0)

    def like(self):
        self.rating += 1
        self.save()

    def dislike(self):
        self.rating -= 1
        self.save()


class News(models.Model):
    name = models.CharField(
        max_length=150,
        unique=True,  # названия товаров не должны повторяться
    )
    description = models.TextField()
    created_time = models.DateField()

    # поле категории будет ссылаться на модель категории
    category = models.ForeignKey(
        to='Category',
        on_delete=models.CASCADE,
        related_name='news',  # все продукты в категории будут доступны через поле products
    )

    def __str__(self):
        return f'{self.name.title()}: {self.description[:20]}'

    class Meta:
        ordering = ['-created_time']

# Create your models here.
