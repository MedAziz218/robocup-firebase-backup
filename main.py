import threading
import os
from time import sleep
from firebaseAPI import FireBaseAPI
#-------# My Imports #-------#
from flask_folder.app import app,FlaskAppConfig
from backup_system import BackupSystem

subpath = lambda x:  os.getcwd() + '/' + x
if not os.path.exists(subpath('backups')):
    os.mkdir(subpath('backups'))
if not os.path.exists(subpath('logs')):
    os.mkdir(subpath('logs'))

database = FireBaseAPI()
backup_sys = BackupSystem(subpath('backups'))
FlaskAppConfig.FILES_DIR = subpath('backups') 



def main_loop():
    counter = 0
    while True:
        counter+=1
        try:
            db_content = database.fetchDB()
            last_backup = backup_sys.get_last_created_backup_data()
            
            if (db_content != last_backup):
                fn = backup_sys.create_backup(db_content)
                print(f"({counter}) Created file: {fn}")      
            else:
                print(f"({counter}) No backup needed")

        except Exception as e:
            print(e)

        sleep(5)

if __name__=='__main__':
    threading.Thread(target=lambda: app.run(  debug=False, use_reloader=False),daemon=True).start()
    main_loop()