#TODO
# do this changes in below code

import json
import firebase_admin
from firebase_admin import firestore,storage
from firebase_admin import credentials

credential_json_file = 'file_name'
databaseURL = 'databaseURL'
storageBucket = 'storageBucket'

cred = credentials.Certificate(credential_json_file)
fa=firebase_admin.initialize_app(cred, {"databaseURL": databaseURL,'storageBucket':storageBucket})
fc=firebase_admin.firestore.client(fa)
db = firestore.client()
blob = storage.bucket(storageBucket).blob('firestore/path/to/save/image')
blob.upload_from_filename('path/to/image')
