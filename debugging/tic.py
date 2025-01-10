def print_board(board):
    """Tahtayı ekrana yazdırır."""
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_winner(board):
    """Kazanan olup olmadığını kontrol eder."""
    # Yatay kontrol
    for row in board:
        if row.count(row[0]) == len(row) and row[0] != " ":
            return True

    # Dikey kontrol
    for col in range(len(board[0])):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != " ":
            return True

    # Çapraz kontrol
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        return True
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
        return True

    return False

def tic_tac_toe():
    """Tic-Tac-Toe oyununu başlatır."""
    board = [[" "]*3 for _ in range(3)]  # 3x3'lük boş bir tahta
    player = "X"  # İlk oyuncu X
    moves = 0  # Hamle sayacı

    while moves < 9 and not check_winner(board):  # En fazla 9 hamle yapılabilir
        print_board(board)
        valid_move = False
        while not valid_move:
            try:
                row = int(input("Enter row (0, 1, or 2) for player " + player + ": "))
                col = int(input("Enter column (0, 1, or 2) for player " + player + ": "))
                if board[row][col] == " ":
                    board[row][col] = player
                    valid_move = True
                    moves += 1
                else:
                    print("That spot is already taken! Try again.")
            except (ValueError, IndexError):
                print("Invalid input. Please enter row and column between 0 and 2.")

        # Değişim
        if player == "X":
            player = "O"
        else:
            player = "X"

    print_board(board)
    if check_winner(board):
        print("Player " + player + " wins!")  # Son oyuncu kazanan olacak
    else:
        print("It's a draw!")  # 9 hamleden sonra kimse kazanmadıysa berabere

# Oyunu başlat
tic_tac_toe()

