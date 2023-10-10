import pygsheets
import pandas as pd
from backup_system import BackupSystem
import os
import json

class GoogleSheetAPI:
    def __init__(self):
        gc = pygsheets.authorize(service_file='Cred_googlesheet.json')# authentificat google sheet
        sh = gc.open('robocup-sheet') #the parameter MUST be the same name that you fixed in the google sheet 
        self.wks = sh[0] #this selects the first worksheet

    def update_teams_sheet(self,whole_data_string):
        json_data = json.loads(whole_data_string)

        df= pd.DataFrame(data=json_data).T
        df = df.rename_axis("TEAMS")

        self.wks.set_dataframe(df,(2,2),copy_index=True, copy_head=True ) #(1,2) means :start from column 1 row 2




