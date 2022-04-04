from statistics import *
from matplotlib import pyplot as plt


def data(l):
	quantiles_l = quantiles(l)
	return {"mean": mean(l), "median": quantiles_l[1], "mode": mode(l), "variance": variance(l), "stdev": stdev(l),
			"first_quartile": quantiles_l[0], "third_quartile": quantiles_l[2], "min": min(l), "max": max(l)}


def plot_data(l):
	to_plot = data(l)
	plt.plot(to_plot)
