import os
import csv
# initialize variables
total_votes = 0
winning_votes = 0
pct_votes = 0
candidates = []
votes = []

election_data_csv = os.path.join("../PyPoll/Resources", "election_data.csv")

#print(f"Path: {election_data_csv}")
#total_months = len(list(election_data_csv))
#print(f"Total Months: {total_months}")
with open(election_data_csv) as csvfile:
    csvreader = csv.reader(csvfile,delimiter=",")
    csv_header = next(csvfile)
    #print(f"Header: {csv_header}")
    
    for row in csvreader:
      #Count the votes
      total_votes += 1
      candidate_name = row[2]
      # If candidate not in candidate list add to list and add vote
      if candidate_name not in candidates:
        candidates.append(candidate_name)
        # add 1 to votes
        votes.append(1)
      else:
        candidate_index = candidates.index(candidate_name)
        votes[candidate_index] += 1 
    
print(f"Election Results")
print(f"----------------------------")
print(f"Total Votes: {total_votes}")
print(f"----------------------------")
nbr_candidates = len(candidates)
i = 0
while i < nbr_candidates:
  pct_votes = votes[i]/total_votes * 100
  print(f"{candidates[i]}: {pct_votes:.3f}% ({votes[i]})")
  # see who the winner is
  if (votes[i] > winning_votes):
    winning_votes = votes[i]
    winner = candidates[i]
  i += 1
print(f"----------------------------")
# print winning candidate
print(f"Winner: {winner}")
print(f"----------------------------")

 # Output to text file
# Specify the file to write to
output_path = os.path.join("..", "PyPoll/analysis", "results.txt")
with open(output_path, "w") as outfile:
  #csvwriter = csv.writer(csvfile)
  outfile.write(f"Election Results\n")
  outfile.write(f"----------------------------\n")
  outfile.write(f"Total Votes: {total_votes}\n")
  outfile.write(f"----------------------------\n")
  # write the candidates to the text file
  i = 0
  while i < nbr_candidates:
    pct_votes = round(votes[i]/total_votes * 100,2)
    outfile.write(f"{candidates[i]}: {pct_votes:.3f}% ({votes[i]})\n")
    i += 1
  outfile.write(f"----------------------------\n")
  # write winning candidate
  outfile.write(f"Winner: {winner}\n")
  outfile.write(f"----------------------------\n")