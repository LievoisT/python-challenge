import os
import csv


csvpath = os.path.join("Resources", "budget_data.csv")
months = 0
total_profits = 0
pl = 0
pl_change = 0
total_pl_change = 0
avg_pl_change = 0
profit_inc = ["", 0]
profit_dec = ["", 0]
output_string = ""

with open(csvpath) as csvfile:
    reader = csv.reader(csvfile)
    next(reader)
    
    for row in reader:
        months += 1
        total_profits = total_profits + float(row[1])
        if pl != 0:
            pl_change = float(row[1]) - pl
        total_pl_change += pl_change
        pl = float(row[1])

        if pl_change > profit_inc[1]:
            profit_inc = [row[0], pl_change]
        
        if pl_change < profit_dec[1]:
            profit_dec = [row[0], pl_change]

    avg_pl_change = total_pl_change/months
        
#    output_string = """Financial Analysis \n---------------------\nTotal Months: {}\nTotal: ${:,}
#    """.format(months, total_profits)

    output_string = """Financial Analysis
--------------------------------
Total Moths: {}
Total: ${:,}
Average Change: ${:-,}
Greatest Increase in Profits: {} (${:-,})
Greatest Decrease in Profits: {} (${:-,})
    """.format(months, total_profits, round(avg_pl_change, 2),
    profit_inc[0], profit_inc[1], profit_dec[0], profit_dec[1])

print(output_string)

output_path = os.path.join("Analysis", "analysis.txt")
with open(output_path, mode="w") as outfile:
    outfile.write(output_string)


