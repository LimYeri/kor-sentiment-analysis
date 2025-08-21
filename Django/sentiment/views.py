from django.shortcuts import render, redirect
from .models import Emotion
from django.db.models import Q
from django.views.generic import ListView
from django.http import JsonResponse
from .apps import SentimentConfig
import numpy as np

# # Create your views here.
def index(request):
    return render(request, "index.html")

# def emotionCreate(request):
#     if request.method == 'POST':
        
#         return redirect('emotionList')
#     else:
#         return render(request, 'index.html', {'error' : 'error'})

class emotionList(ListView):
    model = Emotion
    context_object_name = 'emotion_list'
    ordering = 'pk'
    template_name = 'emotion.html'
    paginate_by = 8

def analyze_sentiment(request):
    class_name = {0: '긍정', 1:'부정', 2:'중립'}
    
    if request.method == "POST":        
        text = request.POST['today_text']
        
        # 토크나이저로 입력 데이터를 처리
        inputs = SentimentConfig.tokenizer(text, return_tensors="tf", padding=True, truncation=True, max_length=150)
        
        # 모델로 예측 수행
        predictions = SentimentConfig.model(inputs)
        
        # 예측 결과 처리 로직 작성
        num = np.argmax(predictions.logits.numpy(), axis=-1)[0]
        result = f'당신의 오늘 기분은 \'{class_name[num]}\'입니다.'
        
        # 객체 저장
        emotion = Emotion()
        emotion.text = request.POST['today_text']
        emotion.mood = class_name[num]
        emotion.save()
        
        return render(request, 'index.html', {'result':result})
    else:
        return render(request, 'index.html', {'error' : 'error'})
