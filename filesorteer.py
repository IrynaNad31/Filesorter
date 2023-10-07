import os
import shutil
from concurrent.futures import ThreadPoolExecutor


def process_folder(src_folder, dest_folder):
    items = os.listdir(src_folder)

    for item in items:
        item_path = os.path.join(src_folder, item)
        if os.path.isfile(item_path):
            _, file_extension = os.path.splitext(item)

            dest_extension_folder = os.path.join(
                dest_folder, file_extension[1:])
            os.makedirs(dest_extension_folder, exist_ok=True)
            shutil.move(item_path, os.path.join(dest_extension_folder, item))

        elif os.path.isdir(item_path):
            with ThreadPoolExecutor() as executor:
                executor.submit(process_folder, item_path, dest_folder)


if __name__ == "__main__":
    src_folder = r'D:\GoIT\Хлам'
    dest_folder = r'D:\GoIT\Хлам'

    os.makedirs(dest_folder, exist_ok=True)

    with ThreadPoolExecutor() as executor:
        executor.submit(process_folder, src_folder, dest_folder)

    print("Сортування завершено.")
