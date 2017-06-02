import time
t = time.time()
y, m, d, hh, mm, ss, weekday, jday, dst = time.localtime(t)

print(t, y, m, jday)


print(time.localtime(t))
