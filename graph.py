import matplotlib.pyplot as plt
import numpy as np


def show_graph(answers):
    plt.rcdefaults()
    fig, ax = plt.subplots()
    # Example data
    options = answers.keys()
    answers = answers.values()
    y_pos = np.arange(len(options))

    ax.barh(y_pos, answers, align='center')
    ax.set_yticks(y_pos)
    ax.set_yticklabels(options)
    ax.invert_yaxis()  # labels read top-to-bottom
    ax.set_xlabel('Совпадения')
    ax.set_title('График ответов')


    plt.show()