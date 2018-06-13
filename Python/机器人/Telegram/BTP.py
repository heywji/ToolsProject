import time
import socket
import telegram
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, MessageHandler, Filters, Job

token = '376950264:xxxxxxx-KL55QtQGhFlPmU'
channel = '-xxxxxxxxxxxx'
myname = socket.getfqdn(socket.gethostname())
myaddr = socket.gethostbyname(myname)

def send2Channel(messages=None):
    updater = Updater(token=token)
    bot = telegram.Bot(token=token)
    jober = updater.job_queue
    dispatcher = updater.dispatcher
    bot.send_message(channel,str(messages))

def read5Kernel():
    fd = open("/proc/net/dev", "r")
    for line in fd.readlines():
        if line.find("net") > 0:
            recv=int(line.split()[2])/1024
            send=int(line.split()[10])/1024
    fd.close()
    return (float(recv),float(send))

def netNow():
    (recv,send) = read5Kernel()
    time.sleep(1)
    (recv_new,send_new) = read5Kernel()
    if recv_new-recv>80 or send_new-send>80:
        send2Channel(messages=myname+myaddr+"warming")
        send2Channel(messages="net0: "+str(recv_new-recv)+"Mbit/s"+"    "+str(send_new-send)+"Mbit/s")

if __name__ == '__main__':
    netNow()
    exit()
