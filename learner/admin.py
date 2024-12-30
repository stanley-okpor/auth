from django.contrib import admin

from .models import Course, Lesson, Enrollment, Progress

# Admin configuration for Course model
class LessonInline(admin.TabularInline):
    model = Lesson
    extra = 1  # Allows adding one additional lesson inline in the admin panel

class CourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'duration')  # Fields displayed in the admin list view
    search_fields = ('title',)  # Search functionality on the title field
    inlines = [LessonInline]  # Inline lessons within the course admin page

# Admin configuration for Enrollment model
class EnrollmentAdmin(admin.ModelAdmin):
    list_display = ('user', 'course', 'enrolled_on')
    list_filter = ('enrolled_on',)  # Filter enrollments by date
    search_fields = ('user__username', 'course__title')

# Admin configuration for Progress model
class ProgressAdmin(admin.ModelAdmin):
    list_display = ('user', 'lesson', 'completed')
    list_filter = ('completed',)
    search_fields = ('user__username', 'lesson__title')



# Register models with their admin configurations
admin.site.register(Course, CourseAdmin)
admin.site.register(Enrollment, EnrollmentAdmin)
admin.site.register(Progress, ProgressAdmin)
