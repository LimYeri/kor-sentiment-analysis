# 🎬 Sentiment Analysis Web

문장을 입력하면 **긍정 / 부정 / 중립**을 판단하는 한국어 감성 분석 프로젝트입니다.  
백엔드는 **Django**, 프론트엔드는 **HTML, CSS, JavaScript**로 구성하였으며,  
학습 모델은 **KLUE/BERT-base**를 Fine-tuning하여 사용했습니다.

- **개발 시기**: 2024.02

---

## 📂 데이터 준비

### 1. 사용한 데이터셋
- **[NSMC (Naver Sentiment Movie Corpus v1.0)](https://github.com/Huffon/pytorch-sentiment-analysis-kor/tree/master/data)**
- **[AI HUB 한국어 감정 대화 데이터셋](https://aihub.or.kr/aihubdata/data/view.do?dataSetSn=270)**
- **[AI HUB 한국어 감정 대화 데이터셋 2](https://aihub.or.kr/aihubdata/data/view.do?dataSetSn=271)**  

### 2. 전처리 과정
- 감정 태깅 기준:
  - 긍정: 행복  
  - 부정: 분노, 혐오  
  - 중립: 중립  
  - → 슬픔, 공포, 놀람은 제외

- 데이터 통합 후 라벨별 개수:
  - 부정 114,361
  - 긍정 106,239
  - 중립 48,611

- 데이터 불균형 해결을 위해 **NSMC 데이터에서만 언더샘플링 진행**
- 최종 `mrus_data` (학습 데이터셋)
  - 긍정 48,611
  - 부정 48,611
  - 중립 48,611


---

## 🤖 모델 학습

### 1. 사용 모델
- **KLUE/BERT-base**
- 라벨 인코딩: `label encoding` 방식
- 분류 클래스: 긍정 / 부정 / 중립 (3가지)

### 2. 성능
- 학습 데이터: `mrus_data`
- Epoch: 7
- Accuracy: **0.86**

### 3. 앙상블 시도
- 투표 기반 앙상블: Accuracy 0.8721
- 단순 평균 앙상블: Accuracy 0.8637  
(최종 서비스에는 단일 모델 `first_klue` 사용)

---

## 🌐 웹 서비스 구조

### Backend
- **Django**
- 학습된 모델 로드

### Frontend
- **HTML, CSS, JavaScript**
- 간단한 입력창과 출력 UI 구성

---

## 📸 실행 화면

### 메인 페이지
<img width="1440" height="686" alt="Image" src="https://github.com/user-attachments/assets/1a33851b-4e5e-479e-8957-f085df283f4b" />

### 텍스트 입력
<img width="1440" height="686" alt="Image" src="https://github.com/user-attachments/assets/67f586c4-6c5c-4da4-8b76-40f3af85e947" />

### 감성 클래스 출력
<img width="1440" height="689" alt="Image" src="https://github.com/user-attachments/assets/30449e90-4d41-4894-9857-35b45d61eb19" />

### 감정 기록 보기
<img width="1440" height="687" alt="Image" src="https://github.com/user-attachments/assets/b8ccdc25-3aba-4181-bc29-54297deb43c8" />
