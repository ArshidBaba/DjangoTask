from django.db import models


# class Category(models.Model):
#     name = models.CharField(max_length=30)

#     def __str__(self):
#         return self.name


class Todo(models.Model):
    title = models.CharField(max_length=255)
    # category = models.ForeignKey(
    #     Category, related_name="todo_category", on_delete=models.CASCADE
    # )
    category = models.CharField(max_length=30)
    description = models.TextField()
    date = models.DateField()

    def __str__(self):
        return self.title
