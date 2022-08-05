## About
Most banking websites allow you to download a csv file that contains transaction data, you can use that file to create a plot that details each transaction!
### Required dependencies
```
pandas
regex
datetime
iqplot
```
## Getting started
1. Log in to your personal banking website
2. Locate your transactions tab
3. There should be an option to download documents
4. Download in 'csv' format
5. Copy the path to the csv file 
Example: ```C:\Users\You\Folder\transactions.csv```
6. Run the python file with the path as your first argument
Example: ```python plot_trasnactions C:\Users\You\Folder\transactions.csv```
![]https://github.com/liamkandel/Transactions-Plotter/blob/main/gif.gif
