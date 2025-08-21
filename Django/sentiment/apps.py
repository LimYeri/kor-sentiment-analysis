from django.apps import AppConfig
import tensorflow as tf
from transformers import TFAutoModelForSequenceClassification, AutoTokenizer
import os


class SentimentConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'sentiment'
    model = None  # 모델 객체를 저장할 클래스 변수를 정의합니다.
    tokenizer = None  # 토크나이저 객체를 저장할 클래스 변수
    
    def ready(self):
        # Django 서버가 시작할 때 모델을 로드합니다.
        super().ready()
        model_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'first_klue_model_and_tokenizer')
        # 모델 로드
        SentimentConfig.model = TFAutoModelForSequenceClassification.from_pretrained(model_path)
        # 토크나이저 로드
        SentimentConfig.tokenizer = AutoTokenizer.from_pretrained(model_path)

