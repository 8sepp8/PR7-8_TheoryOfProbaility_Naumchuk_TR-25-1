import random
import matplotlib.pyplot as m

print("========== БЛОК 1: Байєсівське оновлення (WAF/IDS) ==========")
N_values = [100, 1000, 10000, 100000, 1000000]

pH1, pH2, pH3 = 0.90, 0.08, 0.02# Апріорні ймовірності

pA_H1, pA_H2, pA_H3 = 0.01, 0.25, 0.90# Правдоподібності ознаки А

pA_theor = pH1*pA_H1 + pH2*pA_H2 + pH3*pA_H3# Теорія: Повна ймовірність P(A) та Формула Байєса P(H3|A)
pH3_given_A_theor = (pH3 * pA_H3) / pA_theor

frequencies_H3_given_A = []

print(f"{'N':<10} | {'P(H3|A) (стат)':<15} | {'P(H3|A) (теор)':<15} | {'Похибка':<15}")
print("-" * 62)

for n in N_values:
    count_A = 0
    count_H3_and_A = 0
    
    for i in range(n):
        r = random.random()# Визначаємо гіпотезу (хто відправив запит)
        if r < pH1:
            is_A = random.random() < pA_H1
            is_H3 = False
        elif r < pH1 + pH2:
            is_A = random.random() < pA_H2
            is_H3 = False
        else:
            is_A = random.random() < pA_H3
            is_H3 = True
            
        if is_A:
            count_A += 1
            if is_H3:
                count_H3_and_A += 1
                
    w_H3_given_A = count_H3_and_A / count_A if count_A > 0 else 0
    frequencies_H3_given_A.append(w_H3_given_A)
    error = abs(w_H3_given_A - pH3_given_A_theor)
    
    print(f"{n:<10} | {w_H3_given_A:<15.5f} | {pH3_given_A_theor:<15.5f} | {error:<15.5f}")

# Побудова графіка збіжності
m.figure(figsize=(8, 5))
m.plot(N_values, frequencies_H3_given_A, marker='o', color='blue', label='Статистична P(H3|A)')
m.axhline(y=pH3_given_A_theor, color='red', linestyle='--', label=f'Теорія ({pH3_given_A_theor:.4f})')
m.xscale('log')
m.xlabel('Кількість запитів (N)')
m.ylabel('Ймовірність P(H3|A)')
m.title('Блок 1: Збіжність апостеріорної ймовірності атаки')
m.legend()
m.grid(True, linestyle="--")
m.show()