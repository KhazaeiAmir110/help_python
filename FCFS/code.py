
# زمان پاسخ هر فرآیند
def find_waiting_time(processes, n, burst_time, wt):
    wt[0] = 0
    for i in range(1, n):
        wt[i] = burst_time[i - 1] + wt[i - 1]

# جمع پاسخ فرآیند
def find_turn_around_time(burst_time, wt, tat):
    for i in range(len(burst_time)):
        tat[i] = burst_time[i] + wt[i]

# زمان متوسط : پاسخ / منتظر
def find_avg_time(n, wt, tat):
    total_wt = sum(wt)
    total_tat = sum(tat)
    avg_wt = total_wt / n
    avg_tat = total_tat / n
    print("Average waiting time =", avg_wt)
    print("Average turnaround time =", avg_tat)

# نمایش به صورت جدول
def display(n, burst_time, wt, tat):
    print("Processes\tBurst Time\tWaiting Time\tTurnaround Time")
    for i in range(n):
        print(f"{i + 1}\t\t|\t\t{burst_time[i]}\t\t|\t\t{wt[i]}\t\t|\t\t{tat[i]}")

def fcfs(processes, burst_time):
    n = len(processes)
    wt = [0] * n
    tat = [0] * n
    find_waiting_time(processes, n, burst_time, wt)
    find_turn_around_time(burst_time, wt, tat)
    display(n, burst_time, wt, tat)
    find_avg_time(n, wt, tat)

# example
# processes = [1, 2, 3]
# burst_time = [5, 9, 6]
# fcfs(processes, burst_time)