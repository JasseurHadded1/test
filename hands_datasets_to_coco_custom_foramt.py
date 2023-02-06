import json
from pprint import pprint
import cv2

#All this datasets are from "roboflow" (see: https://public.roboflow.com/ & https://universe.roboflow.com/)
#We'll keep the decomposition of train/val/set datasets
#All dataset are available for commercial-use according to roboflow


datasets_to_update = [1]

if 1 in datasets_to_update:
    # Dataset 1: american_sign_language_letters_v1 (https://public.roboflow.com/object-detection/american-sign-language-letters)
    train_annotation_json = json.load(open('data/american_sign_language_letters_v1/train/annotations_train_coco.json'))
    valid_annotation_json = json.load(open('data/american_sign_language_letters_v1/valid/annotations_valid_coco.json'))
    test_annotation_json = json.load(open('data/american_sign_language_letters_v1/test/annotations_test_coco.json'))

    #pprint(train_annotation_json.get('categories'))
    # pprint(train_annotation_json.get('annotations')[0])

    #we just need to detect the hand

    for json_file in [train_annotation_json, valid_annotation_json, test_annotation_json]:
        json_file['categories'] = [{'id': 0, 'name': 'hand'}]
        for annot in json_file['annotations']:
            annot['category_id'] = 0
            del annot['segmentation']

    # Write the output json
    with open("data/american_sign_language_letters_v1/train/annotations_train_coco_updated.json", "w") as outfile:
        outfile.write(json.dumps(train_annotation_json, indent=4))

    with open("data/american_sign_language_letters_v1/valid/annotations_valid_coco_updated.json", "w") as outfile:
        outfile.write(json.dumps(valid_annotation_json, indent=4))

    with open("data/american_sign_language_letters_v1/test/annotations_test_coco_updated.json", "w") as outfile:
        outfile.write(json.dumps(test_annotation_json, indent=4))

if 2 in datasets_to_update:
    # Dataset 2: cnv_total Computer Vision Project (https://universe.roboflow.com/opensource-zzhlk/cnv_total)
    train_annotation_json = json.load(open('data/cnv_total/train/annotations_train_coco.json'))
    valid_annotation_json = json.load(open('data/cnv_total/valid/annotations_valid_coco.json'))
    test_annotation_json = json.load(open('data/cnv_total/test/annotations_test_coco.json'))

    # pprint(train_annotation_json.get('categories'))
    # pprint(train_annotation_json.get('annotations')[0])

    #we just need to detect the hand

    for json_file in [train_annotation_json, valid_annotation_json, test_annotation_json]:
        json_file['categories'] = [{'id': 0, 'name': 'hand'}]
        for annot in json_file['annotations']:
            annot['category_id'] = 0
            del annot['segmentation']

    # Write the output json
    with open("data/cnv_total/train/annotations_train_coco_updated.json", "w") as outfile:
        outfile.write(json.dumps(train_annotation_json, indent=4))

    with open("data/cnv_total/valid/annotations_valid_coco_updated.json", "w") as outfile:
        outfile.write(json.dumps(valid_annotation_json, indent=4))

    with open("data/cnv_total/test/annotations_test_coco_updated.json", "w") as outfile:
        outfile.write(json.dumps(test_annotation_json, indent=4))



if 3 in datasets_to_update:
    #Dataset 3: egohands_public_v1 (https://public.roboflow.com/object-detection/hands)
    train_annotation_json = json.load(open('data/egohands_public_v1/train/annotations_train_coco.json'))
    valid_annotation_json = json.load(open('data/egohands_public_v1/valid/annotations_valid_coco.json'))
    test_annotation_json = json.load(open('data/egohands_public_v1/test/annotations_test_coco.json'))

    #pprint(train_annotation_json.get('categories'))
    #pprint(train_annotation_json.get('annotations')[0])

    for json_file in [train_annotation_json, valid_annotation_json, test_annotation_json]:
      json_file['categories'] = [{'id': 0, 'name': 'hand'}]
      for annot in json_file['annotations']:
        annot['category_id'] = 0
        del annot['segmentation']

    #Write the output json
    with open("data/egohands_public_v1/train/annotations_train_coco_updated.json", "w") as outfile:
        outfile.write(json.dumps(train_annotation_json, indent=4))

    with open("data/egohands_public_v1/valid/annotations_valid_coco_updated.json", "w") as outfile:
        outfile.write(json.dumps(valid_annotation_json, indent=4))

    with open("data/egohands_public_v1/test/annotations_test_coco_updated.json", "w") as outfile:
        outfile.write(json.dumps(test_annotation_json, indent=4))


