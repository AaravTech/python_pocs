import np
import tensorflow as tf


class Classifier(object):
    def __init__(self, existing_model):
        self.load_model(existing_model)

    def load_model(self, existing_model):
        self.model = None

    def predict(self, location):
        label = 'Unknown'
        '''
        TODO: Write code to predict face using CNN
        '''
        return label