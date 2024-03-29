from django.contrib import admin
from users.models import User
from .models import Course, Lesson, Subscription


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('email',)
    search_fields = ('email',)


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'owner', 'price')
    search_fields = ('name', 'description')
    list_editable = ('owner', 'price')


@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'get_course_name', 'course_id', 'owner')
    search_fields = ('name', 'description')
    list_editable = ('course_id', 'owner')

    def get_course_name(self, obj):
        return obj.course_id.name if obj.course_id else None

    get_course_name.short_description = 'Course'


@admin.register(Subscription)
class SubscriptionAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'course')
    search_fields = ('user', 'course')
    list_editable = ('user', 'course')
