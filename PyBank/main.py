import os
import csv

csvpath = os.path.join('Resources', 'budget_data.csv')

# Open and read CSV file
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    
    # Skip the header row if the CSV file has one
    next(csvreader)
    
    #Initalize variables
    months = 0
    total = 0
    prev_revenue = 0  
    total_change = 0  
    greatest_increase = {"date": "", "amount": float("-inf")}
    greatest_decrease = {"date": "", "amount": float("inf")}

    #Loop through rows in CSV file and calculate toal profit/loss
    for row in csvreader:
        months += 1
        revenue = int(row[1])
        total += revenue
        
        #Calculate change in profit/loss
        if months > 1:
            change = revenue - prev_revenue
            total_change += change

            if change > greatest_increase["amount"]:
                greatest_increase["date"] = row[0]
                greatest_increase["amount"] = change

            if change < greatest_decrease["amount"]:
                greatest_decrease["date"] = row[0]
                greatest_decrease["amount"] = change
        
        #Update previous revenue for the next iteration
        prev_revenue = revenue

# Calculate average change
average_change = total_change / (months - 1) if months > 1 else 0

#Print the results
print("Financial Analysis")
print("------------------------------------------------")
print(f"Total Months: {months}")
print(f"Total: ${total}")
print(f"Average Change: ${average_change:.2f}")
print(f"Greatest Increase in Profits: {greatest_increase['date']} (${greatest_increase['amount']})")
print(f"Greatest Decrease in Profits: {greatest_decrease['date']} (${greatest_decrease['amount']})")
