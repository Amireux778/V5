import os
import shutil

def copy_txt_files(source_folder, destination_folder):
    # 创建目标文件夹
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)

    # 遍历源文件夹及其子文件夹
    for root, dirs, files in os.walk(source_folder):
        for file in files:
            # 检查文件扩展名是否为txt
            if file.endswith(".txt"):
                # 构建源文件的完整路径
                source_path = os.path.join(root, file)
                # 构建目标文件的完整路径
                destination_path = os.path.join(destination_folder, file)
                # 复制文件到目标文件夹
                shutil.copy(source_path, destination_path)

# 示例用法
source_folder = r"D:\AAA\1\res_test"
destination_folder = r"D:\AAA\1\res_txt"

copy_txt_files(source_folder, destination_folder)
