import fitz
from pathlib import Path
import telebot
import time

path = r'path\to\the\folder\which\contains\books\in\pdf\format'
token = 'TOKEN'
chat_id = "@chat_link"

bot = telebot.TeleBot(token)
folder_path = Path(path)

books_paths = [str(file_path) for file_path in folder_path.iterdir() if file_path.is_file() and file_path.suffix == '.pdf']
images_paths = [fr'{i[:-3]}jpg' for i in books_paths]

for i in books_paths:
    file = fitz.open(fr'{i}')
    page = file[0]
    pix = page.get_pixmap(dpi=150)
    pix.save(fr'{i[:-3]}jpg')
    file.close()


for image_path, pdf_path in zip(images_paths, books_paths):
    try:
        with open(image_path, 'rb') as image_file:
            bot.send_photo(chat_id, image_file)
        
        with open(pdf_path, 'rb') as pdf_file:
            bot.send_document(chat_id, pdf_file)
        time.sleep(3)
    except Exception as e:
        print(f"Error sending files: {e}")

print("DONE")
