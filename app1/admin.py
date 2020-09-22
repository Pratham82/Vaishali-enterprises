from django.contrib import admin
from .models import Site,SitePosts

# Register your models here.
# admin.site.register(Site)

class SitePostsAdmin(admin.StackedInline):
	model = SitePosts

@admin.register(Site)
class SiteAdmin(admin.ModelAdmin):
	inlines = [SitePostsAdmin]
	
	class Meta:
		model = Site

@admin.register(SitePosts)
class SitePostsAdmin(admin.ModelAdmin):
	pass