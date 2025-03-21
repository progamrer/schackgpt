import pandas as pd
import time

start_time = time.time()

game_list = []

def parse_pgn(file_path):
    with open(file_path, 'r') as pgn_file:
        line_counter = 0
        game_data = {}


        for line in pgn_file:
            line_counter +=1 
            
            # Skip the first 4 lines of each game
            if line_counter <= 4:
                #print(line)
                continue

            # Save the 5th line
            if line_counter == 5:
                #print(line,line_counter)
                temp = head_parser(line,{})
                #print(temp)

            # Skip 2 lines after the 5th line
            if 6 <= line_counter <= 7:
                #print(line)
                continue

            # Save the 8th and 9th lines
            if line_counter == 8 or line_counter == 9:
                #print(line,line_counter)
                head_parser(line,game_data)

            # Skip 2 lines after the 9th line
            if 10 <= line_counter <= 13:
                #print(line)
                continue

            # Save the 14th line
            if line_counter == 14:
                #print(line,line_counter,"tja")
                key_value = line[1:-1].split(' ', 1)
                key = key_value[0]
                if key == "TimeControl":
                    value = key_value[1].strip('"')  # Remove quotes from the value
                    value = value.rstrip(']').rstrip('"')
                    #print(game_data)
                    #print(temp)
                    game_data[key] = value
                    game_data.update(temp)
                else:
                    find_next_event_line(pgn_file)
                    #print(f"Skipping bajs line: {line}")  # Log malformed lines
                    #print(game_data)
                    game_data = {}
                    #print(game_data,"sap")
                    line_counter = 1
                    continue

            if 15 <= line_counter <= 16:
                #print(line)
                continue

            if line_counter == 17:
                try:
                    linj = line.rstrip().removesuffix(game_data['Result']).rstrip()
                    #print(linj)
                    #print(game_data)
                    #print(game_data['Result'])
                    game_data.update({'GameNotation':linj})
                    #print(game_data)
                    game_list.append(game_data.copy())  # Append a COPY of game_data
                    
                except KeyError:
                    pass
                temp = {}
                game_data = {}
                line_counter = -1

    #print(game_data)
    #print(game_list)

def head_parser(linj,game):
    key_value = linj[1:-1].split(' ', 1)
    if len(key_value) == 2:  # Ensure the line is properly formatted
        key = key_value[0]
        value = key_value[1].strip('"')  # Remove quotes from the value
        value = value.rstrip(']').rstrip('"')
        game[key] = value
        return game
        

def find_next_event_line(file):
    """
    A helper function to read lines from the file until a line starting with [Event is found.
    """
    for line in file:
        stripped_line = line.strip()
        #print(stripped_line)
        if stripped_line.startswith("[Event"):
            return stripped_line
    return None  # Return None if no [Event line is found

# Usage
parse_pgn('lichess_db_standard_rated_2017-02.pgn')
df = pd.DataFrame(game_list)

# Save the DataFrame to a CSV file
df.to_csv('mej', index=False)

print("CSV file saved successfully!")

end_time = time.time()

# Calculate and print the elapsed time
elapsed_time = end_time - start_time
print(f"Script finished in {elapsed_time:.2f} seconds.")

