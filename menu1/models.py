from django.db import models

# Create your models here.

class Menu(models.Model):
    # 칼럼명 = 데이터 자료형
    제목 = models.CharField(max_length=255, blank=False, null=False)
    작성자 = models.CharField(max_length=255, blank=False, null=False)
    내용 = models.TextField(null=False)
    작성일 = models.DateTimeField(null=False)
    수정일 = models.DateTimeField(null=False)
    조회수 = models.IntegerField(null=False)
    # default : 객체 새엇ㅇ할 때 기본값
    댓글수 = models.IntegerField(null=False, default=0)
    좋아요 = models.IntegerField(null=False, default=0)
    싫어요 = models.IntegerField(null=False, default=0)

    def __str__(self):
        return self.제목
    
class Reply(models.Model):
    # 작성자, 작성일자, 내용, borderId
    menu_id = models.IntegerField(null=False)
    작성자 = models.CharField(max_length=255, null=False)
    작성일 = models.DateField(null=False)
    내용 = models.CharField(max_length=255)