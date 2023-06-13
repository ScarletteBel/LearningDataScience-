import tensorflow as tf 

from tensorflow.keras import datasets, layers, models 
import matplotlib.pyplot as plt


(train_images, train_labels), (test_images, test_labels) = datasets.cifar10.load_data()

train_images, test_images = train_images/255, test_images/255


train_images[1].shape
print(train_images)


class_names = ['airplane', 'automobile', 'bird', 'cat', 'deer', 'dog', 'frog', 'horse', 'ship', 'truck']

plt.figure(figsize=(5,5))


#..


model = models.Sequential()
model.add(layers.Conv2D(32(3,3), activation= ))



