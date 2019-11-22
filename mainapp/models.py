from django.db import models

class China_Item(models.Model):
	id = models.AutoField(primary_key=True)
	sido = models.CharField(max_length=128)
	sigungu = models.CharField(max_length=128)
	cityGubun = models.CharField(max_length=128)
	marketType = models.CharField(max_length=128)
	userType = models.CharField(max_length=128)
	ageGroup = models.CharField(max_length=128)
	gender = models.CharField(max_length=64)
	dtYearMonth = models.CharField(max_length=128)
	userCount = models.IntegerField()
	useCount = models.IntegerField()
	useCost = models.IntegerField()
	# memo = JSONField(default={}, dump_kwargs={'ensure_ascii': False})

	def __str__(self):
		return "{}".format(self.id)



# sido sigungu cityGubun marketType userType ageGroup gender dtYearMonth  userCount  useCount     useCost
