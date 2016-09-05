from django.contrib import admin
from api.models import Idea, Vote, User
from api.models import Commentary, Image, Category


admin.site.register(Idea)
admin.site.register(Vote)
admin.site.register(Commentary)
admin.site.register(Image)
admin.site.register(Category)
admin.site.register(User)

