import time
import socket
import telegram
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, MessageHandler, Filters, Job

token = '37695xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxlPmU'
# Please ASK bot_farther to replace
channel = '-10xxxxxxxxx88'
# Find by Login in Web Telegram 
myname = socket.getfqdn(socket.gethostname())
myaddr = [(s.connect(('8.8.8.8', 53)), s.getsockname()[0], s.close()) for s in [socket.socket(socket.AF_INET, socket.SOCK_DGRAM)]][0][1]
# myaddr = socket.gethostbyname(myname)

def send2Channel(messages=None):
    updater = Updater(token=token)
    bot = telegram.Bot(token=token)
    jober = updater.job_queue
    dispatcher = updater.dispatcher
    bot.send_message(channel,str(messages))

def read5Kernel():
    fd = open("/proc/net/dev", "r")
    for line in fd.readlines():
        if line.find("em1") > 0:
            recv=int(line.split()[1])/1024/1024
            send=int(line.split()[9])/1024/1024
    fd.close()
    return (float(recv),float(send))

def netNow():
    (recv,send) = read5Kernel()
    time.sleep(1)
    (recv_new,send_new) = read5Kernel()
    if recv_new-recv>80 or send_new-send>80:
        send2Channel(messages="warming!!!"+"HOST: "+myname+"IP: "+myaddr+"\n"+"NIC: "+str(recv_new-recv)+"Mbit/s"+"    "+str(send_new-send)+"Mbit/s")

if __name__ == '__main__':
    netNow()
    exit()
