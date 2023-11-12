# Google Drive File Uploader

Цей скрипт написаний на мові програмування Python та використовує бібліотеку PyDrive для завантаження файлів на Google Drive. Скрипт має дві основні функції:

1.'create_and_upload_file': Завантажує один файл на Google Drive. Ви можете вказати ім'я файлу та його вміст. За замовчуванням, ім'я файлу - 'test.txt', а вміст - 'Hey Mark!'.

2.'upload_dir': Завантажує всі файли з вказаного каталогу на Google Drive. Ім'я кожного файлу визначається його оригінальним ім'ям. Шлях до каталогу передається як аргумент функції.

# Як користуватися
1.Встановіть необхідні бібліотеки, використовуючи команду:
```
pip install PyDrive

```
2.Запустіть скрипт, використовуючи Python. Вам слід викликати функцію main(), яка зараз викликає функцію upload_dir для завантаження всіх файлів з вказаного каталогу на Google Drive.
```
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
import os

def authenticate_google_drive():
    """
    Автентифікація в Google Drive. Використовується Local Webserver Authentication.
    """
    gauth = GoogleAuth()
    gauth.LocalWebserverAuth()
    return gauth

def create_and_upload_file(file_name='test.txt', file_content='Hey Mark!'):
    """
    Завантаження одного файлу на Google Drive.

    :param file_name: Ім'я файлу для завантаження. За замовчуванням - 'test.txt'.
    :param file_content: Вміст файлу. За замовчуванням - 'Hey Mark!'.
    :return: Повідомлення про успішне завантаження або повідомлення про помилку.
    """
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
    """
    Завантаження всіх файлів з вказаного каталогу на Google Drive.

    :param dir_path: Шлях до каталогу з файлами для завантаження.
    :return: Повідомлення про успішне завантаження або повідомлення про помилку.
    """
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
    # Приклад виклику функції upload_dir для завантаження файлів з вказаного каталогу.
    print(upload_dir(dir_path='D:\\програмування\\Python\\загрузка файлів з google drive\\files'))

if __name__ == '__main__':
    main()

```

# Зауваження
Переконайтеся, що у вас є доступ до Інтернету під час використання скрипта, оскільки він взаємодіє з Google Drive через API.

# Ліцензія
Цей проект поширюється під ліцензією MIT - детальніше читайте в файлі LICENSE.

Долучайте свої внески та відправляйте питання через розділ Issues. Бажаємо вам продуктивного використання!
