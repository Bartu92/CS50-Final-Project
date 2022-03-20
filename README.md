# Turkish Investment Funds Portfolio Tracker 
#### Video Demo:  <https://www.youtube.com/watch?v=GFUotrsFhMk&ab_channel=bartugonulalan>
#### Description: This is a desktop application to assist users in keeping track of their portfolios and calculates the returns of their investments with up-to-date data. 

## Overview
In Turkey, if a small investor wants to invest in investment funds, they have to do it via Banks. Every bank has a system that shows you your portfolio. Unfortunately, if you have multiple funds from multiple banks, you need a 3rd-party fund tracker. With that, investors don't have many options. That's why I wanted to code a desktop app to solve this roblem because there aren't any portfolio trackers on desktop PC.
## Features
The application is pretty simple. Users can enter any funds code to see its up-to-date performance. After the user analyzes it, users can add it or any investment fund to their locally stored database. The application keeps those portfolios in its database. When the user calls the data, the application quickly calculates the return ratios and current value of an investment for each record.

 

## Technologies used

#### Language: 

 - Python
 - SQL
 - Kivy

#### Used libraries: 
 - GUI: Kivy
 - Database: sqlite3
 - Scrapping tool: Beautiful Soup
 - Datetime

#### Data resource: [Turkey Electronic Fund Trading Platform(TEFAS)](https://www.tefas.gov.tr/)



## How to use?
When users open the application. There are 4 different sections. 

#### "Adding a fund section" (Top left section):
In this section, users can add a fund to their portfolio database. To add a record, they need to enter 4 different info, which are; 

"Portfolio name" - (Users choice)
"Fund code" - (The funds 3 letter code which user wants to add)
"Share Amount" - (Buying count of that funds)
"Buying Price of a single share"

Then click "Add Fund" button to save the fund to your database. 

#### Show My Portfolio section (Bottom Left section):
In this section, users can see their funds by clicking the "Show My Portfolio" button. 
Maximizing the app's window is highly recommended to see the portfolios properly. 
At each record, users can also see the current value and return of their investments.
The app calculates this via prices comes from the government website [TEFAS](https://www.tefas.gov.tr/) *Turkey Electronic Fund Trading Platform*.

#### Delete a Fund section (Top right section:
In this section, users can delete a record from their database. 
To delete a record they must enter the id of that record. 
Ids of records can be found in the Show MY Portfolio section. 
After entering the ID, by simply clicking the "Delete the record" button, 
users can delete the record that has already been added previously. 

#### Analyse Fund (Bottom right section):
In this section, users can analyse for any fund that has been placed on [Turkey Electronic Fund Trading Platform(TEFAS)](https://www.tefas.gov.tr/)
To search a fund, users must enter the code of that fund and click the "Search a fund" button.
By searching a fund, users can see summarized up-to-date analyse about that fund and see its performance.


## Behind the curtain
Application has 4 files:

 - main.py 
 - my.kv
 - portfolio.db
 - daily_data.py

### "daily_data.py":
daily_data.py has multiple functions inside. Their main usage is about scrapping data from [Turkey Electronic Fund Trading Platform(TEFAS)](https://www.tefas.gov.tr/) Beautiful Soap is a powerful library to scrap data from a website. Sadly it slows the app a little bit. An API could be better but there isn't any public API to get the data. 

### "portfolio.db":
It's a SQL database.
The user doesn't need to enter every info. After getting 

	db.execute("CREATE TABLE main_table ("  
	 "id INTEGER PRIMARY KEY AUTOINCREMENT," 
	 "portfolio_name TEXT NOT NULL," 
	 "fund_code TEXT NOT NULL," 
	 "fund_name TEXT NOT NULL," 
	 "fund_share INTEGER NOT NULL," 
	 "share_value FLOAT NOT NULL," 
	 "invest_amount FLOAT NOT NULL," 
	 "buy_date TEXT NOT NULL" ");")



### "my.kv":
It's the kivy file for GUI.
I choose this because this GUI can be convertible to a mobile app. Which can be good in the future. Personally, GUI language and implementation was the hardest part. It can be much better and user friendly and eye-catching. Multiple pages can be added with multiple files. For the first steps, this is what I've got.

### "main. py":
This is where daily_data formulas are integrated with SQL and kivy. 
Under the MyGridLayout(Widget) class, there are 4 different functions for 4 functions of the app. These are;

 1. Saving an input to database -  save_fund_button(self):
 2. Deleting an input from database - delete_a_fund(self):
 3. Displaying portfolios - show_my_portfolio(self):
 4. Analyzing a fund - seach_fund_by_code(self):

Except for the 4th one, all other functions are using SQL. Each functions are implemented to take input and give an output via GUI for user interactions.

## What have i accomplished? What can be better? Future To-Do list

 - [x] Get live data from an official resource
 - [x] Make this data more meaningful
 - [x] Have a GUI that works enough
 - [x] Have a database
 - [x] Display database
 - [x] While displaying, calculating live values and returns
 - [ ] Have a better user-friendly GU
 - [ ] Add multiple pages to GUI
 - [ ] Get historic data
 - [ ] Insert Graphs

##### This project was made by Bartu Gönülalan for CS50 Final Project



