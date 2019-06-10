import pickle
from datetime import datetime
import timeit

import numpy as np
from tensorflow import keras
from tensorflow.python.keras.models import load_model

POKER_CARD_LENGTH = 52


def load_image_data(type_='train'):
    if type_ not in ('train', 'test'):
        raise Exception(f"type error(train, test); {type_}")

    return pickle.load(open(f"./{type_}.pickle", 'rb'))


def load_train_data():
    train_ = load_image_data('train')
    return np.array([r[0] for r in train_]), np.array([r[1] for r in train_])


def load_test_data():
    test_ = load_image_data('test')
    return np.array([r[0] for r in test_]), np.array([r[1] for r in test_])


def model_process_step01():
    x_train, y_train = load_train_data()
    x_test, y_test = load_test_data()

    # one hot encoding
    y_train = keras.utils.to_categorical(y_train, POKER_CARD_LENGTH)
    y_test = keras.utils.to_categorical(y_test, POKER_CARD_LENGTH)
    # print(x_train.shape, x_test.shape)

    x_train = x_train.reshape([x_train.shape[0], x_train.shape[1] * x_train.shape[2]])
    x_test = x_test.reshape([x_test.shape[0], x_test.shape[1] * x_test.shape[2]])

    # print(x_train.shape, x_test.shape)
    x_train = x_train.astype('float32') / 255.
    x_test = x_test.astype('float32') / 255.

    model = keras.Sequential()
    model.add(keras.layers.Dense(128, activation="relu", input_shape=(x_train.shape[1],)))
    model.add(keras.layers.Dense(128, activation="relu"))
    model.add(keras.layers.Dense(POKER_CARD_LENGTH, activation="softmax"))

    model.compile(optimizer='Adam', loss="categorical_crossentropy", metrics=['accuracy'])
    model.summary()
    model.fit(x_train, y_train,
              batch_size=4,
              epochs=10,
              validation_data=(x_test, y_test))
    score = model.evaluate(x_test, y_test, verbose=0)
    print('Test loss:', score[0])
    print('Test accuracy:', score[1])

    model.save('model_poker_card.h5')

    # model = load_model('mnist_mlp_model.h5')


if __name__ == '__main__':
    st = timeit.default_timer()

    model_process_step01()

    process_time = (timeit.default_timer() - st)
    if process_time < 100:
        print(__file__, f"Python Elapsed {process_time:.02f} seconds, current time; {datetime.now().strftime('%H:%M')}")
    elif process_time < 6000:
        print(__file__,
              f"Python Elapsed {process_time / 60:.02f} seconds, current time; {datetime.now().strftime('%H:%M')}")
    else:
        print(__file__,
              f"Python Elapsed {process_time / 3600:.02f} seconds, current time; {datetime.now().strftime('%H:%M')}")
