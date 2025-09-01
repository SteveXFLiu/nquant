import matplotlib.pyplot as plt
from matplotlib.patches import  Rectangle

seq = list(range(10))

params = {          # subplot_arrangement: (slicing_start, slicing_end)
    411: (3, 7),
    412: (None, 5),
    413: (6, None),
    414: (-6, -2)
}

fig = plt.figure()

for position, slicing in params.items():
    plt.subplot(position)
    
    ax = plt.gca()
    ax.set_xlim([-1, len(seq)])
    ax.set_ylim([0, 1])
    
    plt.text(-1, 0.5, f'seq[{'' if slicing[0]== None else slicing[0]}:{'' if slicing[1]==None else slicing[1]}]', fontfamily="monospace", fontsize=10, verticalalignment="center", horizontalalignment="right")
    
    for i in seq:
        if i in seq[slicing[0]:slicing[1]]:
            rect = Rectangle((i, 0), width=1, height=1, facecolor="orange", edgecolor="black")
        else:
            rect = Rectangle((i, 0), width=1, height=1, facecolor="white", edgecolor="black")    
        ax.add_patch(rect)
    
        plt.text(i + 0.5, 0.5, i, fontfamily="times", fontsize=12, verticalalignment="center", horizontalalignment="center")
        
        plt.text(i + 0.1, 0.1, -(10-i), color="green", fontfamily="times", fontstyle="italic", fontsize=8, verticalalignment="bottom", horizontalalignment="left")
    
        plt.text(i + 0.1, 0.9, i, color="blue", fontfamily="times", fontstyle="italic", fontsize=8, verticalalignment="top", horizontalalignment="left")
        
    plt.axis('equal')
    plt.axis('off')

plt.show()