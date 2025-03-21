import pandas as pd

# Load the CSV file
input_csv = r'C:\Users\Helena\Documents\GitHub\schackgpt\schack_1_oordning.csv'  # Replace with your CSV file path
output_csv = 'filtered_chess_games.csv'  # Output file path

# Define the Elo range (e.g., 1500-1600 or 1800-max)
min_elo = 1500  # Minimum Elo
max_elo = 1600  # Maximum Elo (use a very high number for "max")

# Read the CSV file
df = pd.read_csv(input_csv)

# Filter rows based on Elo range
filtered_df = df[(df['WhiteElo'] >= min_elo) & (df['WhiteElo'] <= max_elo) &
                (df['BlackElo'] >= min_elo) & (df['BlackElo'] <= max_elo)]

# Save the filtered data to a new CSV file
filtered_df.to_csv(output_csv, index=False)

print(f"Filtered data saved to {output_csv}")