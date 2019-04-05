import random
import re

from dicebot_model import Dice, DiceBot


def roll(bot, update):
    dice_text = update.message.text.split(' ')[-1]
    if re.match(r'^\d*[dD]\d*$', dice_text):
        text_result = dice_text.split('d')
        cnt = int(text_result[0])
        upper = int(text_result[1])
    else:
        cnt = 2
        upper = 6
    
    if cnt > 20:
        reply = '주사위가 너무 많습니다'
    elif upper > 120:
        reply = '주사위 면이 너무 많습니다'
    else:
        dice = Dice(cnt, upper)
        result = dice.roll()
        reply = (f'전체 🎲: {", ".join(str(i) for i in result)} \n'
                 f'결과: {sum(result)}')
    update.message.reply_text(reply)


dice_bot = DiceBot()
dice_bot.add_handler('roll', roll)
dice_bot.add_handler('r', roll)
dice_bot.start()
