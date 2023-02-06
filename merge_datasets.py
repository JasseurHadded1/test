import os
import json
from tqdm import tqdm
from pprint import  pprint
import copy


copy_images = False

annotation_json = json.load(open('data/full_data/annotations_coco_v0.json'))


for mode in ['train', 'valid', 'test']:
    print("Mode:", mode)
    image_id = 0
    annotation_id = 0
    for idx, dataset_name in enumerate(['american_sign_language_letters_v1', 'cnv_total', 'egohands_public_v1', 'handdetecttest_v1i',
                     'two_hand_v5_two_hand_original']):
        print("Dataset:", dataset_name)
        dataset_path = os.path.join('data', dataset_name)
        if os.path.isdir(dataset_path):
            mode_path = os.path.join(dataset_path, mode)
            if os.path.isdir(mode_path):
                if copy_images:
                    for image in tqdm(os.listdir(mode_path)):
                        if image.split('.')[-1] != 'json':
                            image_path = os.path.join(mode_path, image)
                            output_path = "data/full_data/{}/{}".format(mode, image)
                            os.system("cp {} {}".format(image_path, output_path))

                #Combine Jsons
                json_file = json.load(open(os.path.join(mode_path, 'annotations_{}_coco_updated.json'.format(mode))))
                img_old_id_to_new_id = {}
                for img in json_file.get('images'):
                    new_img = dict(img)
                    new_img["dataset_id"] = idx
                    new_img['id'] = image_id
                    img_old_id_to_new_id[img.get('id')] = new_img.get('id')
                    annotation_json['images'].append(new_img)
                    image_id +=1

                for annot in json_file.get('annotations'):
                    new_annot = dict(annot)
                    new_annot["dataset_id"] = idx
                    new_annot['id'] = annotation_id
                    new_annot['image_id'] = img_old_id_to_new_id[annot['image_id']]
                    annotation_json['annotations'].append(new_annot)
                    annotation_id +=1

    # Write the output json
    with open("data/full_data/{}/annotations_{}_coco.json".format(mode, mode), "w") as outfile:
        outfile.write(json.dumps(annotation_json, indent=4))
