from django.db import models

class Category(models.Model):
    category_id = models.AutoField(primary_key=True, null=False, blank= False, unique=True)
    category_name = models.CharField(max_length=100)

    def __str__(self):
        return self.category_name

class Member(models.Model):
    member_id = models.AutoField(primary_key=True, null=False, blank= False, unique=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255, blank=True, null=True)
    phone_number = models.IntegerField()
    email_address = models.EmailField()
    issue_date = models.DateField(auto_now_add= True)
    renew_date = models.DateField()

    def __str__(self) -> str:
        return (self.first_name + self.last_name)

class Book(models.Model):
    book_id = models.AutoField(primary_key=True, null=False, blank= False, unique=True)
    book_name = models.CharField(max_length=100)
    category = models.ForeignKey(Category, null=True, on_delete=models.SET_NULL, related_name="book_category")
    description = models.TextField(blank=True, null=True)
    author_name = models.CharField(max_length=100)
    publish_date = models.DateField()
    publisher = models.CharField(max_length=100)
    issued_to = models.ForeignKey(Member, null=True, on_delete=models.SET_NULL)
    def __str__(self):
        return self.book_name