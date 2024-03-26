import datetime
from pathlib import Path

def create_daily_note():
    # Current date
    today = datetime.datetime.now()
    # Calculating yesterday and tomorrow's dates
    yesterday = today - datetime.timedelta(days=1)
    tomorrow = today + datetime.timedelta(days=1)
    
    # Formatting folder and file names
    year_folder_name = today.strftime("%Y")
    month_folder_name = today.strftime("%m-%B")
    file_name = today.strftime("%Y-%m-%d-%A.md")
    
    # Defining the base directory path
    base_directory = Path("C:/Users/Alecv/Documents/MainVault/Daily Notes")
    # Constructing the full path for today's note
    full_path = base_directory / year_folder_name / month_folder_name
    # Ensure the directory exists
    full_path.mkdir(parents=True, exist_ok=True)
    
    # Creating and writing the daily note template
    with open(full_path / file_name, 'w', encoding='utf-8') as file:
        file_content = f"""---
created: {today.strftime("%Y-%m-%d %H:%M")}
tags:
  - DailyNotes
---
# {today.strftime("%A, %B %d, %Y")}

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
List FROM "" WHERE file.cday = date("{today.strftime('%Y-%m-%d')}") SORT file.ctime asc
```

### Notes last touched today
```dataview
List FROM "" WHERE file.mday = date("{today.strftime('%Y-%m-%d')}") SORT file.mtime asc
```
"""

        file.write(file_content)
        print(f"Daily note for {today.strftime('%Y-%m-%d')} created successfully.")

if __name__ == "__main__":
    create_daily_note()