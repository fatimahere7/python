"""

 How many days,weeks,and month we left if we live until 90 years old
 1 year = 365 days ,52 weeks, 12 month

"""
age = int(input("Enter your current age : "))
year_left = 90-age
days_left= year_left * 365
months_left = year_left * 12
weeks_left = year_left * 52
print(f"you have  only\n{year_left} year\n{days_left} days\n{months_left} months\n{weeks_left} weeks left")
