import pyautogui as pg
import time as tm

confirm = pg.confirm(title='Ver Posição, agora?',buttons=['Sim','Não']);
if confirm == 'Não':
    exit();
print('Posicao do Mouse: '+str(pg.position()));
tm.sleep(30);
