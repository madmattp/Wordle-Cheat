# Wordle_cheat v1
# by madmattp

from os import path
from datetime import datetime
from selenium import webdriver

print("#=------------------------------------=#\n|        \033[1;31;40m Simple Wordle Cheat \033[0m         |\n|                  por\033[1;33;40m madmattp \033[0m       |\n#=------------------------------------=#")
print(f"Data atual: {datetime.now()}")

PATH = path.realpath("chromedriver.exe")
option = webdriver.ChromeOptions()
option.add_argument('headless')
driver = webdriver.Chrome(PATH, options=option)

link = "https://www.nytimes.com/games/wordle/index.html"
driver.get(link)

raw_data = driver.execute_script('return localStorage.getItem("nyt-wordle-state")')
solution = raw_data[104:111]

driver.quit()

print(f"\nA resposta correta é \033[1;31;40m{solution}\033[0m!")
input("(Pressione Enter para sair...)")