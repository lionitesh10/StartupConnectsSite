from django.contrib.auth import get_user_model
from django.db import models

class Ceos(models.Model):
    firstname=models.CharField(max_length=256,blank=False,null=False)
    lastname=models.CharField(max_length=256,blank=False,null=False)
    inspirations=models.TextField(blank=False,null=False)
    favourite_quote=models.CharField(max_length=555,blank=False,null=False)
    profile_picture=models.CharField(max_length=256,blank=False,null=False)

# class FounderStories(models.Model):
#     story=models.TextField(blank=False,null=False)
#     images=models.CharField(blank=True,null=True)
#     startup_team_id=models.ForeignKey(StartupTeams,on_delete=models.CASCADE)
