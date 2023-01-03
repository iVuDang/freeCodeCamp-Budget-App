# PART A - Complete the Category class in budget.py.  to instantiate objects based on different budget categories like food, clothing, and entertainment. When objects are created, they are passed in the name of the category. The class should have an instance variable called ledger that is a list.

class Category: 
  def __init__(self, category):
    self.category = category
    self.ledger = []
    self.balance = []
    # can use accumulator variable '+=', or list & sum(list), the latter keeps a nicer documentation trair, and for debugging / print 

  # A deposit method that accepts an amount and description. If no description is given, it should default to an empty string. The method should append an object to the ledger list in the form of {"amount": amount, "description": description}.

  def deposit(self, amount, description = '') -> None: 
  # description = '' defaults to empty string, used for 'optional' arguments
    deposit_dict = {"amount": amount, "description": description}
    self.ledger.append(deposit_dict)
    self.balance.append(amount) 
    
  # A get_balance method that returns the current balance of the budget category based on the deposits and withdrawals that have occurred.
  def get_balance(self) -> float:
    return sum(self.balance)
    
  # A check_funds method that accepts an amount as an argument. It returns False if the amount is greater than the balance of the budget category and returns True otherwise. This method should be used by both the withdraw method and transfer method.

  def check_funds(self, amount) -> bool:
    return (amount <= self.get_balance())

  # A withdraw method that is similar to the deposit method, but the amount passed in should be stored in the ledger as a negative number. If there are not enough funds, nothing should be added to the ledger. This method should return True if the withdrawal took place, and False otherwise.
  def withdraw(self, amount, description = '') -> bool:
    if (self.check_funds(amount)):
      withdraw_dict = {"amount": amount * -1, "description": description}
      self.ledger.append(withdraw_dict)
      self.balance.append(amount * -1)
      return True
    else: 
      return False

  # A transfer method that accepts an amount and another budget category as arguments. The method should add a withdrawal with the amount and the description "Transfer to [Destination Budget Category]". The method should then add a deposit to the other budget category with the amount and the description "Transfer from [Source Budget Category]". If there are not enough funds, nothing should be added to either ledgers. This method should return True if the transfer took place, and False otherwise.
  def transfer(self, amount, to_category) -> bool:
    if (self.check_funds(amount)):
      self.withdraw(amount, f'Transfer to {to_category.category}')
      to_category.deposit(amount, "Transfer from " + self.category)
      return True
    else:
      return False
    # Can use f'strings' or string concat 
      
    # self.withdraw(amount, f'Transfer to {to_category.category}')
    # self.withdraw refers to our current category, applied withdraw function to it, to_category.category refers to the new instantized category from our parameter, and .category initializes it through our __init__ function
      
    # to_category.deposit(amount, "Transfer from " + self.category)
    # to_category refers to our instantized category from our parameter, we apply the deposit function to it, self.category refers to our previous state
      
    # Food = Category('Food')
    # Food.transfer(50, 'Clothing') 
    # self.withdraw refers to Food, and to_category.deposit refers to Clothing.deposit


# When the budget object is printed it should display
# A title line of 30 characters where the name of the category is centered in a line of * characters.
# A list of the items in the ledger. Each line should show the description and amount. 
# The first 23 characters of the description should be displayed, then the amount. The amount should be right aligned, contain two decimal places, and display a maximum of 7 characters.
# A line displaying the category total.

  def __str__(self):
    object_string = self.category.center(30, '*') + '\n'
    
    for item_object in self.ledger: 
      object_string += f"{item_object['description'][:23]:23}{item_object['amount']:>7.2f}\n"
      # item_object['description'] calls on the key, and returns the value.
      # [:23] slices first 23 characters. :23 display max 23 
      # :>7.2f right aligns amount, displays max 7, and 2 decimal places. 
      # 23 + 7 = 30 total characters    
    object_string += "Total: " + str(self.get_balance())
    # this is outside the for loop, and will add/accumulate last 
    return object_string

      
Food = Category('Food')
Food.deposit(1000, 'initial deposit')
Food.withdraw(10.15, 'groceries')
Food.withdraw(15.89, 'restaurant and more food')
# Food.transfer(50, 'Clothing') - DOESN'T WORK??? 
print(Food)


print('\n')
Clothing = Category('Clothing')
Clothing.deposit(500, 'initial deposit')
Clothing.withdraw(20, 'vuori')
Clothing.withdraw(30, 'mec')
print(Clothing)


"""
Here is an example of the output:

*************Food*************
initial deposit        1000.00
groceries               -10.15
restaurant and more foo -15.89
Transfer to Clothing    -50.00
Total: 923.96
"""


# PART B - create a function (outside of the class) called create_spend_chart that takes a list of categories as an argument. It should return a string that is a bar chart.

def create_spend_chart(categories) -> str:

  spend_list = []

  for category in categories:
    neg_amounts = 0
    for item in category.ledger:
      if item['amount'] < 0:
        neg_amounts += abs(item['amount'])
    spend_list.append(neg_amounts)
        
  print(spend_list)
  # [26.04, 50]
  # 26.04 is from Food, 50 is from Clothing
  
  total_spend = sum(spend_list)
  print(total_spend)
  # 76.03999999999999

  percent_list = [((item/total_spend) * 100) for item in spend_list]

  print(percent_list)
  # [34.24513413992636, 65.75486586007365]
  
  # Use for loop within a for loop, to create a grid
  row_line = "Percentage spent by category" 
  
  for row in range(100, -10, -10):
    row_line += '\n' + str(row).rjust(3) + '|' 
    
    for column_value in percent_list:
      if column_value > row: # e.g. row is moving 100, 90, 80, etc. 
        row_line += ' o ' # e.g. if 34 > then 30, then 20, then 10, we'll add o
      else:
        row_line += '   '
    row_line += ' '
  row_line += "\n    ----------" # new line and 4 spaces because 100| then ---

  categories_len_list = [] 

  for category in categories:
    categories_len_list.append(len(category.category))
    
  max_len = max(categories_len_list)
  
  print(categories_len_list)
  # [4, 8]

  print(max_len) # this determines the rows for our bottom grid
  # 8

  for row in range(max_len): # creates rows 0, 1, 2, 3, 4, 5, 6, 7, 8
    row_line += '\n    '

    for column_item in range(len(categories)): # [Food, Clothing] = 2, loops 0 to 2, to create 2 columns
      if row < categories_len_list[column_item]: # [4, 8], first column is food, if 0 < 4, to create 4 rows
        row_line += ' ' + categories[column_item].category[row] + ' ' 
        # first column is food [loops from 0 to 2].current category is food [loops through 0 to 4, adding each letter per row]
        # categories is our list [Food, Clothing], .category[row] is our string[index of string]
      else:
        row_line += '   ' # 3 spaces: space, letter, space
    row_line += ' '
  return row_line

categories = [Food, Clothing]

print(create_spend_chart(categories))

"""
Percentage spent by category
100|          
 90|          
 80|          
 70|          
 60| o        
 50| o        
 40| o        
 30| o        
 20| o  o     
 10| o  o  o  
  0| o  o  o  
    ----------
     F  C  A  
     o  l  u  
     o  o  t  
     d  t  o  
        h     
        i     
        n     
        g     

"""

