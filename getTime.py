def getMillis() -> int:
    from datetime import datetime
    import time

    # Print today's date and time in UTC
    tdd = datetime.utcnow()
    print("Current UTC time:", tdd)

    # Print today's date in milliseconds since 1/1/1970
    millis = int(round(time.time() * 1000))
    print("Milliseconds since Unix epoch:", millis)
    
    return millis

# Test the getMillis function
if __name__ == "__main__":
    millis = getMillis()
    print("Returned milliseconds:", millis)