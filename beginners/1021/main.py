import re

def main():
    # p1, p2 = input().split(".") # User's Input splitted by the floating point
    # p1, p2 = int(p1), int(p2) # Convert to int
    
    p1, p2 = 576, 73
    
    money = {
        "nota(s)": {
            100: 0,
            50: 0,
            20: 0,
            10: 0,
            5: 0,
            2: 0,                
        },
        "moeda(s)": {
            1: 0,
            .5: 0,
            .25: 0,
            .1: 0,
            .05: 0,
            .01: 0,
        }
    }
    
    for money_type, amounts in money.items():
        print_money_type = re.sub('[\\(\\)]', '', money_type.upper())
        print(f"{print_money_type}:")
        for amount, qtd in amounts.items():
            if amount > 1:
                multiplier = 1
                val = p1
            else:
                multiplier = 10
                val = p2 + p1
            val //= amount * multiplier
            qtd += val % amount
                
            money[money_type][amount]
            print(f"{qtd} {money_type} de R$ {amount:.2f}")
    
if __name__ == '__main__':
    main()
