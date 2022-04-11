from statistics import mean, mode, variance, stdev, quantiles
from matplotlib import pyplot as plt


def data(data_list):
    quantiles_l = quantiles(data_list)
    return {
        "mean": mean(data_list),
        "median": quantiles_l[1],
        "mode": mode(data_list),
        "variance": variance(data_list),
        "stdev": stdev(data_list),
        "first_quartile": quantiles_l[0],
        "third_quartile": quantiles_l[2],
        "min": min(data_list),
        "max": max(data_list),
    }


def plot_data(data_list):
    to_plot = data(data_list)
    plt.plot(to_plot)
