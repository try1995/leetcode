import math
import numpy as np
import pandas as pd
from sklearn import preprocessing
from time import time


class DataLoader:

    """A class for loading and transforming data for the lstm model"""
    # 按照日期分割
    def __init__(self, filename, cols, train_end_data, test_start_data, seq_len, test_data_num=250, drop=False):
        dataframe = pd.read_csv(filename, index_col=0).get(cols).dropna(how="any") if drop else pd.read_csv(filename, index_col=0).get(cols)
        # 归一化
        for col in cols:
            if col not in ["Close", "Open", "High", "Low",  "Volume", "Money"]:
                dataframe[col] = dataframe.get([col]).apply(lambda x:(x-x.min())/(x.max()-x.min()))
        # # 训练数据取最开始数据到预测日期的前一个交易日
        self.data_train = dataframe.loc[dataframe.index[0]:train_end_data].get(cols).values
        # 测试数据要拼接一下训练最后的窗口数据
        self.data_test = np.concatenate((self.data_train[-seq_len:], dataframe.loc[test_start_data:dataframe.index[-1]].get(cols).values[0:test_data_num]))
        self.date_index = dataframe.loc[test_start_data:dataframe.index[-1]].index.values
        self.len_train = len(self.data_train)
        self.len_test = len(self.data_test)
        self.len_train_windows = None

    def get_test_data(self, seq_len, normalise, raw_data=False):
        """
        Create x, y test data windows
        Warning: batch method, not generative, make sure you have enough memory to
        load data, otherwise reduce size of the training split.
        """
        data_windows = []
        for i in range(self.len_test - seq_len):
            data_windows.append(self.data_test[i:i + seq_len])

        data_windows = np.array(data_windows).astype(float)

        # 原始数据
        if raw_data:
            y = data_windows[:, -1, [0]].ravel()

        data_windows = self.normalise_windows(data_windows, single_window=False) if normalise else data_windows

        x = data_windows[:, :-1]
        if not raw_data:
            y = data_windows[:, -1, [0]].ravel()
        return x, y, self.date_index[:y.shape[0]]

    def get_train_data(self, seq_len, normalise):
        """
        Create x, y train data windows
        Warning: batch method, not generative, make sure you have enough memory to
        load data, otherwise use generate_training_window() method.
        """
        data_x = []
        data_y = []
        for i in range(self.len_train - seq_len):
            x, y = self._next_window(i, seq_len, normalise)
            data_x.append(x)
            data_y.append(y)

        return np.array(data_x), np.array(data_y)

    def generate_train_batch(self, seq_len, batch_size, normalise):
        """Yield a generator of training data from filename on given list of cols split for train/test"""
        i = 0
        while i < (self.len_train - seq_len):
            x_batch = []
            y_batch = []
            for b in range(batch_size):
                if i >= (self.len_train - seq_len):
                    # stop-condition for a smaller final batch if data doesn't divide evenly
                    yield np.array(x_batch), np.array(y_batch)
                    i = 0
                x, y = self._next_window(i, seq_len, normalise)
                x_batch.append(x)
                y_batch.append(y)
                i += 1
            yield np.array(x_batch), np.array(y_batch)

    def _next_window(self, i, seq_len, normalise):
        """Generates the next data window from the given index location i"""
        window = self.data_train[i:i + seq_len]
        window = self.normalise_windows(window, single_window=True)[0] if normalise else window
        x = window[:-1]
        y = window[-1, [0]]
        return x, y

    def normalise_windows(self, window_data, single_window=False):
        """Normalise window with a base value of zero"""
        bis=2
        normalised_data = []
        window_data = [window_data] if single_window else window_data
        for window in window_data:
            normalised_window = window.copy()
            normalised_window[:, 0:bis] = window[:, 0:bis] / window[:, 0:bis][0] - 1
            # normalised_window = window / window[0] - 1
            # normalised_window = np.diff(np.log(window), axis=0)
            normalised_data.append(normalised_window)
        return np.array(normalised_data)
