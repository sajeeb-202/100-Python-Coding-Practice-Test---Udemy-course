import calendar

def display_calendar(year, month):
    # Validate year
    if year <= 0:
        return "Invalid year. Year must be positive."
    
    # Validate month
    if month < 1 or month > 12:
        return "Invalid month. Month must be between 1 and 12."
    
    # Create a TextCalendar object (Monday as first day)
    cal = calendar.TextCalendar(calendar.MONDAY)
    
    # Generate and return the formatted calendar
    return cal.formatmonth(year, month)