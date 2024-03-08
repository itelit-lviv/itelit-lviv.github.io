from django.db import models


# Create your models here.
class TrainingProgram(models.Model):
    title = models.CharField(max_length=200, verbose_name='Навчальний напрям')

    class Meta:
        verbose_name = 'Напрям'
        verbose_name_plural = 'Напрями'
        ordering = ('title',)
    def __str__(self):
        return self.title

class Course(models.Model):
    title = models.CharField(max_length=255, verbose_name='Назва курсу')
    public_title = models.CharField(max_length=200, verbose_name='Назва курсу для учнів')
    program = models.ForeignKey(TrainingProgram, on_delete=models.PROTECT, verbose_name='Напрям', related_name='courses')
    description = models.TextField(verbose_name='Опис')

    image = models.ImageField(verbose_name='Зображення курсу', upload_to='course_images', blank=True, null=True)
    age_level = models.IntegerField(verbose_name='Вік')

    class Meta:
        verbose_name = 'Курс'
        verbose_name_plural = 'Курси'
        ordering = ('program',)

    def __str__(self):
        return self.title


class Resource(models.Model):
    title = models.CharField(max_length=200, verbose_name='Назва ресурсу')
    resource_type = models.CharField(max_length=50, verbose_name='Посилання чи файл')  # Посилання чи файл
    link = models.URLField(null=True, blank=True, verbose_name='Посилання')
    file = models.FileField(upload_to='course_files/', null=True, blank=True, verbose_name='Файл')

    class Meta:
        verbose_name = 'Ресурс'
        verbose_name_plural = 'Ресурси'

    def __str__(self):
        return f'{self.title} - {self.resource_type}'


class Theory(models.Model):
    title = models.CharField(max_length=200, verbose_name='Назва')
    content = models.TextField(verbose_name='Теорія')
    resources = models.ManyToManyField(Resource, related_name='used_in_theory_levels', verbose_name='Ресурси')

    class Meta:
        verbose_name = 'Теорія'
        verbose_name_plural = 'Теорія'

    def __str__(self):
        return self.content


class Task(models.Model):
    title = models.CharField(max_length=200, verbose_name='Назва завдання')
    content = models.TextField(verbose_name='Текст завдання')
    image = models.ImageField(upload_to='task_images', blank=True, null=True)
    resources = models.ManyToManyField(Resource, related_name='used_in_tasks', verbose_name='Додаткові ресурси')

    class Meta:
        verbose_name = 'Завдання'
        verbose_name_plural = 'Завдання'

    def __str__(self):
        return self.title


class Level(models.Model):
    THEORY = 'Theory'
    TASK = 'Task'
    LEVEL_TYPES = [
        (THEORY, 'Теорія'),
        (TASK, 'Завдання'),
    ]

    title = models.CharField(max_length=200, verbose_name='Назва рівня')
    type = models.CharField(max_length=50, choices=LEVEL_TYPES, verbose_name='Тип рівня')
    resources = models.ManyToManyField(Resource, verbose_name='Посилання', blank=True)
    theory = models.ManyToManyField(Theory,  related_name='theory_levels', blank=True, verbose_name='Теорія')
    task = models.ManyToManyField(Task, related_name='tasks_levels', blank=True, verbose_name='Завдання')

    class Meta:
        verbose_name = 'Рівень'
        verbose_name_plural = 'Рівні'

    def __str__(self):
        return self.title


class Topic(models.Model):
    title = models.CharField(max_length=200, verbose_name='Тема')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='topics', verbose_name='Курс')
    description = models.TextField(verbose_name='Опис', blank=True, null=True)
    resources = models.ManyToManyField(Resource, verbose_name='Навчальні ресурси', blank=True)
    levels = models.ManyToManyField(Level, related_name='topics', verbose_name='Рівні')

    class Meta:
        verbose_name = 'Тема'
        verbose_name_plural = 'Теми'

    def __str__(self):
        return self.title

