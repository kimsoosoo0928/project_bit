'''
import django
django.setup()
from django.db import models
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project.settings")


class CrimeVO(models.Model): # 데이터베이스에서 데이터를 받아온다. 엔티티
    police = models.TextField() #어트리뷰트
    crime = models.TextField()
    create_at = models.DateTimeField()

class CrimeDTO(DataTransferObject): #DTO는 리액트에서 데이터를 받아온다. 오브젝트
    police = '' #프로퍼티
    crime = ''
    create_at = ''
'''