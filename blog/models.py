from django.db import models

# Create your models here.
class Blogpost(models.Model):
    post_id=models.AutoField(primary_key="true")
    title=models.CharField(max_length=300, default="")
    hdng0=models.CharField(max_length=500, default="")
    chdng0=models.CharField(max_length=500, default="")
    hdng1 = models.CharField(max_length=500, default="")
    chdng1=models.CharField(max_length=500, default="")
    hdng2 = models.CharField(max_length=500, default="")
    chdng2=models.CharField(max_length=500, default="")
    hdng3 = models.CharField(max_length=500, default="")
    chdng3=models.CharField(max_length=500, default="")
    pub_date =models.DateField()
    thumbnail=models.ImageField(upload_to="shop/images", default="")

    def __str__(self):
        return (self.title)
