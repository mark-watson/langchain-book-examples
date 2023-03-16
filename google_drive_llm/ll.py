from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
from pathlib import Path

# good GD search docs: https://developers.google.com/drive/api/guides/search-files#all

# Authenticate with Google
gauth = GoogleAuth()
gauth.LocalWebserverAuth()
drive = GoogleDrive(gauth)

drive = GoogleDrive(gauth)

def list_files(dir_id='root'):
    " test file dir: title: testdata, id: 1TZ9bnL5XOPAvKACJw8VoKWdVJ4jeCszJ "
    file_list = drive.ListFile({'q': f"'{dir_id}' in parents and trashed=false"}).GetList()
    for file1 in file_list:
        print('title: %s, id: %s' % (file1['title'], file1['id']))
    return [[file1['title'], file1['id']] for file1 in file_list]

def create_test_file():
    file1 = drive.CreateFile({'title': 'Hello.txt'})  # Create GoogleDriveFile instance with title 'Hello.txt'.
    file1.SetContentString('Hello World!') # Set content of the file from given string.
    file1.Upload()

def download_file(file_id, dir_id='root'):
    file_list = drive.ListFile({'q': f"'{file_id}' in {dir_id} and trashed=false"}).GetList()
    print(file_list)
    file = file_list[0]
    content = file.GetContentString()

def test():
    #create_test_file()
    fl = list_files("1TZ9bnL5XOPAvKACJw8VoKWdVJ4jeCszJ")
    print(fl)
    for f in fl:
        print(f)
        title_id = download_file(f[1], "1TZ9bnL5XOPAvKACJw8VoKWdVJ4jeCszJ")
        print(title_id[1])
