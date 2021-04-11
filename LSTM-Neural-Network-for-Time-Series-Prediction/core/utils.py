import datetime as dt
import matplotlib.ticker as ticker
import matplotlib.pyplot as plt
import numpy as np
from itertools import combinations, permutations
from sklearn.linear_model import LassoCV, ElasticNetCV


cmcm = ['ACCER', ['ADTM', 'MAADTM'], ["MTR", "ATR"], ["BIAS1", "BIAS2", "BIAS3"], 'CCI', ['DKX', 'MADKX'],
        ['KDJ_K', 'KDJ_D', 'KDJ_J'], 'MFI', 'MTM', 'ROC', ['OSC', 'MAOSC'], ['UDL', 'MAUDL'], ['WR', 'MAWR']]
# 去除DIF
qs = [['CHO', 'MACHO'], ['CYEL', 'CYES'], ['PDI', 'MDI', 'ADX', 'ADXR'], ['DPO', 'MADPO'],
      ['EMV', 'MAEMV'], ['GDX_G', 'GDX_D', 'GDX_X'],
      ['JS', 'MAJS1', 'MAJS2', 'MAJS3'], ['DIF', 'DEA', 'MACD'], ['TRIX', 'MATRIX'], ['UOS', 'MAUOS'],
      ['VPT', 'MAVPT'], ['WVAD', 'MAWVAD']]
nl = [['BR', 'AR'], ['CR', 'MA1', 'MA2', 'MA3', 'MA4'], ['CYR', 'MACYR'], ['MASS', 'MAMASS'], ['PCNT', 'MAPCNT'],
      'PSY', ['VR', 'MAVR']]
cjl = [['AMOW', 'AMO1', 'AMO2'], ['CCL', 'MACCL'], 'OBV', ['VOL', 'MAVOL1', 'MAVOL2'],
       ['VRSI1', 'VRSI2', 'VRSI3'], 'LB']
jx = ['AMV', 'BBI', ['BBI_BOLL', 'BBI_UPR', 'BBI_DOWN'], 'MA', 'HMA', 'LMA', 'VMA']
lj = [['BOLL_UB', 'BOLL_MB', 'BOLL_LB'], ['UPPER', 'LOWER', 'ENE'], ['STOR', 'MIDR', 'WEKR', 'WEKS', 'MIDS', 'STOS'],
      'PBX', ['SUP', 'SDN', 'LUP', 'LDN'], ['PASS1', 'PASS2', 'PASS3', 'PASS4']]
# 去除CYHT,LYJH
qt = ['EMA', 'SMA', ['CDP', 'AH', 'NH', 'NL', 'AL'], ['CJDX_J', 'CJDX_D', 'CJDX_X'],
      ['JYJL1', 'JYJL2'], ['LHXJ1', 'LHXJ2'], ['ZBCD']]
sx = []
lx = [['ZLMM1', 'ZLMM2', 'ZLMM3'], ['SHT1', 'SHT2']]
gx = ['CYW', 'CYS']
ts = [['AROON1', 'AROON2']]
tb = ['ZX', ['PUCU1', 'PUCU2']]
all_indicators = cmcm+qs+nl+cjl+jx+lj+qt+lx+gx+ts+tb


class Timer():

    def __init__(self):
        self.start_dt = None

    def start(self):
        self.start_dt = dt.datetime.now()

    def stop(self):
        end_dt = dt.datetime.now()
        print('Time taken: %s' % (end_dt - self.start_dt))


fig = plt.figure(facecolor='white', figsize=(16, 9))


def plot_results_multiple(predicted_data, true_data, prediction_len, data_index, plt_index, symbol_change_date,
                          raw_data=False, single_plot=True):
    if single_plot:
        fig = plt.figure(facecolor='white', figsize=(16, 9))
        ax = fig.add_subplot(111)
    else:
        global fig
        ax = fig.add_subplot(3, 4, plt_index + 1)
    if raw_data:
        ax.yaxis.set_major_locator(plt.MultipleLocator(50))
    ax.plot(data_index, true_data, label='True Data')
    # ax.vlines(symbol_change_date, 3150, 4500, colors='r')
    if single_plot:
        tick_spacing = 20
    else:
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


def util_ls(ls):
    indicator = []
    for i in ls:
        if isinstance(i, list):
            indicator.extend(util_ls(i))
        else:
            indicator.append(i)
    return indicator


def combinatorial_ls(str_ls, ls, num):
    return list(combinations(str_ls, num)), list(combinations(ls, num))


def check_columns(df, columns):
    #columns = util_ls(j)
    df_data = df.get(columns)
    data = df_data.values
    target = df["Close"].values
    # Find the optimal alpha and l1_ratio for Elastic Net
    encv = ElasticNetCV(alphas=np.logspace(-3, 2, 50), l1_ratio=(0.1, 0.25, 0.5, 0.75, 0.8), normalize=True)
    encv.fit(data, target)
    print('ElasticNet optimal alpha: %.3f and L1 ratio: %.4f' % (encv.alpha_, encv.l1_ratio_))
    if np.sum(encv.coef_ == 0):
        dorp_ls = df_data.columns[encv.coef_ == 0].tolist()
        print(dorp_ls)
        all_drop_ls = []
        for k in dorp_ls:
            if k in all_indicators:
                all_drop_ls.append(k)
            else:
                for w in all_indicators:
                    if isinstance(w, list):
                        if k in w:
                            all_drop_ls.extend(w)
        print(set(all_drop_ls))
        for item in set(all_drop_ls):
            columns.remove(item)
    return columns