import datetime as dt
import matplotlib.ticker as ticker
import matplotlib.pyplot as plt
import numpy as np


class Timer():

    def __init__(self):
        self.start_dt = None

    def start(self):
        self.start_dt = dt.datetime.now()

    def stop(self):
        end_dt = dt.datetime.now()
        print('Time taken: %s' % (end_dt - self.start_dt))


fig = plt.figure(facecolor='white', figsize=(16, 9))

def plot_results_multiple(predicted_data, true_data, prediction_len, data_index, plt_index, raw_data=False):
    ax = fig.add_subplot(3, 4, plt_index+1)
    ax.yaxis.set_major_locator(plt.MultipleLocator(50))
    ax.plot(data_index, true_data, label='True Data')
    tick_spacing = 5  # 设置密度，比如横坐标9个，设置这个为3,到时候横坐标上就显示 9/3=3个横坐标，
    ax.xaxis.set_major_locator(ticker.MultipleLocator(tick_spacing))
    # Pad the list of predictions to shift it in the graph to it's correct start
    for i, data in enumerate(predicted_data):
        if raw_data:
            data = [(item + 1) * true_data[i] for item in data]
        padding = [None for p in range(i * prediction_len)]
        plt.plot(padding + data, label='Prediction')
        plt.legend(loc='lower left', fontsize=8)

    plt.xticks(rotation=-30)  # 设置横坐标显示的角度，角度是逆时针
    # plt.show()


def plot_results(predicted_data, true_data):
    fig = plt.figure(facecolor='white')
    ax = fig.add_subplot(111)
    ax.plot(true_data, label='True Data')
    plt.plot(predicted_data, label='Prediction')
    plt.legend()
    plt.show()


def check_buy_sell(predictions: list):
    """
    返回一个bool，true上涨做多，false下降做空
    """
    predictions = np.array(predictions)
    ret = np.diff(predictions)
    data = ret / abs(ret)
    ls_data = (data / abs(data)).astype(int).tolist()
    return True if ls_data.count(1) > ls_data.count(-1) else False, ls_data
