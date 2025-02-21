def is_armstrong_number(n):
    result = 0
    for x in str(n):
        result += int( x ) ** len(str(n))
    
    return True if result == n else False
