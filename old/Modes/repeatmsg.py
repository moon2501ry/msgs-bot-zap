import pyautogui as pg

msg = pg.prompt(text='Mensagem:',title='Simple Mode');
rng = pg.prompt(text='Número de msgs:',title='Simple Mode');
bg = pg.confirm(text='Começar?',title='Simple Mode',buttons=['Sim','Fechar']);
if bg == 'Fechar':
    exit();
pg.moveTo(700,700); #Coordenadas da caixa de texto
pg.leftClick();
for i in range(int(rng)):
    pg.write(msg);
    pg.press('enter');