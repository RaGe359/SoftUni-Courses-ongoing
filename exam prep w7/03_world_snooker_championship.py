stage = input()
ticket_type = input()
ticket_amt = int(input())
picture = input()
ticket_price = 0
total_price = 0

if stage == "Quarter final":
    if ticket_type == "Standard":
        ticket_price = 55.50
    elif ticket_type == "Premium":
        ticket_price = 105.20
    elif ticket_type == "VIP":
        ticket_price = 118.90
elif stage == "Semi final":
    if ticket_type == "Standard":
        ticket_price = 75.88
    elif ticket_type == "Premium":
        ticket_price = 125.22
    elif ticket_type == "VIP":
        ticket_price = 300.40
elif stage == "Final":
    if ticket_type == "Standard":
        ticket_price = 110.10
    elif ticket_type == "Premium":
        ticket_price = 160.66
    elif ticket_type == "VIP":
        ticket_price = 400

price = ticket_price * ticket_amt
if price > 4000:
    total_price = price * 0.75
elif 2500 < price <= 4000:
    total_price = price * 0.9
    if picture == "Y":
        total_price += ticket_amt * 40
else:
    total_price = price
    if picture == "Y":
        total_price += ticket_amt * 40

print(f'{total_price:.2f}')