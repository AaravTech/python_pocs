import tensorflow as tf
import pandas as pd

# import argparse


TRAIN_URL = "http://download.tensorflow.org/data/iris_training.csv"
TEST_URL = "http://download.tensorflow.org/data/iris_test.csv"

CSV_COLUMN_NAMES = ['SepalLength', 'SepalWidth',
                    'PetalLength', 'PetalWidth', 'Species']


# parser = argparse.ArgumentParser()
# parser.add_argument('--batch_size', default=100, type=int, help='batch size')
# parser.add_argument('--train_steps', default=1000, type=int,
#                     help='number of training steps')

def load_data(label_name='Species'):
    """Parses the csv file in TRAIN_URL and TEST_URL."""

    # Create a local copy of the training set.
    train_path = tf.keras.utils.get_file(fname=TRAIN_URL.split('/')[-1],
                                         origin=TRAIN_URL)
    # train_path now holds the pathname: ~/.keras/datasets/iris_training.csv

    # Parse the local CSV file.
    train = pd.read_csv(filepath_or_buffer=train_path,
                        names=CSV_COLUMN_NAMES,  # list of column names
                        header=0  # ignore the first row of the CSV file.
                       )
    # train now holds a pandas DataFrame, which is data structure
    # analogous to a table.

    # 1. Assign the DataFrame's labels (the right-most column) to train_label.
    # 2. Delete (pop) the labels from the DataFrame.
    # 3. Assign the remainder of the DataFrame to train_features
    train_features, train_label = train, train.pop(label_name)

    # Apply the preceding logic to the test set.
    test_path = tf.keras.utils.get_file(TEST_URL.split('/')[-1], TEST_URL)
    test = pd.read_csv(test_path, names=CSV_COLUMN_NAMES, header=0)
    test_features, test_label = test, test.pop(label_name)

    # Return four DataFrames.
    return (train_features, train_label), (test_features, test_label)


def train_input_fn(features, labels, batch_size):
    dataset = tf.data.Dataset.from_tensor_slices((dict(features), labels))
    dataset = dataset.shuffle(buffer_size=1000).repeat(count=None).batch(batch_size)
    return dataset.make_one_shot_iterator().get_next()


def eval_input_fn(features, labels=None, batch_size=None):
    """An input function for evaluation or prediction"""
    if labels is None:
        # No labels, use only features.
        inputs = dict(features)
    else:
        inputs = (dict(features), labels)

    # Convert inputs to a tf.dataset object.
    dataset = tf.data.Dataset.from_tensor_slices(inputs)

    # Batch the examples
    assert batch_size is not None, "batch_size must not be None"
    dataset = dataset.batch(batch_size)

    # Return the read end of the pipeline.
    return dataset.make_one_shot_iterator().get_next()


def main(argv):
    # args = parser.parse_args(argv[1:])
    default = {}
    default['batch_size'] = 100
    default['train_steps'] = 1000

    (train_feature, train_label), (test_feature, test_label) = load_data()

    # Create feature columns for all features.
    my_feature_columns = []
    for key in train_feature.keys():
        my_feature_columns.append(tf.feature_column.numeric_column(key=key))

    classifier = tf.estimator.DNNClassifier(
        feature_columns=my_feature_columns,
        hidden_units=[10, 10],
        n_classes=3)

    classifier.train(
        input_fn=lambda:train_input_fn(train_feature, train_label, default['batch_size']),
        steps=default['train_steps'])

    # Evaluate the model.
    eval_result = classifier.evaluate(
        input_fn=lambda:eval_input_fn(test_feature, test_label, default['batch_size']))

    print('\nTest set accuracy: {accuracy:0.3f}\n'.format(**eval_result))

    expected = ['Setosa', 'Versicolor', 'Virginica']
    predict_x = {
        'SepalLength': [5.1, 5.9, 6.9],
        'SepalWidth': [3.3, 3.0, 3.1],
        'PetalLength': [1.7, 4.2, 5.4],
        'PetalWidth': [0.5, 1.5, 2.1],
    }

    predictions = classifier.predict(
        input_fn=lambda:eval_input_fn(predict_x, batch_size=default['batch_size']))

    for pred_dict, expec in zip(predictions, expected):
        template = ('\nPrediction is "{}" ({:.1f}%), expected "{}"')

        class_id = pred_dict['class_ids'][0]
        probability = pred_dict['probabilities'][class_id]
        print(template.format(class_id, 100 * probability, expec))

def run():
    tf.logging.set_verbosity(tf.logging.INFO)
    tf.app.run(main)