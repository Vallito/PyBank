#Import Libraries
import os
import csv
    
#set variables
vote_total = 1
candidates=[]
voter = []

#Set Path
election_csv = os.path.join('election_data.csv')

#Open Path
with open(election_csv,'r') as csvfile:
    #reader
    csv_reader = csv.reader(csvfile,delimiter = ',')
    #skip header
    header = next(csv_reader)
    #loop through data
    for row in csv_reader:
        #Total amount of votes
        vote_total += 1
        #Append data to variables
        candidates.append(row[2])
        voter.append(row[0])
        
#List of Candidates
candidate_list = list(set(candidates))
#Amount of Votes Candidates Recieved
votes = []
for amount in candidate_list:
    votes.append(candidates.count(amount))
        
#Print Format
print("Election Results")
print("-------------------------")
print('Votes Total' + " " + str(vote_total))
for i in range(len(candidate_list)):
    print(f"{candidate_list[i]}: {'{:.2%}'.format(votes[i]/len(voter))} ({votes[i]})")
print("-------------------------")   
print(f"Winner: {candidate_list[votes.index(max(votes))]}")

Correy = (votes[0]/vote_total*100)
Li = (votes[1]/vote_total)*100
Khan = (votes[2]/vote_total)*100
O_Tooley = (votes[3]/vote_total)*100

#Export Text File with results 
with open("election_results.txt","w") as text_file:
    text_file.write("Election Results")
    text_file.write("\n")
    text_file.write("-------------------------")
    text_file.write("\n")
    text_file.write('Votes Total' + " " + str(vote_total))
    text_file.write("\n")
   
    text_file.write(f"Correy: {Correy}")
    text_file.write("\n")
    text_file.write(f"Li: {Li}")
    text_file.write("\n")
    text_file.write(f"Khan: {Khan}")
    text_file.write("\n")
    text_file.write(f"O'Tooley: {O_Tooley}")
        
        
    #f = open('election_results.txt',"w+")
    #f.write(f"{candidate_list[i]}: {'{:.2%}'.format(votes[i]/len(voter))}")
    #f.close()
   
    text_file.write("\n")
    text_file.write("-------------------------")
    text_file.write("\n")
    text_file.write(f"Winner: {candidate_list[votes.index(max(votes))]}")