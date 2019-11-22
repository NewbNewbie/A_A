from django.db import models

class China_Item(models.Model):
	china_id = models.AutoField(primary_key=True)
	china_sido = models.CharField(max_length=128)
	china_sigungu = models.CharField(max_length=128)
	china_cityGubun = models.CharField(max_length=128)
	china_marketType = models.CharField(max_length=128)
	china_dtYearMonth = models.CharField(max_length=128)
	china_userCount = models.IntegerField()
	china_useCount = models.IntegerField()
	china_useCost = models.IntegerField()
	# memo = JSONField(default={}, dump_kwargs={'ensure_ascii': False})

	def __str__(self):
		return "{}".format(self.china_id)


class Korea_Item(models.Model):
	korea_id = models.AutoField(primary_key=True)
	korea_sido = models.CharField(max_length=128)
	korea_sigungu = models.CharField(max_length=128)
	korea_cityGubun = models.CharField(max_length=128)
	korea_marketType = models.CharField(max_length=128)
	korea_userType = models.CharField(max_length=128)
	korea_ageGroup = models.CharField(max_length=128)
	korea_gender = models.CharField(max_length=64)
	korea_dtYearMonth = models.CharField(max_length=128)
	korea_userCount = models.IntegerField()
	korea_useCount = models.IntegerField()
	korea_useCost = models.IntegerField()
	# memo = JSONField(default={}, dump_kwargs={'ensure_ascii': False})

	def __str__(self):
		return "{}".format(self.korea_id)



# sido sigungu cityGubun marketType userType ageGroup gender dtYearMonth  userCount  useCount     useCost
