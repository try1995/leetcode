__author__ = "Jakob Aungiers"
__copyright__ = "Jakob Aungiers 2018"
__version__ = "2.0.0"
__license__ = "MIT"

import os
import json
import time
import math
from core.data_processor import DataLoader
from core.model import Model
from core.utils import *

# 兼容tensorflow1.0
import tensorflow.compat.v1 as tf
tf.disable_v2_behavior()


def main():
    configs = json.load(open('config.json', 'r'))
    if not os.path.exists(configs['model']['save_dir']): os.makedirs(configs['model']['save_dir'])

    data = DataLoader(
        os.path.join('data', configs['data']['filename']),
        configs['data']['columns'],
        train_end_data,
        test_start_data,
        configs['data']['sequence_length'],
        configs["data"]["test_data_num"],
        configs['data']['drop']
    )

    model = Model()
    model.build_model(configs)

    x_test, y_test, data_index = data.get_test_data(
        seq_len=configs['data']['sequence_length'],
        normalise=configs['data']['normalise'],
        raw_data = raw_data
    )

    if predict:
        steps_per_epoch = math.ceil(
            (data.len_train - configs['data']['sequence_length']) / configs['training']['batch_size'])
        model.train_generator(
            data_gen=data.generate_train_batch(
                seq_len=configs['data']['sequence_length'],
                batch_size=configs['training']['batch_size'],
                normalise=configs['data']['normalise']
            ),
            epochs=configs['training']['epochs'],
            batch_size=configs['training']['batch_size'],
            steps_per_epoch=steps_per_epoch,
            save_dir=configs['model']['save_dir'],
            datetime_now=test_start_data
        )
    else:
        model.load_model(os.path.join(configs['model']['save_dir'], "%s-e2.h5"%test_start_data))

    predictions = model.predict_sequences_multiple(x_test, configs['data']['sequence_length'],
                                                   configs['data']['sequence_length'])
    # predictions = model.predict_sequence_full(x_test, configs['data']['sequence_length'])
    # predictions = model.predict_point_by_point(x_test)

    plot_results_multiple(predictions, y_test, configs['data']['sequence_length'], data_index, raw_data)
    # plot_results(predictions, y_test)


if __name__ == '__main__':
    predict = True
    raw_data = True
    # train_end_data, test_start_data = '2016-12-30', '2017-01-03'
    ls = [['2016-12-30', '2017-01-03'], ['2017-01-26', '2017-02-03'], ['2017-02-28', '2017-03-01'],
          ['2017-03-31', '2017-04-05'], ['2017-04-28', '2017-05-02'], ['2017-05-31', '2017-06-01'],
          ['2017-06-30', '2017-07-03'], ['2017-07-31', '2017-08-01'], ['2017-08-31', '2017-09-01'],
          ['2017-09-29', '2017-10-09'], ['2017-10-31', '2017-11-01'], ['2017-11-30', '2017-12-01'],
          ['2017-12-29', '2018-01-02'], ['2018-01-31', '2018-02-01'], ['2018-02-28', '2018-03-01'],
          ['2018-03-30', '2018-04-02'], ['2018-04-27', '2018-05-02'], ['2018-05-31', '2018-06-01'],
          ['2018-06-29', '2018-07-02'], ['2018-07-31', '2018-08-01'], ['2018-08-31', '2018-09-03'],
          ['2018-09-28', '2018-10-08'], ['2018-10-31', '2018-11-01'], ['2018-11-30', '2018-12-03'],
          ['2018-12-28', '2019-01-02'], ['2019-01-31', '2019-02-01'], ['2019-02-28', '2019-03-01'],
          ['2019-03-29', '2019-04-01'], ['2019-04-30', '2019-05-06'], ['2019-05-31', '2019-06-03'],
          ['2019-06-28', '2019-07-01'], ['2019-07-31', '2019-08-01'], ['2019-08-30', '2019-09-02'],
          ['2019-09-30', '2019-10-08'], ['2019-10-31', '2019-11-01'], ['2019-11-29', '2019-12-02'],
          ['2019-12-31', '2020-01-02'], ['2020-01-23', '2020-02-03'], ['2020-02-28', '2020-03-02'],
          ['2020-03-31', '2020-04-01'], ['2020-04-30', '2020-05-06'], ['2020-05-29', '2020-06-01'],
          ['2020-06-30', '2020-07-01'], ['2020-07-31', '2020-08-03'], ['2020-08-31', '2020-09-01'],
          ['2020-09-30', '2020-10-09'], ['2020-10-30', '2020-11-02'], ['2020-11-30', '2020-12-01']]
    for i in ls:
        train_end_data, test_start_data = i
        # train_end_data, test_start_data = '2017-12-29', '2018-01-02'
        # train_end_data, test_start_data = '2018-12-28', '2019-01-02'
        # train_end_data, test_start_data = '2019-12-31', '2020-01-02'
        main()
