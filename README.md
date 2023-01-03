# freeCodeCamp-Budget-App

## Instructions:
https://www.freecodecamp.org/learn/scientific-computing-with-python/scientific-computing-with-python-projects/budget-app

## Purpose
When the budget object is printed it should display:

```python
*************Food*************
initial deposit        1000.00
groceries               -10.15
restaurant and more foo -15.89
Transfer to Clothing    -50.00
Total: 923.96
```

Besides the Category class, create a function (outside of the class) called create_spend_chart that takes a list of categories as an argument. It should return a string that is a bar chart.
This function will be tested with up to four categories.

```python
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
```

## Preview:
<img src="https://github.com/iVuDang/freeCodeCamp-Budget-App/blob/main/budget%20preview.png" width=100% height=100%>

## Technologies: 
* Python

## Outcome :white_check_mark: :
| Website | Link | 
| ------------- | ------------- | 
| Replit demo | https://replit.com/@iVuDang/freeCodeCamp-Budget-App-v1#main.py | 

<br/>

- - - -

## Notes - stuff learned:  
1) __str_method

The __str__ method in Python represents the class objects as a string – used for classes.
Otherwise, when trying to print(class), it shows: 
__main__.Category object at 0x7fdec80bf610>


2) Default & optional parameters in Python functions 
  ```python
  def deposit(self, amount, description = '') 
  
  description = '' defaults to empty string, used for 'optional' arguments
  ```

3) A list can contain another list. A dictionary can contain another dictionary. A dictionary can also contain a list, and a list can contain dictionaries. 


4) Can use accumulator variable '+=', or appending to a list & sum(list), the latter keeps a nicer documentation trail, and for debugging / print.

Syntax: sum(list)

5) Three ways to if condition a Boolean:  
  ```python
  if self.check_funds(amount):
  if self.check_funds(amount) is True:
  if self.check_funds(amount) == True:
  ```

6) Two ways to return a Boolean: 

  ```python
  return amount > self.get_balance()
  ```

same as:
  ```python
  if amount > self.get_balance():
      return False
  else:
      return True
  ```

7) To comment all code out:
Ctrl + /


8) Two ways to center strings:

with f'string'
  ```python
    >>> hello = "world"

    >>> f"{hello:^11}"
    '   world   '

    >>> f"{hello:*^11}"
    '***world***'
  ```

with string.center() method
  ```python
    string.center(length, character) 
  ```


9) Create a list with a for loop inside [] 
[modification for item in list]

percent_list = [(item/total_spend) for item in spend_list]

  ```python
  row_line = "Percentage spent by category" + '\n'
  
  for row in range(100, -10, -10):
    row_line += str(row).rjust(3) + '|' + '\n'
    for column_value in percent_list:
      if column_value > row: # e.g. row is moving 100, 90, 80, etc. 
        row_line += ' o ' # e.g. if 34 > then 30, then 20, then 10, we'll add 
      else:
        row_line += '   '
    row_line += "\n    ----------" # new line and 4 spaces because 100| then ---
  ```

10) Using for loop with range(start, stop, step) is good for generating line instances. 

Using for loop within a for loop is good for creating a grid e.g. a bar graph. 

range(start, stop, step) 
range(start default is 0, stop required, step, default is 1)

  ```python
  row_line = "Percentage spent by category" 
  
  for row in range(100, -10, -10):
    row_line += '\n' + str(row).rjust(3) + '|' 
    
    for column_value in percent_list:
      if column_value > row: # e.g. row is moving 100, 90, 80, etc. 
        row_line += ' o ' # e.g. if 34 > then 30, then 20, then 10, we'll add 
      else:
        row_line += '   '
    row_line += ' '
  row_line += "\n    ----------" # new line and 4 spaces because 100| then ---
  ```

11) Two ways to right align strings:

a) string.rjust(length, character) 

b)  line = f"{variable:>length}"


12) Can add a last row by putting the accumulator variable OUTSIDE of the loop, and accumulate. 


## Citations:
Ideas to solve project inspired from renatosantos98, RobisonTorres, sfoteini. 

https://www.educative.io/answers/what-is-the-str-method-in-python
http://www.compciv.org/guides/python/fundamentals/dictionaries-overview/
https://www.askpython.com/python/list/list-of-dictionaries


https://miguendes.me/73-examples-to-help-you-master-pythons-f-strings
https://cheatography.com/brianallan/cheat-sheets/python-f-strings-basics/
https://www.pythonmorsels.com/string-formatting/

https://www.w3schools.com/python/ref_func_range.asp



