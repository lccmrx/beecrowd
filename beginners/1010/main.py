total_price = 0

for i in range(0,2):
    _, qtd, unit_price = input().split(" ")
    total_price += int(qtd) * float(unit_price)
    
print(f"VALOR A PAGAR: R$ {total_price:.2f}")
