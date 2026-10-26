import random

print("========== Блок 3: Наївний байєсівський класифікатор ==========")
N = 10000

p_Spam = 0.30# Параметри моделі
p_Ham = 0.70

pw1_Spam, pw2_Spam = 0.80, 0.60# ймовірності слів w1 та w2 для кожного класу
pw1_Ham, pw2_Ham = 0.05, 0.10


TP, FP, TN, FN = 0, 0, 0, 0 # mатриця помилок

for i in range(N):
    actual_spam = random.random() < p_Spam# Генерація фактичного класу повідомлення
    
    if actual_spam:#Генерація ознак (наявність слів w1 та w2)
        x1 = 1 if random.random() < pw1_Spam else 0
        x2 = 1 if random.random() < pw2_Spam else 0
    else:
        x1 = 1 if random.random() < pw1_Ham else 0
        x2 = 1 if random.random() < pw2_Ham else 0
        
    # згладжування не застосовуємо, оскільки ймовірності не нульові
    prob_X_Spam = (pw1_Spam if x1 else 1 - pw1_Spam) * (pw2_Spam if x2 else 1 - pw2_Spam)
    score_Spam = p_Spam * prob_X_Spam
    
    prob_X_Ham = (pw1_Ham if x1 else 1 - pw1_Ham) * (pw2_Ham if x2 else 1 - pw2_Ham)
    score_Ham = p_Ham * prob_X_Ham
    
    pred_spam = score_Spam > score_Ham    # прогнозований клас
    
    if actual_spam and pred_spam:
        TP += 1
    elif not actual_spam and pred_spam:
        FP += 1
    elif not actual_spam and not pred_spam:
        TN += 1
    elif actual_spam and not pred_spam:
        FN += 1

#oбчислення метрик
accuracy = (TP + TN) / N
precision = TP / (TP + FP) if (TP + FP) > 0 else 0
recall = TP / (TP + FN) if (TP + FN) > 0 else 0
f1_score = 2 * precision * recall / (precision + recall) if (precision + recall) > 0 else 0

print("Матриця помилок (Confusion Matrix):")
print(f"TP (True Spam): {TP} \t FP (False Spam): {FP}")
print(f"FN (Missed Spam): {FN} \t TN (True Ham): {TN}")
print("-" * 40)
print(f"Accuracy:  {accuracy:.4f}")
print(f"Precision: {precision:.4f}")
print(f"Recall:    {recall:.4f}")
print(f"F1-score:  {f1_score:.4f}")
