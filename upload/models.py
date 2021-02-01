from django.utils import timezone
from django.db import models
from django.db.models.fields import FloatField
from django.forms.fields import FloatField as FloatFormField
from django.contrib.auth.models import User
from django.conf import settings
from django.urls import reverse
from django.utils.text import slugify



# Create your models here.
class Upload (models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )


    Title   = models.CharField(max_length=250)
    slug    = models.SlugField(max_length=250,
                               unique_for_date='publish', null=True)
    author  = models.ForeignKey(settings.AUTH_USER_MODEL,
                                related_name='publication_upload',
                                on_delete=models.CASCADE,
                                null=True
                                )
    Issn    = models.SlugField(max_length=10, db_index=True)
    Title2  = models.CharField(name='Second Title',
                               max_length=250, null=True, blank=True)
    Points  = models.IntegerField(default=1)
    anu     = models.CharField(max_length=1,
                               name='architecture and urbanistic', null=True,
                               blank=True)
    history = models.CharField(max_length=1, null=True, blank=True)
    ling    = models.CharField(max_length=1, name='linguistics',
                               null=True, blank=True)
    lite    = models.CharField(max_length=1, name='literature',
                               null=True, blank=True)
    socar   = models.CharField(max_length=1,
                               name='studies on culture and religion',
                               null=True, blank=True)
    soa     = models.CharField(max_length=1, name='studies on arts',
                               null=True, blank=True)
    auto    = models.CharField(max_length=1,
                               name='automatic, electronic and electrotechnic',
                               null=True, blank=True)
    techIT  = models.CharField(max_length=1,
                               name='technical IT and telecomunication',
                               null=True, blank=True)
    chem    = models.CharField(max_length=1,
                               name='chemical engineering',
                               null=True, blank=True)
    civil   = models.CharField(max_length=1,
                               name='civil engineering and transport',
                               null=True, blank=True)
    mater   = models.CharField(max_length=1,
                               name='material engineering',
                               null=True, blank=True)
    mech    = models.CharField(max_length=1,
                               name='mechanical engineering',
                               null=True, blank=True)
    envior  = models.CharField(max_length=1,
                               name='environmnetal engineering, mining and energetic',
                               null=True,blank=True)
    pharma  = models.CharField(max_length=1,
                               name='pharmaceutical sciences',
                               null=True, blank=True)
    medic   = models.CharField(max_length=1,
                               name='medical sciences',
                               null=True, blank=True)

    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True, null=True)
    updated = models.DateTimeField(auto_now=True)
    status  = models.CharField(max_length=10,
                               choices=STATUS_CHOICES,
                               default='draft')
    description = models.TextField(blank=True)
    liked = models.ManyToManyField(User, related_name='likes', blank=True)



    class Meta:
        ordering = ('-publish',)

    def __str__(self):
        return self.Title

    def get_absolute_url(self):
        return reverse('upload:upload_details',
                        args=[self.id, self.Issn])

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.Title)
            super(Upload, self).save(*args, **kwargs)

    def total_likes(self) :
        return self.liked.count()       



class Comment(models.Model):
    post = models.ForeignKey(Upload, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ('created',)

    def __str__(self):
        return 'Comment added by {} for publication {}'.format(self.user, self.post)
