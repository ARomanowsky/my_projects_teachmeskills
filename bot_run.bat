@echo off

call %~dp0wikibot\env\Scripts\activate

cd %~dp0wikibot\env

set TOKEN=5665694238:AAGBgRNgsNxU21OlUSLp2VEIffk_LK5C87E

python bot_wiki.py 

pause 
