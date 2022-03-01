![Profile views](https://gpvc.arturio.dev/BEPb) 
![GitHub top language](https://img.shields.io/github/languages/top/BEPb/python-bot) 
![GitHub language count](https://img.shields.io/github/languages/count/BEPb/python-bot)
![GitHub code size in bytes](https://img.shields.io/github/languages/code-size/BEPb/python-bot)
![GitHub repo size](https://img.shields.io/github/repo-size/BEPb/python-bot) 
![GitHub](https://img.shields.io/github/license/BEPb/python-bot) 
![GitHub last commit](https://img.shields.io/github/last-commit/BEPb/python-bot)

![GitHub User's stars](https://img.shields.io/github/stars/BEPb?style=social)


Read in other languages: [English](README.ru.md), [हिन्दी](README.hindi.md)


## CHROME browser offline game bot

____
![](./media/title.gif)

In automatic mode, launches the Chrome browser under windows OS, also automatically detects screen resolutions,
Based on the received data, it finds the main character - a dinosaur and calculates the response zone. My personal
the record with this bot is 3119, but you feel weak?....

## How to install and run
____
### Clone the repository
 
```sh
$ cmd
$ git clone https://github.com/BEPb/python-bot
$ cd python-bot
```
 
### Install the necessary packages (Install dependencies)
```sh
$    -r requirements.txt
```
### Turn off the Internet, make sure of this, otherwise the game will not appear in the browser
### Run our bot
 
```sh
$ python bot_offline.py
```

The bot opens the last page and updates it, in the absence of the Internet, the game opens. Because algorithm
 definitions based on only one zone, not taking into account the increasing speed of approaching objects does not
 is optimal and when you lose, the game starts again after 15 seconds, after the loss. The program itself is provided with a log
 file, taking into account the screen resolution and the duration of each game.
      
 For manual selection of the response zone, the draft.py program was also written, which will perform all the same manipulations.
 upon launching the browser, and then it will save you a screenshot with a black rectangle highlighted in the response area.
 He described the code in great detail, for its improvement, this is only welcome. Python rules
 
____
![](./media/python.jpeg)