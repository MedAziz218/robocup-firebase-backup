import firebase_admin
from firebase_admin import credentials,db
import json

class FireBaseAPI:
    def __init__(self):
        # Initialize Firebase Admin SDK with your credentials and database URL
        cred = credentials.Certificate('Cred_firebase.json')
        # Replace 'your-database-url' with your Firebase Realtime Database URL
        firebase_admin.initialize_app(cred, {'databaseURL': 'https://robocapp-517ab-default-rtdb.firebaseio.com' })
        # Get a reference to the Firebase Realtime Databasei
        ref = db.reference('/')
        self.ref = ref

    def fetchDB(self):
        data = self.ref.get()
        json_data = json.dumps(data, indent=4)
        return json_data



#-------------- TEST --------------#

if __name__ == '__main__':
    firebaseAPI = FireBaseAPI()
    data = firebaseAPI.fetchDB()    
    print(data)