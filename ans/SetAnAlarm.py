import sched
import time
import winsound # only for windows.

def my_a_event(msg):
    print(f"Message: {msg}")
    winsound.Beep(37, 10000)
    
def set_an_alarm(alarm_time, msg):
    my_a_plan = sched.scheduler(time.time, time.sleep)
    my_a_plan.enterabs(alarm_time, 1, my_a_event, argument=(msg,))
    print("Alarm set for: %s" % time.asctime(time.localtime(alarm_time)))
    my_a_plan.run()

def main():
    msg = 'Wake up!'
    set_seconds_into_future = 60
    a_time = time.time() +  set_seconds_into_future

    set_an_alarm(a_time, msg)

if __name__ == '__main__': main()
