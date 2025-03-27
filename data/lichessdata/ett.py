import re
import csv

with open("lichess_db_standard_rated_2017-02.pgn", "r") as f:
    content = f.read()

pattern = r'[\s\S]*?\[Result\s+"([^"]*)"\][\s\S]*?\[WhiteElo\s+"([^"]*)"\][\s\S]*?\[BlackElo\s+"([^"]*)"\][\s\S]*?\[TimeControl\s+"([^"]*)"\][\s\S]*?(1\..*) .*'
#print(re.sub(pattern, r"\2,\3,\4,\1,\5\n",content))

matches = re.findall(pattern, content)

# Write to CSV
with open("telf.csv", "w", newline="") as csvfile:
    writer = csv.writer(csvfile)
    # Write headers
    writer.writerow(["WhiteElo", "BlackElo", "TimeControl", "Result", "GameNotation"])
    # Write data
    for match in matches:
        writer.writerow([match[1], match[2], match[3], match[0], match[4].strip()])