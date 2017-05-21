from django.db import models
from django.contrib.auth.models import User
from fcm_django.models import FCMDevice

class Agent(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    short_name = models.TextField(max_length=20, null=True)
    pos_latitude = models.FloatField(null=True)
    pos_longitude = models.FloatField(null=True)
    pos_speed = models.FloatField(null=True)
    pos_bearing = models.FloatField(null=True)
    pos_timestamp = models.DateTimeField(null=True)
    device = models.OneToOneField(FCMDevice, null=True, on_delete=models.CASCADE)

    def __str__(self):
        if self.short_name:
            return "({})  {}".format(self.short_name, self.user.get_full_name())
        else:
            return self.user.get_full_name()

class Group(models.Model):
    name = models.TextField(max_length=250, null=True)
    members = models.ManyToManyField(Agent)
    linked = models.ManyToManyField('self', symmetrical=False)

    class Meta:
        permissions = (
            ('read_members', 'Can read group members data'),
            ('change_members', 'Can edit group members')
        )

    def __str__(self):
        return self.name

