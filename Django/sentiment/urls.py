from django.urls import path
from .views import *

urlpatterns = [
    # 메인 페이지
    path("", index, name = "index"),
    path("analyze_sentiment/", analyze_sentiment, name = "analyze_sentiment"),
    path('emotion-list/', emotionList.as_view(), name='emotionList'),
]