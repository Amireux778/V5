import json
import os
import shutil

# 图片文件夹根目录
img_folder_root = r'D:\桌面\fudan考核\Tools\data'
# 新的图片文件夹路径
new_img_folder = r'D:\桌面\fudan考核\Tools\image'
# 新的txt文件夹路径
new_txt_folder = r'D:\桌面\fudan考核\Tools\label'


# 创建新的图片和txt文件夹
os.makedirs(new_img_folder, exist_ok=True)
os.makedirs(new_txt_folder, exist_ok=True)

# 遍历所有文件夹和图片文件
for folder_name in os.listdir(img_folder_root):
    folder_path = os.path.join(img_folder_root, folder_name)
    if os.path.isdir(folder_path):
        # 生成文件夹对应的文件名前缀
        file_prefix = folder_name + '_'

        json_path = os.path.join(folder_path, 'IR_label.json')
        with open(json_path, 'r', encoding='utf-8') as f:
            anno_data = json.load(f)
        exist_list = anno_data['exist']
        rect_list = anno_data['gt_rect']
        print(rect_list)
        print(len(rect_list))
        for img_filename in os.listdir(folder_path):
            # 判断文件是否为图片文件
            if img_filename.endswith('.jpg') or img_filename.endswith('.png'):
                # 生成新的文件名
                new_filename = file_prefix + img_filename
                new_img_filepath = os.path.join(new_img_folder, new_filename)
                new_txt_filepath = os.path.join(new_txt_folder, new_filename[:-4] + '.txt')

                # 计算当前图片对应的位置信息
                idx = int(os.path.splitext(img_filename)[0]) - 1
                if exist_list[idx] == 0:
                    content = ""
                else:
                    x, y, w, h = rect_list[idx]
                    center_x = x + w / 2
                    center_y = y + h / 2
                    norm_width = w / 640
                    norm_height = h / 512
                    content = f"{0} {center_x / 640:.6f} {center_y / 512:.6f} {norm_width:.6f} {norm_height:.6f}\n"

                # 将位置信息写入txt文件，并复制文件
                with open(new_txt_filepath, 'w') as f:
                    f.write(content)
                shutil.copy(os.path.join(folder_path, img_filename), new_img_filepath)
                # shutil.copy(new_txt_filepath, os.path.join(new_txt_folder, new_filename[:-4] + '.txt'))