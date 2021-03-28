from time import time
from multiprocessing import Process
from playsound import playsound
import time
def print_starting():
    str1 = '''
          /\    /\    ___  ___ ____ ____          ____
         // \  // \  ||__ ||__  ||   ||  ||\\ || ||  __
        //   \//   \ ||__ ||__  ||  _||_ || \\|| ||__||
        _______	  _   _  ___  _________________________
       |       | |_) | |  |  |             version 1.0 |
       |_______| |_) |_|  |  |_________________________|

        Project By:
        Abhinav Belhekar (https://github.com/CoderAbhinav)
        Keyur Gandhi     (https://github.com/keyurgit45  )
        Shardul Joshi    (https://github.com/shardul2002)
        Atharva Chavan   (https://github.com/programmerAtharva)

        About The Project :
        This is a simple bot which automatically log you in to your scheduled 
        meeting. So there will be no more hassle for you to join any meeting
        This Project is made by students of First Year Computer Engineering at
        Vishwakarma Institute Of Information Technology, Pune
        (http://www.viit.ac.in)
        
        Find Project Reposetories on github at:
        https://github.com/CoderAbhinav/meeting_bot
        
        Dependencies :
        selenium 3.141.0
        pandas 1.2.2
        pause 0.3
       
        '''
    print(str1)
def auout(): 
    playsound('audio/startup_1.mp3')

def give_intro():
    print_starting()
    auout()