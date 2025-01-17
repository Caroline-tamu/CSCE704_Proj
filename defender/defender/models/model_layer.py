import tensorflow as tf
from tensorflow.keras import layers
from tensorflow.keras.regularizers import l2

class CustomLayer(layers.Layer):
    def __init__(self, **kwargs):
        super(CustomLayer, self).__init__(**kwargs)
        self.conv1 = layers.Conv2D(filters=128, kernel_size=(5, 5), padding='valid')
        self.act1 = layers.Activation('relu')
        self.pool1 = layers.MaxPooling2D(pool_size=(2, 2))
        self.batch_norm1 = layers.BatchNormalization()

        self.conv2 = layers.Conv2D(filters=64, kernel_size=(3, 3), padding='valid', kernel_regularizer=l2(0.00005))
        self.act2 = layers.Activation('relu')
        self.pool2 = layers.MaxPooling2D(pool_size=(2, 2))
        self.batch_norm2 = layers.BatchNormalization()

        self.conv3 = layers.Conv2D(filters=32, kernel_size=(3, 3), padding='valid', kernel_regularizer=l2(0.00005))
        self.act3 = layers.Activation('relu')
        self.pool3 = layers.MaxPooling2D(pool_size=(2, 2))
        self.batch_norm3 = layers.BatchNormalization()

        self.flatten = layers.Flatten()
        self.dense1 = layers.Dense(units=256, activation='relu')
        self.dropout = layers.Dropout(0.5)
        self.output_layer = layers.Dense(units=1, activation='sigmoid')

    def call(self, inputs):
        x = self.conv1(inputs)
        x = self.act1(x)
        x = self.pool1(x)
        x = self.batch_norm1(x)

        x = self.conv2(x)
        x = self.act2(x)
        x = self.pool2(x)
        x = self.batch_norm2(x)

        x = self.conv3(x)
        x = self.act3(x)
        x = self.pool3(x)
        x = self.batch_norm3(x)

        x = self.flatten(x)
        x = self.dense1(x)
        x = self.dropout(x)
        return self.output_layer(x)