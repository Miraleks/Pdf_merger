import os
import PyPDF2

# Папка, где хранятся PDF-файлы
folder_path = './data/'

# Создаем объект для записи итогового PDF
pdf_writer = PyPDF2.PdfMerger()

# Обходим все файлы в папке и объединяем только PDF
for filename in os.listdir(folder_path):
    if filename.endswith('.pdf'):
        file_path = os.path.join(folder_path, filename)
        with open(file_path, 'rb') as file:
            pdf_writer.append(file)

# Сохраняем объединенный PDF в папке
output_file_path = os.path.join(folder_path, 'merged.pdf')
with open(output_file_path, 'wb') as output_file:
    pdf_writer.write(output_file)

print(f"PDF-файлы из папки {folder_path} успешно объединены в 'merged.pdf'!")