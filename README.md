![](https://img.shields.io/github/repo-size/CoderAbhinav/meeting_bot) ![](https://img.shields.io/hackage-deps/v/selenium) ![](https://img.shields.io/github/contributors/CoderAbhinav/meeting_bot) ![](https://img.shields.io/github/last-commit/CoderAbhinav/meeting_bot) ![](https://img.shields.io/github/downloads/CoderAbhinav/meeting_bot/total) ![](https://img.shields.io/github/forks/CoderAbhinav/meeting_bot?style=social)
![](https://img.shields.io/pypi/pyversions/pandas)

## [About](#about-the-project)

## [Developers](#developed-by)

## [Getting Started](#instructions)

![meeting bot](files/Meeting_logo.png)



-----------------------------------------------
# About The Project
This is a simple bot which automatically log you in to your scheduled 
meeting. So there will be no more hassle for you to join any meeting
This Project is made by students of First Year Computer Engineering at
Vishwakarma Institute Of Information Technology, Pune
(http://www.viit.ac.in)
----------------------------------------------------
# Developed By 
![Github/](files/GitHub-Mark-32px.png)[ /CoderAbhinav](https://github.com/CoderAbhinav) - Abhinav Belhekar

![Github/](files/GitHub-Mark-32px.png)[ /keyurgit45](https://github.com/keyurgit45) - Keyur Gandhi

![Github/](files/GitHub-Mark-32px.png)[ /shardul2002](https://github.com/shardul2002) - Shardul Joshi

![Github](files/GitHub-Mark-32px.png)[ /programmerAtharva](https://github.com/programmerAtharva) - Atharva Chavan

--------------------------------------------------------

# Instructions

* ## Setting Your Environment 
    - Open the folder containgin the program.
    - Open terminal in the folder.
        - In Windows by typing 'cmd' in the file explorer
    - Then type the following command
        - > ### pip install -r requirements.txt
    - As the Environment is ready go to the next part of the process

* ## Writing your schedule 
    - To write the schedule just open the 'timings.csv' file in Excel.
    - Then write the appropriate data in column.
    - How to Enter the details ?
        - Date Column : Format (DD/MM/YYYY)
        - Time column : Format (HH:MM:SS) 24 hours format 
    - The program is designed in such a way that it would automaticaly check if link is available or not, if it is unavilable then the program uses ID & Password
    - You can write one of the Link or ID and Password.

* ## Changes required in program:
    - Open main.py file in any text editor
    - Add your email id and password at line 11 of program.
    - Add chrome profile path at line 17 of program.
        - You can get user path by typing 
            > ### chrome://version    
            in google chrome. (look for profile path : )
    - Your Program is now ready to use.

* ## How to use the program ?
    - Open terminal in the folder containing the program.
    - type the following command
        - > ### python main.py
    



