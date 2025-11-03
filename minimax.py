import math

# Kontrolliert wer gewonnen hat (kann auch unentschieden sein)
def check_winner(board):
    wins = [(0,1,2), (3,4,5), (6,7,8),
            (0,3,6), (1,4,7), (2,5,8),
            (0,4,8), (2,4,6)]
    for a,b,c in wins:
        if board[a] != " " and board[a] == board[b] == board[c]:
            return board[a]
    if " " not in board:
        return "draw"
    return None

# Minimax-Algo
node_counter = 0

def minimax(board, is_maximizing):
    global node_counter
    node_counter += 1

    winner = check_winner(board)
    if winner == "X": return 1
    if winner == "O": return -1
    if winner == "draw": return 0

    if is_maximizing:
        best = -math.inf
        for i in range(9):
            if board[i] == " ":
                board[i] = "X"
                value = minimax(board, False)
                board[i] = " "
                best = max(best, value)
        return best
    else:
        best = math.inf
        for i in range(9):
            if board[i] == " ":
                board[i] = "O"
                value = minimax(board, True)
                board[i] = " "
                best = min(best, value)
        return best


# Ausgabe
board = [" ", " ", " ", " ", " ", " ", " ", " ", " "]   # Spielfeld leer generieren
result = minimax(board, True)
print("Startzustandsbewertung:", result)
print("Besuchte Knoten:", node_counter)

node_counter_pruning = 0

def minimax_pruning(board, is_maximizing, alpha=-math.inf, beta=math.inf):
    global node_counter_pruning
    node_counter_pruning += 1

    winner = check_winner(board)
    if winner == "X": return 1
    if winner == "O": return -1
    if winner == "draw": return 0

    if is_maximizing:
        best = -math.inf
        for i in range(9):
            if board[i] == " ":
                board[i] = "X"
                value = minimax_pruning(board, False, alpha, beta)
                board[i] = " "
                best = max(best, value)
                alpha = max(alpha, best)
                if beta <= alpha:
                    break  # Prune
        return best
    else:
        best = math.inf
        for i in range(9):
            if board[i] == " ":
                board[i] = "O"
                value = minimax_pruning(board, True, alpha, beta)
                board[i] = " "
                best = min(best, value)
                beta = min(beta, best)
                if beta <= alpha:
                    break
        return best

# Ausgabe
board = [" ", " ", " ", " ", " ", " ", " ", " ", " "]   # Spielfeld leer generieren
result = minimax_pruning(board, True)
print("Startzustandsbewertung:", result)
print("Besuchte Knoten:", node_counter_pruning)

# Vergleich
board = ["X", "O", "X", "O", " ", " ", " ", " ", " "]

node_counter = 0
score_plain = minimax(board, True)

node_counter_pruning = 0
score_pruning = minimax_pruning(board, True)

print("Minimax-Ergebnis:", score_plain, "Knoten:", node_counter)
print("Alpha-Beta-Ergebnis:", score_pruning, "Knoten:", node_counter_pruning)
