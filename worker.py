__author__ = 'm12sl'
import mraa
import time
import redis

red = redis.Redis('localhost', port=6379)

led = mraa.Gpio(13)
led.dir(mraa.DIR_OUT)
led.write(0)

red.set('led', 0)
while True:
    status = int(red.get('led'))
    if status in [0, 1]:
        led.write(status)
    time.sleep(1)
