"""basic_classification
"""
# TensorFlow and tf.keras
import tensorflow as tf

# Helper libraries
import numpy as np
import matplotlib.pyplot as plt
from math import sqrt

print(tf.__version__)

__author__ = "help@castellanidavide.it"
__version__ = "1.0 2020-12-30"

class basic_classification:
	def __init__ (self):
		"""Where it all begins
		"""
		self.load_model()
		self.print_some_model_infos()
		#self.show_img()
		self.create_the_model()
		self.feed_model()
		self.check_accuracy()
	
	def load_model(self):
		"""Load the model
		"""
		self.fashion_mnist = tf.keras.datasets.fashion_mnist

		(self.train_images, self.train_labels), (self.test_images, self.test_labels) = self.fashion_mnist.load_data()
		self.train_images = self.train_images / 255.0
		self.test_images = self.test_images / 255.0
		
		self.class_names = ['T-shirt/top', 'Trouser', 'Pullover', 'Dress', 'Coat',
               'Sandal', 'Shirt', 'Sneaker', 'Bag', 'Ankle boot']

	def print_some_model_infos(self):
		"""Prints some infos from the model
		"""
		print(f"Shape: {self.train_images.shape}")
		print(f"Len: {len(self.train_labels)}")
		print(f"Labels: {self.train_labels}")
		print(f"Test shape: {self.test_images.shape}")
		print(f"Test len: {len(self.test_labels)}")

	def show_img(self):
		"""Preprocess the data
		"""
		# Only one
		"""plt.figure()
		plt.imshow(self.train_images[0])
		plt.colorbar()
		plt.grid(False)
		plt.show()"""

		# Grind
		plt.figure(figsize=(10,10))
		n_photos = 30
		for i in range(n_photos):
			plt.subplot(int(sqrt(n_photos)), n_photos / int(sqrt(n_photos)), i + 1)
			plt.xticks([])
			plt.yticks([])
			plt.grid(False)
			plt.imshow(self.train_images[i])
			plt.xlabel(f"{i}) {self.class_names[self.train_labels[i]]}")
		plt.show()

	def create_the_model(self):
		"""Creates the module
		"""
		self.model = tf.keras.Sequential([
			tf.keras.layers.Flatten(input_shape=(28, 28)),
			tf.keras.layers.Dense(128, activation='relu'),
			tf.keras.layers.Dense(10)
		])

		self.model.compile(optimizer='adam',
              loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
              metrics=['accuracy'])

	def feed_model(self):
		"""Fit my personal model
		"""
		self.model.fit(self.train_images, self.train_labels, epochs=10)

	def check_accuracy(self):
		"""Now checks the accuracy
		"""
		test_loss, test_acc = self.model.evaluate(self.test_images, self.test_labels, verbose=2)
		
		print(f"Test accuracy: {test_acc}")

if __name__ == "__main__":
	basic_classification()
