from django.db import models

# Create your models here.
class Site(models.Model):
	site_id = models.AutoField
	clientName = models.CharField(max_length=50)
	status = models.CharField(max_length=50, default="")
	location = models.CharField(max_length=50, default="")
	payment=models.IntegerField(default=0)
	description = models.CharField(max_length=300)
	pub_date = models.DateField()
	image = models.ImageField(upload_to="mediaFiles/images", default="")

	def __str__(self):
		return self.clientName

class SitePosts(models.Model):
	post = models.ForeignKey(Site, default=None, on_delete=models.CASCADE)
	image = models.ImageField(upload_to="mediaFiles/images", default="")

	def __str__(self):
		return self.post.clientName