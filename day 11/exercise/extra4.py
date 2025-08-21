from datetime import datetime
import pytz

def convert_timezone(time_str, from_tz, to_tz):

    time_format = "%Y-%m-%d %H:%M:%S"
    
    try:

        naive_dt = datetime.strptime(time_str, time_format)
        

        from_timezone = pytz.timezone(from_tz)
        to_timezone = pytz.timezone(to_tz)
        

        localized_dt = from_timezone.localize(naive_dt)
        

        converted_dt = localized_dt.astimezone(to_timezone)
        

        return converted_dt.strftime(time_format)
    
    except Exception as e:
        return f"Error: {e}"


time_input = "2023-10-05 14:30:00"
from_timezone = "US/Eastern"
to_timezone = "UTC"

converted_time = convert_timezone(time_input, from_timezone, to_timezone)
print(f"Converted time: {converted_time}")
