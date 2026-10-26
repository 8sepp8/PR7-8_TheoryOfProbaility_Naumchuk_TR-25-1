import random

print("========== Блок 2 (Варіант 3): Джерела веб-трафіку ==========")
N = 100000

pH1, pH2, pH3 = 0.40, 0.40, 0.20# Апріорні ймовірності каналів (H1 - Прямий, H2 - Органіка, H3 - Реклама)
pC_H1, pC_H2, pC_H3 = 0.05, 0.02, 0.10# Правдоподібності покупки C

pC_theor = pH1*pC_H1 + pH2*pC_H2 + pH3*pC_H3
pH3_given_C_theor = (pH3 * pC_H3) / pC_theor

count_C = 0
count_H3_and_C = 0

for i in range(N):
    r = random.random()
    if r < pH1:
        is_C = random.random() < pC_H1
        is_H3 = False
    elif r < pH1 + pH2:
        is_C = random.random() < pC_H2
        is_H3 = False
    else:
        is_C = random.random() < pC_H3
        is_H3 = True
        
    if is_C:
        count_C += 1
        if is_H3:
            count_H3_and_C += 1

w_C = count_C / N
w_H3_given_C = count_H3_and_C / count_C if count_C > 0 else 0

print(f"Симуляцій: {N}")
print(f"Повна ймовірність конверсії P(C): Теорія = {pC_theor:.4f}, Статистика = {w_C:.4f}")
print(f"Апостеріорна ймовірність реклами P(H3|C): Теорія = {pH3_given_C_theor:.4f}, Статистика = {w_H3_given_C:.4f}")
print(f"Абсолютна похибка P(H3|C): {abs(w_H3_given_C - pH3_given_C_theor):.5f}")
