The code which will tell you that in which year you will turn 95 years old:-
#!/usr/bin/python3
from datetime import datetime
name=input("Enter your name:")
age=int(input("Enter your age:"))
current_year=datetime.now().year
print(f"{name} will turn 95 by the year {current_year+95-age}")
