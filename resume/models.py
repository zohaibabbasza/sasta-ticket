from django.db import models
import uuid
from resume_collector007.users.models import User

def get_file_path(instance, filename):
    ext = filename.split('.')[-1]
    filename = "%s.%s" % (uuid.uuid4(), ext)
    return filename

class SkillTag(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.name

class GeneralTag(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.name
    
class Resume(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,related_name='resume_user')
    information = models.TextField(null=True,blank=True)
    cv = models.FileField(upload_to=get_file_path)
    skill_tags = models.ManyToManyField(SkillTag,blank=True)
    general_tags = models.ManyToManyField(GeneralTag,blank=True)
    reference = models.ForeignKey(User,on_delete=models.CASCADE,
        related_name="%(class)s_reference",null=True,blank=True)

    def __str__(self) -> str:
        return self.user.email