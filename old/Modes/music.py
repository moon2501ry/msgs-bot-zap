import pyautogui as pg

with open('Modes/music.txt') as fl:
    msg = fl.readlines();
bg = pg.confirm(text='Começar?', title='Music Mode', buttons=['Sim','Fechar']);
if bg == 'Fechar':
    exit();
pg.moveTo(700,700); #Coordenadas da caixa de texto
pg.leftClick();
for i in msg:
    pg.write(i);
pg.press('enter');