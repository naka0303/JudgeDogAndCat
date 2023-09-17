import os
import glob
import random
import shutil

DATASET_DIRPATH = os.path.join(os.path.dirname(__file__), '../dataset/original')
TRAIN_DIRPATH = os.path.join(os.path.dirname(__file__), '../dataset/train')
VALIDATION_DIRPATH = os.path.join(os.path.dirname(__file__), '../dataset/validation')
SAMPLING_RATIO = 0.7 # 0〜1の範囲内で指定すること

def split():
    ## 犬画像分割処理
    # 犬画像ファイルパス取得
    dogs_dataset = glob.glob(DATASET_DIRPATH + '/dogs' + '/*.jpg')

    # 指定した割合の犬画像をサンプリング
    dogs_dataset_train = random.sample(dogs_dataset, int(len(dogs_dataset) * SAMPLING_RATIO))
    dogs_dataset_valid = list(set(dogs_dataset) ^ set(dogs_dataset_train))

    # サンプリングした犬画像をtrainディレクトリ下にコピー
    for img_path in dogs_dataset_train:
         shutil.copy2(img_path, TRAIN_DIRPATH + '/dogs/')

    # 残りの犬画像をvalidationディレクトリ下にコピー
    for img_path in dogs_dataset_valid:
         shutil.copy2(img_path, VALIDATION_DIRPATH + '/dogs/')

    ## 猫画像分割処理
    # 猫画像ファイルパス取得
    cats_dataset = glob.glob(DATASET_DIRPATH + '/cats' + '/*.jpg')

    # 指定した割合の猫画像をサンプリング
    cats_dataset_train = random.sample(cats_dataset, int(len(cats_dataset) * SAMPLING_RATIO))
    cats_dataset_valid = list(set(cats_dataset) ^ set(cats_dataset_train))

    # サンプリングした猫画像をtrainディレクトリ下にコピー
    for img_path in cats_dataset_train:
         shutil.copy2(img_path, TRAIN_DIRPATH + '/cats/')

    # 残りの猫画像をvalidationディレクトリ下にコピー
    for img_path in cats_dataset_valid:
         shutil.copy2(img_path, VALIDATION_DIRPATH + '/cats/')

if __name__ == '__main__':
    split()
