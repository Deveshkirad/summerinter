import sys
from datetime import datetime

print("=== Docker Python Application ===")
print(f"Python Version: {sys.version}")

current_time = datetime.now()
print(f"Current Date & Time: {current_time}")