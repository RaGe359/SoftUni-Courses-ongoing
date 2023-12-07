length = int(input())
width = int(input())
total_pieces = length * width
pieces_taken = 0

while True:
    piece = input()
    if piece == "STOP":
        print(f"{pieces_diff} pieces are left." )
        break

    piece = int(piece)
    pieces_taken += piece
    pieces_diff= abs(total_pieces - pieces_taken)

    if pieces_taken >= total_pieces:
        print(f"No more cake left! You need {pieces_diff} pieces more.")
        break