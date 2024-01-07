import csv
import os

csvpath = os.path.join('Resources', 'election_data.csv')

# Open and read CSV file
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    # Skip the header row if the CSV file has one
    next(csvreader)

    # Set variables
    total_votes = 0
    candidates = {}
    max_votes = 0
    winner = ""

    # Loop through each row in CSV
    for row in csvreader:
        total_votes += 1
        candidate_name = row[2]

        if candidate_name in candidates:
            candidates[candidate_name] += 1
        else:
            candidates[candidate_name] = 1

    # Calculate percentage of votes
    percentages = {candidate: (votes / total_votes) * 100 for candidate, votes in candidates.items()}

    # Find the candidate with the most votes to declare the winner
    for candidate, votes in candidates.items():
        if votes > max_votes:
            max_votes = votes
            winner = candidate

    # Print results 
    print("Election Results")
    print("----------------------------------------")
    print(f"Total Votes: {total_votes}")
    print("----------------------------------------")
    for candidate, votes in candidates.items():
        print(f"{candidate}: {percentages[candidate]:.3f}% ({votes})")
    print("----------------------------------------")
    print(f"Winner: {winner}")
    print("----------------------------------------")
