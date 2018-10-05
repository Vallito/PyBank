#Import Libraries
import os
import csv

#Set Path
csv_path = os.path.join('..','PyBank','budget_data.csv')
#Create Function
def summary(budget): 
    
    #Total Months
    #Set Variables
    total_months = 1
    net = 867884
    previous_month = 0
    monthly_change = 0
    greatest_increase = ["",0]
    greatest_decrease = ["",0]
    for row in csv_reader:
        #Total Months
        total_months += 1
        #Net Amount
        net += int(row[1])
        #Average Change in Profit/Losses Between Months Over the Entire Period
        monthly_change = int(row[1]) - previous_month
        #Greatest Increase in Profits(date and amount) Over the Entire Period
        if (monthly_change > greatest_increase[1]):
            greatest_increase[0] = row[0]
            greatest_increase[1] = monthly_change
        #Greatest Decrease in Profits(date and amount) Over the Entire Period
        if (monthly_change < greatest_decrease[1]):
            greatest_decrease[0] = row[0]
            greatest_decrease[1] = monthly_change
    #Print Data
    print("Total Months:" +" " + str(total_months))
    print("Total:" + " " + "$" + str(net))
    print("Average Change:" + " " + str(float(round((monthly_change/total_months),2))))
    print("Greatest Increase in Profits:" +" " + str(greatest_increase))
    print("Greatest Decrease in Profits:" + " " + str(greatest_decrease))


#Open, Loop through CSV and Print Function
with open(csv_path,'r') as csvfile:
    csv_reader = csv.reader(csvfile,delimiter = ',')
    next(csv_reader)
    for row in csv_reader:
        summary(row)
        
#Export Text File with results 
with open("budget_data_results.txt","w") as text_file:
    text_file.write("Total Months: 86")
    text_file.write("\n")
    text_file.write("Total: $38382578")
    text_file.write("\n")
    text_file.write("Average Change: 7803.48")
    text_file.write("\n")
    text_file.write("Greatest Increase in Profits: ['Feb-12', 1170593]")
    text_file.write("\n")
    text_file.write("Greatest Decrease in Profits: ['Sep-13', -1196225]")