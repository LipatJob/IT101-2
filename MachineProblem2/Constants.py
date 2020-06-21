import os

# Window
WINDOW_TITLE = "4 Pycs 1 Word"
SCREEN_SIZE = "506x770+10+10"

# Backgrounds
BG_COLOR = "#1c2131"
HDR_COLOR = "#1c1c20"

# Guess Letters
BTN_SIZE = 40

# Costs and Rewards
LEVEL_REWARD = 10
SKIP_COST = 10
REMOVE_LETTER_COST = 2
REVEAL_LETTER_COST = 2

# Sounds
CLICK_SOUND_FILE = os.getcwd() + "\\assets\\sound\\click.wav"
CORRECT_SOUND_FILE = os.getcwd() + "\\assets\\sound\\correct2.wav"
INCORRECT_SOUND_FILE = os.getcwd() + "\\assets\\sound\\incorrect.wav"

# Pictures
COIN_PICTURE =  os.getcwd() + "/assets/coin.png"
PLAY_PICTURE =  os.getcwd() + "/assets/play.png"
TITLE_PICTURE =  os.getcwd() + "/assets/titlelogo.png"
TITLE_LEVEL_PICTURE =  os.getcwd() + "/assets/titlelevel.png"
END_BUTTON_PICTURE =  os.getcwd() + "/assets/endbutton.png"
FAVICO = os.getcwd() + "/assets/favico.png"

# Levels
LAST_LEVEL = 50