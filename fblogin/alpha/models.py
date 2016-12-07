from __future__ import unicode_literals
from allauth.socialaccount.models import SocialAccount
import hashlib


# to make the user's email-verification status available to the template via request.user.profile.account_verified




from django.contrib.auth.models import User
from django.db import models
from allauth.account.models import EmailAddress

from django.utils import timezone

try:
    from django.utils.encoding import force_text
except ImportError:
    from django.utils.encoding import force_unicode as force_text


# Create your models here.

# to make the user's email-verification status available to the template via request.user.profile.account_verified

# Create your models here.


def profile_image_url(self):
    fb_uid = SocialAccount.objects.filter(user_id=self.user.id, provider='facebook')

    if len(fb_uid):
        return "http://graph.facebook.com/{}/picture?width=40&height=40".format(fb_uid[0].uid)

    return "http://www.gravatar.com/avatar/{}?s=40".format(hashlib.md5(self.user.email).hexdigest())


class Question(models.Model):
    question_text = models.CharField(max_length=200)


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)



class UserProfile(models.Model):
    user = models.OneToOneField(User, primary_key=True, verbose_name='user', related_name='profile')
    avatar_url = models.CharField(max_length=256, blank=True, null=True)

    def __str__(self):
        return force_text(self.user.email)


    class Meta():
        db_table = 'user_profile'

    def __unicode__(self):
        return "{}'s profile".format(self.user.username)

    class Meta:
        db_table = 'user_profile'

    def account_verified(self):
        if self.user.is_authenticated:
            result = EmailAddress.objects.filter(email=self.user.email)
            if len(result):
                return result[0].verified
        return False

    def profile_image_url(self):
        fb_uid = SocialAccount.objects.filter(user_id=self.user.id, provider='facebook')

        if len(fb_uid):
            return "http://graph.facebook.com/{}/picture?width=40&height=40".format(fb_uid[0].uid)

        # url = "http://graph.facebook.com/%s/picture?type=large" % response['id']
        # avatar = urlopen(url)
        # profile = user.get_profile()
        # profile.profile_photo.save(slugify(user.username + " social") + '.jpg',
        #                         ContentFile(avatar.read()))
        # profile.save()
        #
        # {{user.socialaccount_set.all.0.get_avatar_url}}
        # {{user.socialaccount_set.all.0.uid}}

        return "http://www.gravatar.com/avatar/{}?s=40".format(hashlib.md5(self.user.email).hexdigest())

User.profile = property(lambda u: UserProfile.objects.get_or_create(user=u)[0])


class Post(models.Model):
    author = models.ForeignKey('auth.User')  # a link to another model.
    title = models.CharField(max_length=200)  # define text with a limited number of characters
    text = models.TextField()  # long text without a limit. sounds ideal for blog post content
    created_date = models.DateTimeField(default=timezone.now)  # date and time
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title


