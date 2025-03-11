from mbz import ZapBot
from pymsgbox import *

nav = confirm("Selecione seu navegador:", "MBZ - Nav Select", ['edge','firefoz','chrome','safari']);
bot = ZapBot(nav);
mode = confirm("Modo de enviar:", "MBZ - Mode Select", ['Repetido','Arquivo','TXT','ZaWarudo']);
user = prompt("Nome do usuário do WhatsApp:", "MBZ - User Select");
bot.set_chat(user);
match mode:
    case "Repetido":
        msg = prompt("Mensagem a ser enviada repetidamente:", "MBZ - Message Select");
    case "Arquivo":
        msg = prompt("Arquivo a ser enviado repetidamente:", "MBZ - Archive Select");
    case "TXT":
        f_txt = prompt("Arquivo de texto '.txt':", "MBZ - TXT Archive Select")
        with open(f_txt, "r", encoding="utf-8") as txt:
            msgs = txt.readlines();
        for msg in msgs:
            bot.send(msg);
    case "ZaWarudo":
        num_msg = int(prompt("Quantidade de MUDAs:", "MBZ - Number Select"));
        for _ in range(num_msg):
            bot.send("MUDA");
        bot.send("ZA WARUDO!!!");
if mode == "Arquivo" or mode == "Repetido":
    num_msg = int(prompt("Número de mensagens a serem enviadas:", "MBZ - Number Select"));
    for _ in range(num_msg):
        bot.send(msg);
bot.wait(3);