import os

def get_directory_size(directory):
      way = os.scandir(directory)
      total,file,dirs = 0,0,0
      for entry in way:
            if entry.is_file():
                  total += os.path.getsize(entry)
                  file += 1
            elif entry.is_dir():
                  total += get_directory_size(entry)[0]
                  file += get_directory_size(entry)[1]
                  dirs += 1
      return total,file,dirs


folder_path = os.path.abspath(os.path.join('..','..','Module14'))
total,file,dirs = get_directory_size(folder_path)
print('Размер каталога (в Кб):',total/1024,
      '\nКоличество подкаталогов:',dirs,
      '\nКоличество файлов:',file)
