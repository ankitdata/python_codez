"""
this file will help to download images from firebase storage
make changes in TODO
"""

#TODO
credential_json_file = ['file_name.json']
databaseURL = ['databaseURL']
storageBucket = ['storageBucket']

if (not len(firebase_admin._apps)):
    cred = credentials.Certificate(credential_json_file)
    fa=firebase_admin.initialize_app(cred, {"databaseURL": databaseURL,'storageBucket':storageBucket})
    fc=firebase_admin.firestore.client(fa)
    db = firestore.client()
blob = storage.bucket(storageBucket).blob(url) # this will download image from url
blob.download_to_filename('path/to/save/image.jpeg') # change extension to your image extension eg.png/jpg or any
