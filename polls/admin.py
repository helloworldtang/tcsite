from django.contrib import admin
from django.contrib.admin import ModelAdmin
from models import Question, Choice

# Register your models here.
class ChoiceInline(admin.StackedInline):
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    # class QuestionAdmin(admin.TabularInline):
    list_display = ('question_text', 'pub_date')
    # list_display = ('question_text', 'pub_date', 'was_published_recently')
    fieldsets = [
        (None, {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline]

# fieldsets = [
#     (None, {'fields': ['question_text']}),
#     ('Date information', {'fields': ['pub_date']}),
# ]
# fields=['pub_date','question_text']


admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)
