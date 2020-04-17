import os
import csv
Resources_PyPoll = os.path.join( "Resources_PP","election_data (1).csv")
file_to_output = os.path.join("Resources_PP", "election_data.txt")

total_votes = 0
khan_votes = 0
correy_votes = 0
li_votes = 0
otooley_votes = 0
net_change_list=[]
percentage_votes_candidate= 0
total_votes_candidate= 0
most_voted = 0


with open (Resources_PyPoll) as csvfile:
    csvreader = csv.reader(csvfile)
    header =next(csvreader)

 # Calculate total number of votes cast
    for row in csvreader:
        total_votes += 1
        # print ({total_votes})
        if row[2] == "Khan": 
            khan_votes +=1
        elif row[2] == "Correy":
            correy_votes +=1
        elif row[2] == "Li": 
            li_votes +=1
        elif row[2] == "O'Tooley":
            otooley_votes +=1

candidates = ["Khan", "Correy", "Li","O'Tooley"]
votes = [khan_votes, correy_votes,li_votes,otooley_votes]

# Zip in dictonary
# Max function of the dictionary 
dict_candidates_and_votes = dict(zip(candidates,votes))
key = max(dict_candidates_and_votes, key=dict_candidates_and_votes.get)

# Percentages per candidate
khan_percent = (khan_votes/total_votes) *100
correy_percent = (correy_votes/total_votes) * 100
li_percent = (li_votes/total_votes)* 100
otooley_percent = (otooley_votes/total_votes) * 100

# Output
Output=(
    f"Election Results\n"
    f"----------------------------\n"
    f"Total Votes: {total_votes}\n"
    f"----------------------------\n"
    f"Khan: {khan_percent:.3f}% ({khan_votes})\n"
    f"Correy: {correy_percent:.3f}% ({correy_votes})\n"
    f"Li: {li_percent:.3f}% ({li_votes})\n"
    f"O'Tooley: {otooley_percent:.3f}% ({otooley_votes})\n"
    f"----------------------------\n"    
    f"Winner: {key}\n"
    f"----------------------------\n"
)
print(Output)

# Export Results
with open(file_to_output, "w") as txt_file:
    txt_file.write(Output)



















































































































