from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
import os

def authenticate_google_drive():
    gauth = GoogleAuth()
    gauth.LocalWebserverAuth()
    return gauth

def create_and_upload_file(file_name='test.txt', file_content='Hey Mark!'):
    try:
        gauth = authenticate_google_drive()
        drive = GoogleDrive(gauth)

        my_file = drive.CreateFile({'title': file_name})
        my_file.SetContentString(file_content)
        my_file.Upload()

        return f'File {file_name} was uploaded! Have a good day!'
    except Exception as ex:
        return f'Got some trouble: {ex}'
    

def upload_dir(dir_path):
    try:
        gauth = authenticate_google_drive()
        drive = GoogleDrive(gauth)
        
        for file_name in os.listdir(dir_path):

            my_file = drive.CreateFile({'title': file_name})
            my_file.SetContentFile(os.path.join(dir_path, file_name))
            my_file.Upload()
            
            print(f'File {file_name} was uploaded!')
            
        return f'Success! Have a good day!'
    except Exception as ex:
        return f'Got some trouble: {ex}'



def main():
    # print(create_and_upload_file(file_name='hello.txt', file_content='Hello World'))
   print(upload_dir(dir_path='D:\\програмування\\Python\\загрузка файлів з google drive\\files'))

if __name__ == '__main__':
    main()
