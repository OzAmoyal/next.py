def gen_secs():
    for i in range(0,60):
        yield i
def gen_minutes():
    for i in range(0,60):
        yield i
def gen_hours():
    for i in range(0,24):
        yield i

def gen_time():
    for hour in gen_hours():
        for minute in gen_minutes():
            for second in gen_secs():
                yield "{:02d}:{:02d}:{:02d}".format(hour, minute, second)
                
                
for i in gen_time():
    print(i)