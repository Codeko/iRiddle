from django.contrib import admin
from iriddle.riddles.models import Category
from iriddle.riddles.models import Riddle
from iriddle.riddles.models import Tag
from iriddle.riddles.models import Valoration

admin.site.register(Tag)
admin.site.register(Category)
admin.site.register(Riddle)
admin.site.register(Valoration)

