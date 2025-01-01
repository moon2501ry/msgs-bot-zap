from mbz import ZapBot
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

d6 = r.randrange(1,7);
bot = ZapBot('chrome');
bot.send('Teste', f"ZapBot 1.1 version. D6: {d6}");
time.sleep(5);