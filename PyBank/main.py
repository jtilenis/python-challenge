import os
import csv
# initialize variables
monthNbr = 0
total_amt = 0
profit_change = 0
sum_profit_change = 0
current_month_profit = 0
prior_month_profit = 0
max_profit = 0
min_profit = 0
budget_data_csv = os.path.join("../PyBank/Resources", "budget_data.csv")
# Specify the file to write to
output_path = os.path.join("..", "PyBank/analysis", "results.csv")

with open(budget_data_csv) as csvfile:
    csvreader = csv.reader(csvfile,delimiter=",")
    csv_header = next(csvfile)
   
    for row in csvreader:
      # Count Months
      monthNbr += 1
      total_amt = total_amt + int(row[1])
      if (monthNbr == 1):
        prior_month_profit = int(row[1])
      if (monthNbr > 1):
      # Monthly change in Profiit/Loss
        current_month_profit = int(row[1])
        profit_change = current_month_profit - prior_month_profit
      # Keep running total of profit_change
        sum_profit_change = sum_profit_change + profit_change
        prior_month_profit = int(row[1])
        
      # Record max profit
      if (profit_change > max_profit):
        max_month = row[0]
        max_profit = profit_change
      # Record min profit
      if (profit_change < min_profit):
       min_month = row[0]
       min_profit = profit_change
    #Average change in profit
    avg_change = sum_profit_change / (monthNbr - 1)
    
    # Print to terminal
    print(f"Financial Analysis")
    print(f"----------------------------")
    print(f"Total Months: {monthNbr}")
    print(f"Total: ${total_amt}")
    print(f"Average Change: ${round(avg_change,2)}")
    print(f"Greatest Increase in Profits: {max_month} (${max_profit})")
    print(f"Greatest Decrease in Profits: {min_month} (${min_profit})")

    # Output to text file
    with open(output_path, "w") as outfile:
    #csvwriter = csv.writer(csvfile)
      outfile.write(f"Financial Analysis\n")
      outfile.write(f"----------------------------\n")
      outfile.write(f"Total Months: {monthNbr}\n")
      outfile.write(f"Total: ${total_amt}\n")
      outfile.write(f"Average Change: ${round(avg_change,2)}\n")
      outfile.write(f"Greatest Increase in Profits: {max_month} (${max_profit})\n")
      outfile.write(f"Greatest Decrease in Profits: {min_month} (${min_profit})\n")
       
    
