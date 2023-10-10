import threading
import os
from time import sleep
from firebaseAPI import FireBaseAPI
#-------# My Imports #-------#
from flask_folder.app import app,FlaskAppConfig
from backup_system import BackupSystem
from googlesheetAPI import GoogleSheetAPI


subpath = lambda x:  os.getcwd() + '/' + x
if not os.path.exists(subpath('backups')):
    os.mkdir(subpath('backups'))
if not os.path.exists(subpath('logs')):
    os.mkdir(subpath('logs'))

database = FireBaseAPI()
googlesheet = GoogleSheetAPI()

backup_sys = BackupSystem(subpath('backups'))
FlaskAppConfig.FILES_DIR = subpath('backups') 


def update_google_sheet(whole_dbcontent_string=None):
    if not whole_dbcontent_string:
        whole_dbcontent_string = backup_sys.get_last_created_backup_data()
    if whole_dbcontent_string:
        threading.Thread(target=lambda:googlesheet.update_teams_sheet(whole_dbcontent_string),daemon=True).start()
    else: 
        raise Exception("something went wrong")
    
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
                
                update_google_sheet(db_content)
                


            else:
                print(f"({counter}) No backup needed")

        except Exception as e:
            print(e)

        sleep(5)

if __name__=='__main__':
    threading.Thread(target=lambda: app.run(  debug=False, use_reloader=False),daemon=True).start()
    main_loop()