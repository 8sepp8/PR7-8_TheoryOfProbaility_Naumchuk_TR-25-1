import random
import matplotlib.pyplot as m

print("========== Блок 4 (Варіант 8): Детекція фроду ==========")
N_values = [1000, 10000, 100000, 500000, 1000000]

pH1 = 0.002   # фрод
pH2 = 0.998   # легітимна транзакція

pA_H1 = 0.40  # ознака А у фроді
pA_H2 = 0.001 # ознака А у легітимній

pA_theor = pH1*pA_H1 + pH2*pA_H2
pH1_given_A_theor = (pH1 * pA_H1) / pA_theor  # точна теорія: ~0.4449

frequencies = []

print(f"{'N':<10} | {'P(Фрод|А) (стат)':<18} | {'P (теор)':<10} | {'Похибка':<10}")
print("-" * 63)

for n in N_values:
    count_A = 0
    count_H1_and_A = 0
    
    for _ in range(n):
        is_H1 = random.random() < pH1
        
        if is_H1:
            is_A = random.random() < pA_H1
        else:
            is_A = random.random() < pA_H2
            
        if is_A:
            count_A += 1
            if is_H1:
                count_H1_and_A += 1
                
    w_H1_given_A = count_H1_and_A / count_A if count_A > 0 else 0
    frequencies.append(w_H1_given_A)
    error = abs(w_H1_given_A - pH1_given_A_theor)
    
    print(f"{n:<10} | {w_H1_given_A:<18.5f} | {pH1_given_A_theor:<10.5f} | {error:<10.5f}")

# Графік збіжності для розпізнавання фроду
m.figure(figsize=(8, 5))
m.plot(N_values, frequencies, marker='^', color='darkred', label='Симуляція P(Фрод|Ознака А)')
m.axhline(y=pH1_given_A_theor, color='black', linestyle='--', label=f'Теорія Байєса ({pH1_given_A_theor:.4f})')
m.xscale('log')
m.xlabel('Кількість транзакцій (N)')
m.ylabel('Ймовірність, що це фрод (P)')
m.title('Блок 4: Детекція фродових транзакцій (Закон великих чисел)')
m.legend()
m.grid(True, linestyle="--")
m.show()
