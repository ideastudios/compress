import openpyxl
import zipfile
import os
import time

depress_path = './collection'


def extract_excel(file_path):
    extracted_file_path = os.path.join(depress_path, os.path.basename(file_path))
    if not os.path.exists(extracted_file_path):
        os.makedirs(extracted_file_path)
    z = zipfile.ZipFile(file_path, 'r')
    z.extractall(extracted_file_path)
    return extracted_file_path


def get_images(file_path):
    decompressed_media_path = f"{file_path}/xl/media"
    print(f'decompressed_media_path is {decompressed_media_path}')
    if os.path.exists(decompressed_media_path):
        contain_images = []
        for root, dirs, files in os.walk(decompressed_media_path):
            for file in files:
                temp = (file, os.path.join(root, file))
                contain_images.append(temp)
        print(contain_images)
        return contain_images
    else:
        return []


def get_scan_text(file_path):
    wb = openpyxl.load_workbook(file_path)
    sheet_names = wb.sheetnames
    print(sheet_names)


def zip_folder(folder_path):
    cur_folder, extension = os.path.splitext(folder_path)
    zip_path = f"{cur_folder}_{get_current_time()}_out{extension}"
    z = zipfile.ZipFile(zip_path, 'w')
    for root, dirs, files in os.walk(folder_path):
        temp_dir = root.replace(folder_path, '')
        for file in files:
            z.write(os.path.join(root, file), os.path.join(temp_dir, file))
        for cur_dir in dirs:
            z.write(os.path.join(root, cur_dir), os.path.join(temp_dir, cur_dir))
    z.close()
    return zip_path


def get_current_time():
    return time.strftime("%y%m%d%H%M%S", time.localtime())


if __name__ == "__main__":
    extracted_path = extract_excel('./1.xlsx')
    get_images(extracted_path)
    zip_folder(extracted_path)
