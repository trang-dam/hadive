import os
import random
import lxml.etree as etree
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.image import imread
from PIL import Image
import pylab

def parse_xml(path):
    tree = etree.parse(path)
    obj_elems = tree.findall('object')
    boxes = []
    for obj in obj_elems:
        for ele in obj:
            box = []
            if ele.tag == 'name':
                label = ele.text
            if ele.tag == 'bndbox':
                for coor in ele:
                    box.append(int(coor.text))
                boxes.append((label, box))  
    return boxes
    
class compare_img(object):
    def __init__(self, orig_path, resized_path, img_num):
        self.orig_path = orig_path
        self.resized_path = resized_path
        self.img_num = img_num
        self.boxes = None

    def get_boxes(self):
        orig_xml = os.path.join(self.orig_path, 'Annotations', str(self.img_num) + '.xml')
        resized_xml = os.path.join(self.resized_path, 'Annotations', str(self.img_num) + '.xml')
        self.orig_boxes = parse_xml(orig_xml)
        self.resized_boxes = parse_xml(resized_xml)
    
    def visualize(self):
        orig_img = os.path.join(self.orig_path, 'JPEGImages', str(self.img_num) + '.jpg')
        resized_img = os.path.join(self.resized_path, 'JPEGImages', str(self.img_num) + '.jpg')
        orig = imread(orig_img)
        resized = imread(resized_img)
        fig, ([ax1, ax2]) = plt.subplots(nrows=1, ncols=2, figsize=(18, 6))
        
        ax1.imshow(orig)
        for box in map(lambda x: x[1], self.orig_boxes):
            ax1.add_patch(
                patches.Rectangle((box[0], box[3]),
                                  (box[2] - box[0]),
                                  (box[1] - box[3]),
                                  fill=False, edgecolor='red'))
        
        ax2.imshow(resized)
        for box in map(lambda x: x[1], self.resized_boxes):
            ax2.add_patch(
                patches.Rectangle((box[0], box[3]),
                                  (box[2] - box[0]),
                                  (box[1] - box[3]),
                                  fill=False, edgecolor='red'))
        pylab.show()

if __name__ == '__main__':
    test = compare_img('/Users/JordanVani/Documents/NYU/GRA/R-CNNs/VOC_Data/VOCdevkit2007/VOC2007/',
                   '/Users/JordanVani/Desktop', '000001')
    test.get_boxes()
    test.visualize()
