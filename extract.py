import os
import shutil

def extract_images(source_folder, target_folder):
    """
    Извлекает все изображения из исходной папки и копирует их в целевую папку.
    
    :param source_folder: Путь к исходной папке с подпапками
    :param target_folder: Путь к целевой папке для изображений
    """
    # Создаем целевую папку, если она не существует
    os.makedirs(target_folder, exist_ok=True)
    
    # Проходим по всем файлам и подпапкам в исходной папке
    for root, dirs, files in os.walk(source_folder):
        for file in files:
            # Проверяем, является ли файл изображением (по расширению)
            if file.lower().endswith(('.jpg', '.jpeg', '.png', '.bmp', '.gif')):
                # Полный путь к исходному файлу
                src_path = os.path.join(root, file)
                # Путь для целевого файла (чтобы избежать конфликтов имен)
                dst_path = os.path.join(target_folder, file)
                
                # Если файл с таким именем уже существует, добавляем суффикс
                counter = 1
                while os.path.exists(dst_path):
                    name, ext = os.path.splitext(file)
                    dst_path = os.path.join(target_folder, f"{name}_{counter}{ext}")
                    counter += 1
                
                # Копируем файл
                shutil.copy2(src_path, dst_path)
                print(f"Скопировано: {src_path} -> {dst_path}")

# Пример использования

import torch
print(torch.__version__)            # PyTorch version
print(torch.cuda.is_available())    # Should return True if fixed
print(torch.cuda.get_device_name(0))  # Name of your GPU
if __name__ == "__main__":
    # source_folder = "../veri/veri"  # Замените на ваш путь
    # target_folder = "/veri776_ds"    # Замените на ваш путь
    # extract_images(source_folder, target_folder)
    # print("Все изображения успешно извлечены!")
    print(torch.cuda.is_available())