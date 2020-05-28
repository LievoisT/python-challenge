import os
import csv

# Creating a filepath string
filepath = os.path.join("Resources", "election_data.csv")

# Initilizing some variables
total_votes = 0
candidates = []
cand_percents = {}
cand_votes = {}
winner = ""
win_votes = 0


# Opening the election_data.csv file using csv.reader
with open(filepath) as csvfile:
    csvdata = csv.reader(csvfile)
    # Skipping the header
    next(csvdata)

    # Looping through each row of the csv
    for row in csvdata:
        total_votes += 1

        candidate = row[2]

        if candidate not in candidates:
            candidates.append(candidate)
            cand_votes[candidate] = 0
            cand_percents[candidate] = 0
        
        cand_votes[candidate] += 1

for cand in candidates:
    cand_percents[cand] = cand_votes[cand]/total_votes

    if cand_votes[cand] > win_votes:
        win_votes = cand_votes[cand]
        winner = cand

output_header = """Election Results
-----------------------------------
Total Votes: {:,}
-----------------------------------
 """.format(total_votes)

output_bulk = ""
for cand in candidates:
    output_bulk += "\n{}: {:%} ({:,})".format(cand, cand_percents[cand], cand_votes[cand])

output_footer = """
-----------------------------------
Winner: {}
-----------------------------------""".format(winner)

output_string = output_header + output_bulk + output_footer
print(output_string)

out_path = os.path.join("Analysis", "analysis.txt")
with open(out_path, mode="w") as outfile:
    outfile.write(output_string)
    
