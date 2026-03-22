from collections import deque

# queue and stack
income_application = deque()
processed_application = []

# messy data
messy_data = [" TechCorp ", "bio-gen"]

# clean and enqueue
for data in messy_data:
    clean_data = data.strip().lower()
    income_application.append(clean_data)

# process applications (FIFO) Queue
while income_application:
    first = income_application.popleft()
    print("Processing:", first)
    processed_application.append(first)

# undo last action (LIFO) Stack
if processed_application:
    undo = processed_application.pop()
    print("Undo last processed:", undo)
else:
    print("No processed applications to undo.")

