import random
import matplotlib.pyplot as plt

def segment_generator(num):
    segments_list = []
    for i in range(num):
        segment = [round(random.uniform(0, 10),3) for _ in range(4)]
        segments_list.append(segment)
    return segments_list

segments = segment_generator(100)
print(segments)

def plot_segments(segments):
    #using matplotlib to plot the segments (the format is [x1,y1,x2,y2]) in the plane which has the title "All Lines, plot from 0 to 10 in two axis, the color and thickness is random from reasonable values"
    for i, segment in enumerate(segments):
        x1, y1, x2, y2 = segment
        color = (random.uniform(0,1),random.uniform(0,1),random.uniform(0,1),)
        thickness = random.uniform(0.5, 5)
        plt.plot([x1, x2], [y1, y2], color=color, lw=thickness)
    
plot_segments(segments)
plt.grid()
plt.show()