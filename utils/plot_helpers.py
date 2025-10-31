import matplotlib.pyplot as plt

def save_basic_hist(series, path):
    fig, ax = plt.subplots()
    ax.hist(series.dropna())
    ax.set_title("Histogram")
    fig.savefig(path, bbox_inches='tight')
    plt.close(fig)
