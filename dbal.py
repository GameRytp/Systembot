from vedis import Vedis
import config


# Пытаемся узнать из базы «состояние» пользователя
def get_current_state(user_id):
    with Vedis(config.dbFile) as db:
        try:
            return db[user_id].decode() # Если используете Vedis версии ниже, чем 0.7.1, то .decode() НЕ НУЖЕН
        except KeyError:  # Если такого ключа почему-то не оказалось
            return config.States.sStart.value  # значение по умолчанию - начало диалога


# Сохраняем текущее «состояние» пользователя в нашу базу
def set_state(user_id):
    with Vedis(config.dbFile) as db:
        try:
            db[user_id] = 0
            return True
        except:
            # тут желательно как-то обработать ситуацию
            return False

def setStation(user_id, value):
    with Vedis(config.dbStation) as db:
        try:
            db[user_id] = value
            return True
        except:
            # тут желательно как-то обработать ситуацию
            return False

def plusState(user_id):
    with Vedis(config.dbFile) as db:
        try:
            db[user_id] = int(db[user_id])+1
            return True
        except:
            # тут желательно как-то обработать ситуацию
            return False

def out(user_id):
    with Vedis(config.dbFile) as db:
        try:
            return db[user_id]
        except:
            # тут желательно как-то обработать ситуацию
            return False

def outStation(user_id):
    with Vedis(config.dbStation) as db:
        try:
            return db[user_id]
        except:
            # тут желательно как-то обработать ситуацию
            return False

def letnext(user_id):
    with Vedis(config.dbChek) as db:
        try:
            db[user_id] = "1"
            return True
        except:
            # тут желательно как-то обработать ситуацию
            return False

def nonext(user_id):
    with Vedis(config.dbChek) as db:
        try:
            db[user_id] = "0"
            return True
        except:
            # тут желательно как-то обработать ситуацию
            return False

def checknext(user_id):
    with Vedis(config.dbChek) as db:
        try:
           
            return bool(int(db[user_id]))
        except:
            # тут желательно как-то обработать ситуацию
            return False

def setline(user_id, value):
    with Vedis(config.dbline) as db:
        try:
            db[user_id] = value
            return True
        except:
            # тут желательно как-то обработать ситуацию
            return False

def outline(user_id):
    with Vedis(config.dbline) as db:
        try:
            return int(db[user_id])
        except:
            # тут желательно как-то обработать ситуацию
            return False