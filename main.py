# coding=utf8
import itchat
from apscheduler.schedulers.blocking import BlockingScheduler


itchat.auto_login()

sched = BlockingScheduler()


def my_job():
    itchat.send('Hello, filehelper', toUserName='filehelper')


sched.add_job(my_job, 'cron', hour='18', minute=10)
sched.start()

