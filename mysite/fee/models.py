from django.db import models


# Create your models here.
class Info(models.Model):
    name = models.CharField(max_length=100, verbose_name="姓名")
    id_num = models.CharField(max_length=100, verbose_name="身份证号")
    fee = models.CharField(max_length=100, verbose_name="费用")
    pub_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "缴费信息"
