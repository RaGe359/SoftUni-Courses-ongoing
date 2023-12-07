price_mackerel = float(input())
price_sprat = float(input())
kg_bonito = float(input())
kg_scad = float(input())
kg_mussels = int(input())

price_bonito = price_mackerel + (price_mackerel * 0.6)
total_bonito = kg_bonito * price_bonito

price_scad = price_sprat + (price_sprat * 0.8)
total_scad = kg_scad * price_scad

total_mussels = kg_mussels * 7.50

total_price = total_bonito + total_scad + total_mussels

print(f'{total_price:.2f}')