from django.contrib.auth.models import AbstractUser
from django.db import models  # импорт

class Author(models.Model):
    """
        cвязь «один к одному» с встроенной моделью пользователей User;
        рейтинг пользователя.
        Метод update_rating() модели Author, который обновляет рейтинг пользователя,
         переданный в аргумент этого метода.
    Он состоит из следующего:
    суммарный рейтинг каждой статьи автора умножается на 3;
    суммарный рейтинг всех комментариев автора;
    суммарный рейтинг всех комментариев к статьям автора.
"""
    full_name = models.CharField()
    name = models.CharField(null=True)
    staff = models.OneToOneField(AbstractUser, unique=True)
    rating = models.IntegerField(default=0)
    Author = models.OneToOneField(AbstractUser, unique=True)

    def update_rating(self):
        Comment. += 1
        Author.rating *= 3



class Category(models.Model):
    Category_name = models.CharField(unique=True)


class Post(models.Model):
    """
        связь «один ко многим» с моделью Author;
        поле с выбором — «статья» или «новость»;
        автоматически добавляемая дата и время создания;
        связь «многие ко многим» с моделью Category (с дополнительной моделью PostCategory);
        заголовок статьи/новости;
        текст статьи/новости;
        рейтинг статьи/новости.
        Методы like() и dislike() в моделях Comment и Post, которые увеличивают/уменьшают
        рейтинг на единицу.
        Метод preview() модели Post, который возвращает начало статьи (предварительный просмотр)
         длиной 124 символа и добавляет многоточие в конце
"""
    news_1 = models.BooleanField
    Post = models.ManyToManyField(Category, through='PostCategory')
    time = models.DateTimeField
    articls_name = models.CharField(max_length=100)
    text = models.TextField
    Author = models.ForeignKey(Author, on_delete=models.CASCADE)

    def preview(self):
        text = models.CharField(max_length=124)

    def like(self):
        rating = self.rating
        rating += 1
        return rating

    def dislike(self):
        rating = self.rating
        rating -= 1
        return rating


class PostCategory(models.Model):
    """
        связь «один ко многим» с моделью Post;
        связь «один ко многим» с моделью Category.
"""
    Post = models.ManyToManyField
    Category = models.ManyToManyField


class Comment(models.Model):
    """
        связь «один ко многим» с моделью Post;
        связь «один ко многим» со встроенной моделью User (комментарии может оставить любой
        пользователь, необязательно автор);
        текст комментария;
        дата и время создания комментария;
        рейтинг комментария.
        Методы like() и dislike() в моделях Comment и Post, которые увеличивают/уменьшают
         рейтинг на единицу.
"""

    def like(self):
        rating = self.rating
        rating += 1
        return rating

    def dislike(self):
        rating = self.rating
        rating -= 1
        return rating
