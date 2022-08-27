# --- display_pic ---
import matplotlib.pyplot as plt
from PIL import Image
import numpy as np
import os

def display_pic(folder):
    fig = plt.figure(figsize=(30, 60))
    files = os.listdir(folder)
    files.sort()
    for i, file in enumerate(files):
        if file=='.ipynb_checkpoints':
           continue
        if file=='.DS_Store':
           continue
        img = Image.open(folder+'/'+file)    
        images = np.asarray(img)
        ax = fig.add_subplot(10, 5, i+1, xticks=[], yticks=[])
        image_plt = np.array(images)
        ax.imshow(image_plt)
        #name = os.path.splitext(file)
        ax.set_xlabel(file, fontsize=30)               
    plt.show()
    plt.close()


# --- reset_folder ---
import shutil

def reset_folder(path):
    if os.path.isdir(path):
      shutil.rmtree(path)
    os.makedirs(path,exist_ok=True)
