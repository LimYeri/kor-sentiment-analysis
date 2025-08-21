from django.db import models

# Create your models here.
class Emotion(models.Model):
    # 글
    text = models.TextField()
    # 작성시간
    created_at = models.DateTimeField(auto_now_add=True)
    # 감성
    mood = models.CharField(max_length=20, blank=True, null=True)
    
    class Meta:
        db_table = 'Emotions'
    
    def __str__(self):
        return self.text