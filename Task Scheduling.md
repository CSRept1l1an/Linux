
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
