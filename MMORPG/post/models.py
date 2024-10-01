from django.db import models
from django.contrib.auth import get_user_model
from django_ckeditor_5.fields import CKEditor5Field


class Post(models.Model):
    CATEGORY_NAME = [
        ('TN', 'Tank'),
        ('HE', 'Healer'),
        ('DD', 'Dd'),
        ('DL', 'Dealer'),
        ('GM', 'GuildMaster'),
        ('QG', 'QuestGiver'),
        ('BS', 'BlackSmith'),
        ('TN', 'Tanner'),
        ('PM', 'PotionMaster'),
        ('MS', 'MasterSpells'),
    ]

    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    time_create = models.DateTimeField(auto_now_add=True)
    category = models.CharField(max_length=15, choices=CATEGORY_NAME)
    text = CKEditor5Field('Text', config_name='extends')

    def __str__(self):
        return f'{self.text}'
