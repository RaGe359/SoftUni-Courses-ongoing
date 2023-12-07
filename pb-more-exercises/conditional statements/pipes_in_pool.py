V = int(input())
P1 = int(input())
P2 = int(input())
H = float(input())

pipe1 = P1 * H
pipe2 = P2 * H
total_pipes = pipe1 + pipe2
overflowed = abs(V - total_pipes)
pipe1_perc = pipe1 / total_pipes * 100
pipe2_perc = pipe2 / total_pipes * 100
total_perc = total_pipes / V * 100

if total_pipes <= V:
    print(f"The pool is {total_perc:.2f}% full. Pipe 1: {pipe1_perc:.2f}%. Pipe 2: {pipe2_perc:.2f}%.")
else:
    print(f"For {H:.2f} hours the pool overflows with {overflowed:.2f} liters.")