import os
import shutil


path=input("Enter path: ")
files = [os.path.abspath(i) for i in list(os.walk(path))[0][2] ]

for file in files:
    if os.path.samefile(__file__, file):
        # dont do anything to current file
        continue

    filename,extension=os.path.splitext(file)
    extension = extension[1:]
    exten=""
    if extension in ('mp3', 'wav', 'flac', 'ogg', 'm4a', 'aac', 'raw', 'dct', 'wma', 'opus', 'ra', 'rm'):
        exten='Music or Audio'
    elif extension in ('mp4', 'mkv', 'flv', 'avi', 'mov', 'wmv', 'rmvb', 'm4v', 'mpg', '3gp'):
        exten='Videos and Movies'
    elif extension in ("xls","xlsx","xlsm","xlsb",".xlt","xltx","xltm",".xla","xlam","xll","xlw"):
        exten='Spreadsheets'
    elif extension in ('ppt','pptx'):
        exten='Presentation'    
    elif extension in ('doc', 'docx', 'pdf', 'txt', 'odt', 'rtf', 'tex', 'wps', 'wks', 'wpd'):
        exten='Documents'
    elif extension in ('exe', 'msi', 'app', 'dmg', 'apk', 'jar', 'deb', 'rpm', 'pkg', 'iso'):
        exten='Softwares'
    elif extension in ('zip', 'rar', '7z', 'tar', 'gz', 'bz2', 'xz', 'lz', 'z', 'iso'):
        exten='Compressed files'
    elif extension in('jpg', 'jpeg', 'png', 'gif', 'bmp', 'tiff', 'ico', 'jfif', 'webp', 'heif'):
        exten='Photos'
    elif extension=='ini':
        continue
    else:
        exten=extension

    if os.path.exists(path+'/'+exten):
        shutil.move(path+'/'+file, path+'/'+exten+'/'+file)
    else:
        os.makedirs(path+'/'+exten,)
        shutil.move(path+'/'+file, path+'/'+exten+'/'+file)