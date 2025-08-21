import re
from datetime import datetime, timezone

def parse_log_timestamps(log):
    pattern = r'\[(\d{2}/[A-Za-z]{3}/\d{4}:\d{2}:\d{2}:\d{2} \+\d{4})\]'
    
    matches = re.findall(pattern, log)
    formatted_timestamps = []
    
    for ts in matches:
        dt = datetime.strptime(ts, "%d/%b/%Y:%H:%M:%S %z")
        
        dt_utc = dt.astimezone(timezone.utc)
        
        formatted_timestamps.append(dt_utc.strftime("%Y-%m-%d %H:%M:%S"))
        
    return formatted_timestamps

log_string = '''
127.0.0.1 - - [21/Aug/2025:14:23:15 +0000] "GET /index.html HTTP/1.1" 200 1024
127.0.0.1 - - [22/Aug/2025:18:45:00 +0000] "POST /form HTTP/1.1" 302 512
'''

timestamps = parse_log_timestamps(log_string)
print(timestamps)
