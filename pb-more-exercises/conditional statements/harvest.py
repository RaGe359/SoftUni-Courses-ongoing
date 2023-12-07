import math

loze = int(input())
grapes_m2 = float(input())
needed_litres = int(input())
workers_amt = int(input())

rekolta = loze * 0.4
kg_grapes = rekolta * grapes_m2
wine_l = kg_grapes / 2.5
diff = abs(wine_l - needed_litres)
wine_pp = diff / workers_amt

if wine_l < needed_litres:
    print(f"It will be a tough winter! More {math.floor(diff)} liters wine needed.")
else:
    print(f'Good harvest this year! Total wine: {math.floor(wine_l)} liters.')
    print(f'{math.ceil(diff)} liters left -> {math.ceil(wine_pp)} liters per person.')