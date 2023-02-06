# import json
#
# train_annotation_json = json.load(open('data/american_sign_language_letters_v1/test/annotations_test_coco.json'))
#
# images_id_to_delete = []
#
# images = []
# for image in train_annotation_json.get('images'):
#     if image.get('file_name')[0] == 'Y':
#         images_id_to_delete.append(image.get('id'))
#     else:
#         images.append(image)
#
# train_annotation_json['images'] = images
#
# print(type(images_id_to_delete[0]))
#
# annotations = []
#
# for annot in train_annotation_json.get('annotations'):
#     if annot.get('image_id') not in images_id_to_delete:
#         annotations.append(annot)
#
# train_annotation_json['annotations'] = annotations
#
# with open("data/american_sign_language_letters_v1/test/annotations_test_coco_v1.json", "w") as outfile:
#     outfile.write(json.dumps(train_annotation_json, indent=4))

import cv2

image = cv2.imread("data/arabic_sign_language/train/images/IMG_20210609_184853_jpg.rf.0cc4ccc2a6d8873a0c57570ead4e2c2a.jpg")
# print(image.shape)
label = [0.5540865384615384, 0.5913461538461539, 0.46153846153846156, 0.46875]
label = [416 - int(x*416) for x in label]
print(label)
label = [230, 246, 192, 195]
# label = [186, 170, 224, 221]

# label = [186, 246, 224, 195]

image = cv2.rectangle(image,
                      (label[0], label[1]),
                      (label[2] + label[0], label[1] + label[3]),
                      (36,255,12),
                      1)
cv2.imshow('image', image)
cv2.waitKey(0)

# closing all open windows
cv2.destroyAllWindows()