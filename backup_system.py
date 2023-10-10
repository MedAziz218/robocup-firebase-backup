import os
import datetime

class BackupSystem:
    def __init__(self,backup_directory):
        if not os.path.exists(backup_directory):
            os.mkdir(backup_directory)
        self.backup_directory = backup_directory

    def get_last_created_backup_name(self):
        # Get a list of all files in the output directory
        files = os.listdir(self.backup_directory)
        
        # Sort the list of files by modification time (most recent first)
        files.sort(key=lambda x: os.path.getmtime(os.path.join(self.backup_directory, x)), reverse=True)
        
        # Return the name of the most recently created file
        if files: 
            return files[0]
        return None
    

    def get_last_created_backup_data(self):
        last_created_backup_name = self.get_last_created_backup_name()
        if last_created_backup_name:
            path = f'{self.backup_directory}/{last_created_backup_name}'
            with open(path, "r") as file:
                data = file.read() 
            return data
        return None
    

    def create_backup(self,data):
        current_time = datetime.datetime.now()
        
        # Format the date and time as a string
        formatted_time = current_time.strftime("%Y-%m-%d+%H.%M.%S")
        file_name = f"{formatted_time}.json"
        # Create a file with the formatted time as the name
        file_path = os.path.join(self.backup_directory, file_name)
        
        # Create and write some content to the file
        with open(file_path, "w") as file:
            file.write(data)

        return file_name
        
       
#-------------- TEST --------------#

def test():
    from time import sleep
    test_path = os.getcwd()  + '/test_backup'
    test = BackupSystem(test_path)
    test.create_backup("1")
    sleep(1)
    test.create_backup("2")
    sleep(1)
    test.create_backup("33333333333333333")

if __name__=='__main__':
    test()

