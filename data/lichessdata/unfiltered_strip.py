import chess.pgn
import pandas as pd
import time

start_time = time.time()

# Initialize an empty list to store game data
games_data = []

# Open the PGN file
with open('test.pgn') as pgn_file:
    while True:
        game = chess.pgn.read_game(pgn_file)
        if game is None:
            break  # End of file

        # Extract headers
        headers = game.headers
        white_elo = headers.get("WhiteElo", "")
        black_elo = headers.get("BlackElo", "")
        time_control = headers.get("TimeControl", "")
        result = headers.get("Result", "")
        if white_elo.isdigit() & black_elo.isdigit():

            # Extract the game notation (moves)
            board = game.board()
            moves = []
            move_number = 1
            for move in game.mainline_moves():
                if board.turn == chess.WHITE:
                    moves.append(f"{move_number}. {board.san(move)}")
                else:
                    moves[-1] += f" {board.san(move)}"
                    move_number += 1
                board.push(move)
            game_notation = " ".join(moves)

            # Append the game data to the list
            games_data.append({
                'WhiteElo': white_elo,
                'BlackElo': black_elo,
                'TimeControl': time_control,
                'Result': result,
                'GameNotation': game_notation
        })

# Convert the list to a DataFrame
df = pd.DataFrame(games_data)
print(games_data)

# Convert Elo columns to nullable integer type (Int64)
df['WhiteElo'] = df['WhiteElo'].astype('Int16')
df['BlackElo'] = df['BlackElo'].astype('Int16')

# Save the DataFrame to a CSV file
df.to_csv('tej', index=False)

print("CSV file saved successfully!")

end_time = time.time()

# Calculate and print the elapsed time
elapsed_time = end_time - start_time
print(f"Script finished in {elapsed_time:.2f} seconds.")