from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
from pathlib import Path

# good GD search docs: https://developers.google.com/drive/api/guides/search-files#all

# Authenticate with Google
gauth = GoogleAuth()
gauth.LocalWebserverAuth()
drive = GoogleDrive(gauth)

drive = GoogleDrive(gauth)

def get_txt_files(dir_id='root'):
    " get all plain text files with .txt extension in top level Google Drive directory "

    file_list = drive.ListFile({'q': f"'{dir_id}' in parents and trashed=false"}).GetList()
    for file1 in file_list:
        print('title: %s, id: %s' % (file1['title'], file1['id']))
    return [[file1['title'], file1['id'], file1.GetContentString()]
            for file1 in file_list if file1['title'].endswith(".txt")]

def create_test_file():
    " not currently used, but useful for testing. "

    # Create GoogleDriveFile instance with title 'Hello.txt':
    file1 = drive.CreateFile({'title': 'Hello.txt'})
    file1.SetContentString('Hello World!')
    file1.Upload()

def test():
    fl = get_txt_files()
    for f in fl:
        print(f)
        file1 = open("data/" + f[0],"w")
        file1.write(f[2])
        file1.close()

if __name__ == '__main__':
    test()
