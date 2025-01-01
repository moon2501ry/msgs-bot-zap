import pyautogui as pg
import random as rnd
import time

rng = pg.prompt(text='Quantidade de msgs:', title='ZaWarudo Mode')
bg = pg.confirm(text='Começar?', title='ZaWarudo Mode', buttons=['Sim','Fechar']);
if bg == 'Fechar':
    exit();
pg.moveTo(700,700); #Coordenadas da caixa de texto
pg.leftClick();
for i in range(int(rng)):
    msg = rnd.choice(['Za Warudo!!!','MUDA','MUDA','MUDA','MUDA','JOJOOO!!!!!!!']);
    print(str(i)+'- '+msg);
    pg.write(msg);
    pg.press('enter');
    if msg == 'Za Warudo!!!':
        print('Sleep de 2 segundos');
        time.sleep(2);