import os
import random
from shutil import copyfile

# 指定数据集目录和输出目录
image_dir = r"D:\桌面\fudan考核\1\images"
label_dir = r"D:\桌面\fudan考核\1\labels"
output_dir = r"D:\桌面\fudan考核\2"

# 指定训练集、验证集和测试集的比例
train_ratio = 0.7
val_ratio = 0.2
test_ratio = 0.1

# 创建输出目录
os.makedirs(output_dir, exist_ok=True)
train_image_dir = os.path.join(output_dir, "train_images")
val_image_dir = os.path.join(output_dir, "val_images")
test_image_dir = os.path.join(output_dir, "test_images")
train_label_dir = os.path.join(output_dir, "train_labels")
val_label_dir = os.path.join(output_dir, "val_labels")
test_label_dir = os.path.join(output_dir, "test_labels")
os.makedirs(train_image_dir, exist_ok=True)
os.makedirs(val_image_dir, exist_ok=True)
os.makedirs(test_image_dir, exist_ok=True)
os.makedirs(train_label_dir, exist_ok=True)
os.makedirs(val_label_dir, exist_ok=True)
os.makedirs(test_label_dir, exist_ok=True)

# 获取图像和标注文件列表
image_list = sorted(os.listdir(image_dir))
label_list = sorted(os.listdir(label_dir))

# 将图像和标注文件列表合并
data_list = list(zip(image_list, label_list))

# 打乱数据集
random.shuffle(data_list)

# 计算数据集大小
data_size = len(data_list)

# 计算训练集、验证集和测试集的大小
train_size = int(data_size * train_ratio)
val_size = int(data_size * val_ratio)
test_size = data_size - train_size - val_size

# 将数据集分割成训练集、验证集和测试集
train_set = data_list[:train_size]
val_set = data_list[train_size:train_size+val_size]
test_set = data_list[train_size+val_size:]

# 将训练集、验证集和测试集的图像和标注文件复制到输出目录
for set_name, set_data, set_image_dir, set_label_dir in [("train", train_set, train_image_dir, train_label_dir),
                                                         ("val", val_set, val_image_dir, val_label_dir),
                                                         ("test", test_set, test_image_dir, test_label_dir)]:
    for image_file, label_file in set_data:
        # 复制图像文件
        src_image_file = os.path.join(image_dir, image_file)
        dst_image_file = os.path.join(set_image_dir, image_file)
        copyfile(src_image_file, dst_image_file)
        # 复制标注文件
        src_label_file = os.path.join(label_dir, label_file)
        dst_label_file = os.path.join(set_label_dir, label_file)
        copyfile(src_label_file, dst_label_file)