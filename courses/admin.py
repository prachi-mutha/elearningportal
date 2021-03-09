from django.contrib import admin
from	.models	import	Course , Chapter ,TextBlock,FileUpload

# Register your models here.
@admin.register(Course)
class	CourseAdmin(admin.ModelAdmin):
	pass

@admin.register(Chapter)
class	ChapterAdmin(admin.ModelAdmin):
	pass
@admin.register(TextBlock)
class	TextBlockAdmin(admin.ModelAdmin):
	pass
@admin.register(FileUpload)
class	FileUploadAdmin(admin.ModelAdmin):
	pass