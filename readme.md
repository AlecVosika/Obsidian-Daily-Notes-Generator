# Daily Note Generator

This Python script automatically generates a daily note with a predefined template in a specific directory structure based on the current date. It's designed to work with markdown files and supports the `dataview` plugin syntax for Obsidian.

## Directory Structure

The script organizes notes into folders by year and month within the specified base directory:

```
C:\Users\Alecv\Documents\MainVault\Daily Notes
│
└───2024
    │
    └───02-February
        │   2024-02-01-Friday.md
        │   2024-02-02-Saturday.md
        │   ...
```

## Prerequisites

- Python 3.x installed on your Windows machine.
- Basic knowledge of Windows Task Scheduler for automating the script.

## Setup Instructions

1. **Python Script**: Ensure the script `main.py` (or whatever you've named it) is located in a convenient and accessible directory on your system.

2. **Scheduling with Windows Task Scheduler**:

   - **Open Task Scheduler**: Press `Windows + R`, type `taskschd.msc`, and press Enter to open Task Scheduler.

   - **Create a New Task**: In the Actions pane on the right, click "Create Task...".

   - **General Tab**: Enter a name for the task, such as "Daily Note Generator". Optionally, provide a description.

   - **Triggers Tab**: Click "New..." to create a new trigger. Set it to start "Daily" and set the start time to `00:01` every day. Click "OK" to save the trigger.

   - **Actions Tab**: Click "New..." to create a new action. Set "Action" to "Start a program". In the "Program/script" field, enter the path to your Python executable (usually found in `"C:\Program Files\Python312\python.exe"`). In the "Add arguments" field, enter the path to your script `"C:\Users\Alecv\Documents\AV\Repo\Obsidian Daily Notes Generator\main.py"`. In the "Start in" field, enter the directory path where your script is located. Click "OK" to save the action.

   - **Conditions and Settings Tabs**: Adjust these settings as needed, but the defaults should suffice for most users.

   - **Save Your Task**: Click "OK" to save the new task. You may be prompted to enter your Windows password.

3. **Verification**: To verify the task runs as expected, you can right-click the task in Task Scheduler and select "Run". Check the specified directory for the new note to confirm it's being generated correctly.