if 4 in datasets_to_update:
    #Dataset 4: handdetecttest Image Dataset (https://universe.roboflow.com/robotichand/handdetecttest)
    train_annotation_json = json.load(open('data/handdetecttest_v1i/train/annotations_train_coco.json'))
    valid_annotation_json = json.load(open('data/handdetecttest_v1i/valid/annotations_valid_coco.json'))
    test_annotation_json = json.load(open('data/handdetecttest_v1i/test/annotations_test_coco.json'))

    # pprint(train_annotation_json.get('categories'))
    # pprint(train_annotation_json.get('annotations')[0])

    for json_file in [train_annotation_json, valid_annotation_json, test_annotation_json]:
      json_file['categories'] = [{'id': 0, 'name': 'hand'}]
      for annot in json_file['annotations']:
        annot['category_id'] = 0
        del annot['segmentation']

    #Write the output json
    with open("data/handdetecttest_v1i/train/annotations_train_coco_updated.json", "w") as outfile:
        outfile.write(json.dumps(train_annotation_json, indent=4))

    with open("data/handdetecttest_v1i/valid/annotations_valid_coco_updated.json", "w") as outfile:
        outfile.write(json.dumps(valid_annotation_json, indent=4))

    with open("data/handdetecttest_v1i/test/annotations_test_coco_updated.json", "w") as outfile:
        outfile.write(json.dumps(test_annotation_json, indent=4))

if 5 in datasets_to_update:
    #Dataset 5: two hand Computer Vision Project (https://universe.roboflow.com/nomac555/two-hand-lw9jy)
    train_annotation_json = json.load(open('data/two_hand_v5_two_hand_original/train/annotations_train_coco.json'))

    # pprint(train_annotation_json.get('categories'))
    # pprint(train_annotation_json.get('annotations')[0])

    for json_file in [train_annotation_json]:
      json_file['categories'] = [{'id': 0, 'name': 'hand'}]
      for annot in json_file['annotations']:
        annot['category_id'] = 0
        del annot['segmentation']

    #Write the output json
    with open("data/two_hand_v5_two_hand_original/train/annotations_train_coco_updated.json", "w") as outfile:
        outfile.write(json.dumps(train_annotation_json, indent=4))

if 6 in datasets_to_update:
    #Dataset 6: arabic_sign_language Image Dataset (https://www.kaggle.com/datasets/sabribelmadoui/arabic-sign-language-augmented-dataset)
    #Annotation format is different to other datasets
    annotation_json_v0 = {{
    "infos": {
        "description": "Arabic Sign Language ArSL dataset, from Kaggle",
        "url": "https://www.kaggle.com/datasets/sabribelmadoui/arabic-sign-language-augmented-dataset",
        "date_created": "2020-10-20T16:55:24+00:00"    },
    "licenses": [
        {
            "id": 0,
            "datasets_id": [0],
            "url": "https://creativecommons.org/publicdomain/zero/1.0/",
            "name": "Public Domain"
        },
        {
            "id": 1,
            "datasets_id": [1,2,3,4],
            "url": "https://creativecommons.org/licenses/by/4.0/",
            "name": "CC BY 4.0"
        }


    ],
    "categories": [
        {
            "id": 0,
            "name": "hand"
        }
    ],
    "images": [
    ],
    "annotations": [
    ]
}

    train_annotation_json = json.load(open('data/handdetecttest_v1i/train/annotations_train_coco.json'))
    valid_annotation_json = json.load(open('data/handdetecttest_v1i/valid/annotations_valid_coco.json'))
    test_annotation_json = json.load(open('data/handdetecttest_v1i/test/annotations_test_coco.json'))

    # pprint(train_annotation_json.get('categories'))
    # pprint(train_annotation_json.get('annotations')[0])

    for json_file in [train_annotation_json, valid_annotation_json, test_annotation_json]:
      json_file['categories'] = [{'id': 0, 'name': 'hand'}]
      for annot in json_file['annotations']:
        annot['category_id'] = 0
        del annot['segmentation']

    #Write the output json
    with open("data/handdetecttest_v1i/train/annotations_train_coco_updated.json", "w") as outfile:
        outfile.write(json.dumps(train_annotation_json, indent=4))

    with open("data/handdetecttest_v1i/valid/annotations_valid_coco_updated.json", "w") as outfile:
        outfile.write(json.dumps(valid_annotation_json, indent=4))

    with open("data/handdetecttest_v1i/test/annotations_test_coco_updated.json", "w") as outfile:
        outfile.write(json.dumps(test_annotation_json, indent=4))
