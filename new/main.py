from mbz import ZapBot
from datetime import datetime
import random as r
import time

"""
Requisitos:
selenium (pip install selenium);
time (pip install time).

- Para usar o bot em um projeto especifico, passe o arquivo 'mbz.py' para a pasta do projeto
e importe a classe ZapBot ('from mbz import ZapBot');
- O __init__ de ZapBot precisa do parametro 'browser', que é o navegador que você irá usar.

Lista de navegadores para o parametro 'browser':
'chrome'; 'safari'; 'edge'; 'firefox'.
"""

bot = ZapBot();
bot.set_chat('Teste');
bot.send(bot.__version__);

# while True:
#     time.sleep(10);
#     time_ = datetime.now().strftime("%H:%M");
#     match time_:
#         case :
#             bot.send()
#     print(time_);