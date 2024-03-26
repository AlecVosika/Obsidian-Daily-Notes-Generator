import datetime
from pathlib import Path
from calendar import monthrange

def create_missing_daily_notes(year=2024, month=3):
    # Determine the number of days in March 2024
    num_days = monthrange(year, month)[1]
    
    # Base directory path
    base_directory = Path("C:/Users/Alecv/Documents/MainVault/Daily Notes")
    year_folder_name = str(year)
    month_folder_name = datetime.date(year, month, 1).strftime("%m-%B")
    
    # Iterate over each day of the month
    for day in range(1, num_days + 1):
        # Construct the date
        current_date = datetime.date(year, month, day)
        file_name = current_date.strftime("%Y-%m-%d-%A.md")
        full_path = base_directory / year_folder_name / month_folder_name
        
        # Check if the file already exists
        if not (full_path / file_name).exists():
            # Ensure the directory exists
            full_path.mkdir(parents=True, exist_ok=True)
            
            # Calculate yesterday and tomorrow
            yesterday = current_date - datetime.timedelta(days=1)
            tomorrow = current_date + datetime.timedelta(days=1)
            
            # Creating and writing the daily note template
            with open(full_path / file_name, 'w', encoding='utf-8') as file:
                file_content = f"""---
created: {current_date.strftime("%Y-%m-%d %H:%M")}
tags:
  - DailyNotes
---
# {current_date.strftime("%A, %B %d, %Y")}

<< [[{yesterday.strftime('%Y-%m-%d')}-{yesterday.strftime('%A')}|Yesterday]] | [[{tomorrow.strftime('%Y-%m-%d')}-{tomorrow.strftime('%A')}|Tomorrow]] >>

---
### 📅 Daily Questions
##### 📅 Today I...
- 
##### 🙌 Tasks
- [ ] 

---
# 📝 Notes
- 

---
### Notes created today
```dataview
List FROM "" WHERE file.cday = date("{current_date.strftime('%Y-%m-%d')}") SORT file.ctime asc
```

### Notes last touched today
```dataview
List FROM "" WHERE file.mday = date("{current_date.strftime('%Y-%m-%d')}") SORT file.mtime asc
```
"""

                file.write(file_content)
                print(f"Daily note for {current_date.strftime('%Y-%m-%d')} created successfully.")



if __name__ == "__main__":
    create_missing_daily_notes()