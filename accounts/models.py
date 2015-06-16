from django.contrib.auth.models import User
from django.db import models


class UserProfile(models.Model):
    user = models.ForeignKey(User)
    work_place = models.CharField('勤務先', default='東京本社', max_length=512) # TODO 勤務先マスタ作る
    work_status = models.CharField('勤務形態', default='在席', max_length=512) #  TODO 勤務形態マスタ作る
    division = models.IntegerField('所属コード', default=0) #  TODO 所属コードマスタ作る
    accept_question = models.IntegerField('受信可', default=1) # 0:不可, 1:可