
#Schedule an event

#import sched , time
#scheduler = sched.scheduler()


#def saytime():
#    print(time.ctime())
#    scheduler.enter(delay = 2, priority = 1 , action = saytime)
#
#def hello():
#    print("Hello")
#    scheduler.enter(delay = 3, priority = 1 , action = hello)
#
#def start():
#    scheduler.enter(delay = 0, priority = 2, action = hello)
#    scheduler.enter(delay = 0, priority = 1 , action = saytime)

#start()

#scheduler.run(blocking = True)

#Schedule an event in a specific moment

import sched, time

from datetime import datetime, timedelta

                                                # + , delayfunc= 
scheduler = sched.scheduler(timefunc = time.time)

#def reschedule_plus_sec():
    # undefined time, but quantity

    #new_target = datetime.now()
    #new_target += timedelta( seconds = 30 )
    #print(new_target)

    #scheduler.enterabs ( new_target.timestamp(), priority = 100 , action= saytime)
    
    # defined timed
    #scheduler.enterabs (datetime(2021, 11, 16, 19, 27, 45).timestamp(), priority = 100 , action= saytime)
 
#def saytime():
#    print(time.ctime())
#    #reschedule_plus_sec()
#    
#reschedule_plus_sec()

#scheduler.run(blocking = True)


def reschedule_plus_min():
    new_target = datetime.now()
    new_target += timedelta( seconds= 10 )
    print(new_target)

    scheduler.enterabs ( new_target.timestamp(),
                        priority = 100 ,
                        action= saytime)
    

def saytime():
    print(time.ctime())
    reschedule_plus_min()

def google_request():
    from requests import get

    if get('https://www.google.com/').status_code != 304:
        print('we got a problem')
    else:
        reschedule_plus_min()

reschedule_plus_min()
google_request()

scheduler.run(blocking = True)

#dumps list - from pickles import load

