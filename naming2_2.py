t = [10, 7, 5, 6]
s = 0
for j in range (0, len(t)):
    s += t[j] * 4 / 5
print(s)


task_estimate = [10, 7, 5, 6]
real_days_per_idle_days = 4
work_days_per_week = 5
days_sum = 0
for task_index in range(0, len(task_estimate)):
    real_task_days = task_estimate[task_index] * real_days_per_idle_days
    real_task_weeks = real_task_days / work_days_per_week
    days_sum += real_task_weeks
print(days_sum)
