import pyautogui as pg
import subprocess as sbp

mode = pg.confirm(text='Modo:',title='Auto Messages',buttons=['Simple','Music','ZaWarudo']);
match mode:
    case 'Simple':
        sbp.run("python Modes/repeatmsg.py");
    case 'Music':
        sbp.run("python Modes/music.py");
    case 'ZaWarudo':
        sbp.run("python Modes/zawarudo.py");