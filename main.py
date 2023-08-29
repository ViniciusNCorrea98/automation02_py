import os
from tkinter.filedialog import askdirectory

root = askdirectory(title='Selecione um diretorio')
list_files = os.listdir(root)

locals= {
    'images': ['.png', '.jpeg', 'jpg'],
    'tables': ['.xlsx'],
    'PDFs': ['.pdf'],
    'csv': ['.csv'],
    'videos': ['.mp4'],
}

for file in list_files:

    name, extension = os.path.splitext(f'{root}/{file}')
    for folder in locals:
        if extension in locals[folder]:
            if not os.path.exists(f'{root}/{folder}'):
                os.mkdir(f'{root}/{folder}')
            os.rename(f'{root}/{file}', f'{root}/{folder}/{file}')