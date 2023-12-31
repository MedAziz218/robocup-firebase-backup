import os
import time
from flask import Flask, render_template, send_file

app = Flask(__name__)
app.debug = False
app.use_reloader=False
current_directory = os.getcwd()

print("Current Working Directory:", current_directory)
class FlaskAppConfig:
    FILES_DIR = current_directory+ ""
    UPDATE_SHEET_FUNCTION = None
def background_function():
    if not FlaskAppConfig.UPDATE_SHEET_FUNCTION:
        return "Something went Wrong (too soon)"
    try:
        FlaskAppConfig.UPDATE_SHEET_FUNCTION()
    except:
        return "Something went horribly Wrong"
    
    return "Sheet Updated Successfully"

@app.route('/')
def file_list():
    # List all files in the directory
    # files = os.listdir(FlaskAppConfig.FILES_DIR)
    files = [entry.name for entry in os.scandir(FlaskAppConfig.FILES_DIR) if entry.is_file()]
    files.sort(reverse=True)
    return render_template('file_list.html', files=files)

@app.route('/view/<filename>')
def view_file(filename):
    # Construct the full path to the selected file
    file_path = os.path.join(FlaskAppConfig.FILES_DIR, filename)
    # Return the file as an attachment
    return send_file(file_path)

@app.route('/download/<filename>')
def download_file(filename):
    # Construct the full path to the selected file
    file_path = os.path.join(FlaskAppConfig.FILES_DIR, filename)
    # Return the file for download
    return send_file(file_path, as_attachment=True)

@app.route('/background_task', methods=['POST'])
def start_background_task():
    result = background_function()
    return result



#-------------- TEST --------------#
if __name__=='__main__':
    app.debug = True
    app.use_reloader=True
    app.run()