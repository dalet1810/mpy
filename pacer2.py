import machine
import esp32
import time

l2=machine.Pin(2,machine.Pin.OUT)

def rmt2():
  r = esp32.RMT(2,pin=l2)
  return r

def blink():
    pwm2 = machine.PWM(l2, freq=1, duty=255)
    return pwm2

def pacer(strt, tgt, dly):
    crnt = strt
    pwm2 = machine.PWM(l2, freq=strt, duty=512)
    while crnt < tgt+1:
        time.sleep(dly)
        crnt += 1
        pwm2.freq(crnt)
    pwm2.deinit()
    return pwm2
