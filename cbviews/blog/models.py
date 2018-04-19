# https://raw.githubusercontent.com/codingforentrepreneurs/Django-Models-Unleashed/master/src/blog/models.py
from datetime import timedelta, datetime, date

from django.db import models
from django.db.models.signals import pre_save, post_save
from django.utils.encoding import smart_text
from django.utils import timezone 
from django.utils.text import slugify
from django.utils.timesince import timesince

PUBLISH_CHOICES = [
        ('draft', 'Draft'),
        ('publish', 'Publish'),
        ('private', 'Private'),
    ]


class PostModel(models.Model):
    id = models.BigAutoField(primary_key=True)
    active = models.BooleanField(default=True)
    title = models.CharField(max_length=240, 
                             verbose_name='Post title', 
                             unique=True,
                             error_messages={'unique': 'This title is not unique, please try again.',
                               				 'blank': 'This field is not full, please try again.'},
                             help_text='Must be a unique title.')
    slug = models.SlugField(null=True, blank=True)
    content = models.TextField(null=True, blank=True)
    publish = models.CharField(max_length=120, choices=PUBLISH_CHOICES, default='draft')
    view_count = models.IntegerField(default=0)
    publish_date = models.DateField(auto_now=False, auto_now_add=False, default=timezone.now)
    author_email = models.EmailField(max_length=240, null=True, blank=True)
    added_by = models.CharField(max_length=240, default='Anonymous')
    updated = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return smart_text(self.title)

    @property
    def age(self):
        if self.publish == 'publish':
            now = datetime.now()
            publish_time = datetime.combine(
                                self.publish_date,
                                datetime.now().min.time()
                        )
            try:
                difference = now - publish_time
            except:
                return 'Unknown'
            if difference <= timedelta(minutes=1):
                return 'just now'
            return '{time} ago'.format(time= timesince(publish_time).split(', ')[0])
        return 'Not published'

def blog_post_model_pre_save_receiver(sender, instance, *args, **kwargs):
    instance.slug = slugify(instance.title) 

pre_save.connect(blog_post_model_pre_save_receiver, sender=PostModel)