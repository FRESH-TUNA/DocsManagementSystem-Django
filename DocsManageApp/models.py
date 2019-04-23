from django.db import models

class Document(models.Model):
    category = models.CharField(max_length=20)
    content = models.TextField()
    url = models.TextField()
    class MongoMeta:
        db_table = "DocsManageApp_document"
    def __str__(self):
        return self.content

class Category(models.Model):
    categoryName = models.CharField(max_length=20)
    class MongoMeta:
        db_table = "DocsManageApp_category"
    def __str__(self):
        return self.categoryName
#MongoMeta를 통해 db_table = "DocsManageApp_category" 존재하는 db사용