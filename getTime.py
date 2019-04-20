def getMillis():
    # type: () -> object
    import pytz
    from datetime import datetime
    import time

    #Print today's date and time in UTC
    tdd = datetime.utcnow().replace(tzinfo=pytz.utc)
    print(tdd)

    #Print today's date in milliseconds since 1/1/1970
    millis = int(round(time.time() * 1000))
    #print(millis)
    return millis


