from aiogram.utils import executor
import logging
from config import db
from handler import client, callback, admin, extra, fsm_anketa

callback.reg_hand_callback(db)
admin.reg_ban(db)
extra.reg_hand_extra(db)
client.reg_client(db)
fsm_anketa.reg_hand_anketa(db)

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(db, skip_updates=True)
