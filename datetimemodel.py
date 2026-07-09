from datetime import datetime, timedelta 

now = datetime.now()

new_time = now + timedelta(days=10)

print("current time:", now)
print("new time after 10 days:", new_time)