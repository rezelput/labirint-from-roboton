import sys
import time
import random
import math

class Program():
  __interpretation_started_timestamp__ = time.time() * 1000

  pi = 3.141592653589793
  start = None
  x = None
  z = None

  def execMain(self):

    
    while True:
      self.x = brick.sensor("D1").read()
      self.start = 0
      self.start = Threading.receiveMessage(False)
      
      if (self.x < 20 and self.x > 10):
        while True:
          self.z = brick.sensor("A1").read()
          if bool(self.z = 1):
            break
          while True:
            while brick.sensor("A1").read() <= 0:
              script.wait(10)
            
            brick.motor("M3").setPower(15)
            
            brick.motor("M4").setPower(25)
            
            if self.x < 20:
              break
          while not (brick.sensor("D1").read() < 10):
            script.wait(10)
          
          brick.motor("M3").setPower(-(100))
          brick.motor("M4").setPower(-(100))
          
          script.wait(300)
          
        while brick.sensor("A1").read() <= 0:
          script.wait(10)
        
        brick.motor("M3").setPower(-(100))
        brick.motor("M4").setPower(-(100))
        
        script.wait(700)
        
        brick.motor("M3").powerOff()
        brick.motor("M4").powerOff()
        
        brick.motor("M4").setPower(25)
        
      else:
        brick.motor("M3").setPower(50)
        brick.motor("M4").setPower(50)
        
        while not (brick.sensor("D1").read() < 15):
          script.wait(10)
        

def main():
  program = Program()
  program.execMain()

if __name__ == '__main__':
  main()
