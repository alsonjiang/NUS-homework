### PE 02

"""
Question 1: Auction
"""
import csv
from pprint import pprint
def read_csv(csvfilename):
  rows = []
  with open(csvfilename) as csvfile:
    file_reader = csv.reader(csvfile)
    for row in file_reader:
      rows.append(row)
  return rows[1:] #skips the heading
"""
1.1 Vickrey Auction
  Write the function to find the winner
  in a Vickrey auction
"""
#winning bidder is highest price, price to be paid is 2nd highest price
#output = (winning bid name, price)
def vickrey(bid_file: csv, title: str, item_num: int) -> (str, float):
  bidding_lst = read_csv(bid_file)
  current_bid = [] #a list of the current item's [bidders, prices]

  for bid_title, bid_item_num, bidder, bid_price in bidding_lst:
    if (bid_title == title) and (bid_item_num == str(item_num)):
      current_bid.append([bidder, bid_price])
    
  if len(current_bid) > 1: #more than one interested bidder saved
    current_bid = sorted(current_bid, key=lambda x: x[1], reverse= True) #sorts lists in descending order based on bid_price
    return (current_bid[0][0], float(current_bid[1][1]))

  return (current_bid[0][0], float(current_bid[0][1]))
  #return (highest_bidder, price_to_be_paid)
    
### Test cases (comment out or remove before copying to Coursemology)
#print(vickrey('Practical Exam 2/19-20_sem2/bid_info.csv', 'AGGREGATES, HOT MIX ASPHALT(HWYS)', 9))
#print(vickrey('Practical Exam 2/19-20_sem2/bid_info.csv', 'AGGREGATES, HOT MIX ASPHALT(HWYS)', 10))
#print(vickrey('Practical Exam 2/19-20_sem2/bid_info.csv', 'AGGREGATES, HOT MIX ASPHALT(HWYS)', 13))


"""
1.2 Successful Companies
  Write the function to find all
  successful companies
"""
#for each project, success = most no. of win on items
#dict = {
#       'TITLE': {COMPANY_1, COMPANY_2, etc}        
#       }
def success(bid_file: csv) -> dict:
  companies = {}
  count = 0 #count wins

  bidding_lst = read_csv(bid_file)
  for bid_title, bid_item_num, bidder, bid_price in bidding_lst:
    if bidder not in companies:
      companies[bidder]

  return companies
    
  

### Test cases (comment out or remove before copying to Coursemology)
print(success('Practical Exam 2/19-20_sem2/small_bid_info.csv'))
