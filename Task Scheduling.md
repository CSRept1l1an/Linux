
## Linux Task Scheduling Cheat Sheet

This cheat sheet covers two popular methods for scheduling tasks in Linux: cron and at.

### 1. cron

- **What it is:** A powerful tool for scheduling tasks to run periodically in the background.
- **How it works:** Uses a crontab file which defines the schedule (time and date) and the command to execute.
- **Crontab format:**

  ```
  Minute Hour DayOfMonth Month DayOfWeek Command
  ```

### Special characters:

- `*`: Matches any value in the field (e.g., `* * * * *` runs every minute)
- `,`: Separates multiple values (e.g., `0,15 * * * *` runs at minute 0 and 15 of every hour)
- `-`: Defines a range (e.g., `10-20 * * * *` runs between minute 10 and 20 of every hour)
- `/`: Defines an interval (e.g., `*/15 * * * *` runs every 15 minutes)

### Common shortcuts:
- `@hourly` : Run once every hour (0 * * * *)
- `@daily` : Run once every day (0 0 * * *)
- `@weekly` : Run once every week (0 0 * * 0) (Sunday)
- `@monthly` : Run once every month (0 0 1 * *)
- `@reboot` : Run once after system reboot

### Editing crontab:
- Use `crontab -e` to edit your crontab file.
- Choose a text editor (e.g., nano, vi) to add your schedule entries.

### `at`
- **What it is**: Used for scheduling one-time tasks to run at a specific date and time.
- **How it works**: Takes a command and a time specification as input.
- **Syntax**: at TIME [ + INTERVAL ] command
- **TIME**: Can be specified in various formats (e.g., 14:30, 20:00 tomorrow, next tuesday 3pm)
- **INTERVAL**: Optional time interval to wait before running the command (e.g., + 5 minutes)
