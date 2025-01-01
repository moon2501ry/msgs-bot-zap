from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

class ZapBot():
    def __init__(self, browser: str):
        match browser:
            case 'chrome':
                self.web = webdriver.Chrome();
            case 'firefoz':
                self.web = webdriver.Firefox();
            case 'edge':
                self.web = webdriver.Edge();
            case 'safari':
                self.web = webdriver.Safari();
            case '':
                self.web = webdriver.Chrome();
        self.web.get('https://web.whatsapp.com/');
    
    def send(self, user: str, msg: str):
        while True:
            time.sleep(15);
            try:
                login_ = self.web.find_element(By.CSS_SELECTOR, 'div._aigw.x9f619.x1n2onr6.x5yr21d.x17dzmu4.x1i1dayz.x2ipvbc.x1w8yi2h.x78zum5.xdt5ytf.xa1v5g2.x1plvlek.xryxfnj.xd32934');
                print('Ready');
                break;
            except:
                print('Please log in. Or a ERROR occurred');
        try:
            search_ = self.web.find_element(By.CSS_SELECTOR, 'p.selectable-text.copyable-text.x15bjb6t.x1n2onr6');
            search_.send_keys(str(user) + Keys.ENTER);
            send_ = self.web.find_element(By.CSS_SELECTOR, 'div._ak1r').find_element(By.CSS_SELECTOR, 'p.selectable-text.copyable-text.x15bjb6t.x1n2onr6');
            send_.send_keys(str(msg) + Keys.ENTER);
        except:
            print('A ERROR occurred')