from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
from pathlib import Path

# Authenticate with Google
gauth = GoogleAuth()
gauth.LocalWebserverAuth()
drive = GoogleDrive(gauth)

drive = GoogleDrive(gauth)

def list_files():
    file_list = drive.ListFile({'q': "'root' in parents and trashed=false"}).GetList()
    for file1 in file_list:
        print('title: %s, id: %s' % (file1['title'], file1['id']))

def create_test_file():
    file1 = drive.CreateFile({'title': 'Hello.txt'})  # Create GoogleDriveFile instance with title 'Hello.txt'.
    file1.SetContentString('Hello World!') # Set content of the file from given string.
    file1.Upload()
    
def test():
    create_test_file()
    list_files()
