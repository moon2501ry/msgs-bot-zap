from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
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

class ZapBot():
    def __init__(self, browser: str | None = 'chrome'):
        self.__version__ = 'MBZ 2.0 version';
        match browser:
            case 'chrome':
                self.web = webdriver.Chrome();
            case 'firefoz':
                self.web = webdriver.Firefox();
            case 'edge':
                self.web = webdriver.Edge();
            case 'safari':
                self.web = webdriver.Safari();
        self.web.get('https://web.whatsapp.com/');
        while True:
            time.sleep(15);
            try:
                self.web.find_element(By.CSS_SELECTOR, 'div.xixxii4.x16p50fe.xnalus7.xqtp20y.x1plvlek.xryxfnj');
                print(self.__version__);
                break;
            except:
                print('Please log in. Or a ERROR occurred');
    
    def set_chat(self, user: str):
        try:
            search_ = self.web.find_element(By.CSS_SELECTOR, 'p.selectable-text.copyable-text.x15bjb6t.x1n2onr6');
            search_.send_keys(str(user) + Keys.ENTER);
        except:
            print('A ERROR occurred with the user chat');
    
    def send(self, msg: str | None = None):
        if msg is None:
            msg = self.__version__;
        try:
            send_ = self.web.find_element(By.CSS_SELECTOR, 'div._ak1r').find_element(By.CSS_SELECTOR, 'p.selectable-text.copyable-text.x15bjb6t.x1n2onr6');
            send_.send_keys(str(msg) + Keys.ENTER);
        except:
            print('A ERROR occurred with the message');

    def get_history(self):
        self.history_ = self.web.find_elements(By.CSS_SELECTOR, 'div._amk4._amkd._amk5');

    def wait(self, seconds):
        time.sleep(seconds);

    # def get_new_msg(self):
    #     time_ = datetime.now().strftime('%H:%M, %d/%m/%Y');
    #     for m in self.history_:
    #         if m.find_element(By.CSS_SELECTOR, 'div.copyable-text').get_attribute('data-pre-plain-text') == f'[{time_}] {self.user_}:':
    #             self.new_msg_ = m;
    #             self.new_msg_str = self.new_msg_.find_element(By.CSS_SELECTOR, 'span._ao3e.selectable-text.copyable-text').find_element(By.TAG_NAME, 'span').text;
    #             return self.new_msg_str;
    #         else:
    #             return 0;

if __name__ == '__main__':
    print("This code can't to be used like a main code. Please use with 'from mbz import ZapBot'.");