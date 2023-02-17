from django.db import models


class Women(models.Model): # Наследуем от базового класса Model, в котором уже есть id записей
    title = models.CharField(max_length=255) # Текстовое поле (описание полей смотрим в документации djbook.ru)
    content = models.TextField(blank=True) # Расширенная информация (параметр, что поле может быть пустым)
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/") # Поле фото (в параметре указывается каталог, в который будет загружаться изображение, при этом можно разделить на подкаталоги по году/месяцу/дню)
    time_create = models.DateTimeField(auto_now_add=True) # Время создания статьи (параметр принимает текущее время и более никогда не меняется)
    time_update = models.DateTimeField(auto_now=True) # Время последнего редактирования (Параметр принимает текущее время, но меняется каждый раз при обновлении)
    is_published = models.BooleanField(default=True) # Каждый раз, когда мы будем загружать, оно будет принимать значение True
