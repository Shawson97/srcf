from django.db import models
from django.conf import settings
from django.contrib.auth.models import User



class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL,
                                on_delete=models.CASCADE)
    date_of_birth = models.DateField(name='Born', blank=True, null=True)
    photo = models.ImageField(default='no_image.png', upload_to='users/%Y/%m/%d')
    city = models.CharField(max_length=50, blank=True)
    edu = models.CharField(name='Education', max_length=50, blank=True, null=True)
    bio = models.TextField(default='None', blank=True)
    work_as = models.CharField(name='Job', max_length=30, blank=True, null=True)


    def __str__(self):
        return 'User profile {}.'.format(self.user.username)

class Contact(models.Model):
    follower = models.ForeignKey(User,related_name='rel_from_set', on_delete=models.CASCADE)
    following = models.ForeignKey(User, related_name='rel_to_set', on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True, db_index=True)

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return '{} follows {}'.format(self.user_from, self.user_to)


# Add following field to User dynamically
