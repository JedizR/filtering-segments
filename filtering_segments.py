import random
import matplotlib.pyplot as plt
import time
import numpy as np

def segment_generator(num):
    segments_list = []
    for i in range(num):
        segment = [round(random.uniform(0, 10),3) for _ in range(4)]
        segments_list.append(segment)
    return segments_list

segments = segment_generator(1000)

def plot_segments(segments_list, title):
    plt.title(title)
    plt.axis([0, 10, 0, 10])
    for i, segment in enumerate(segments_list):
        x1, y1, x2, y2 = segment
        color = (random.uniform(0,1),random.uniform(0,1),random.uniform(0,1),)
        thickness = random.uniform(0.5, 5)
        plt.plot([x1, x2], [y1, y2], color=color, lw=thickness)
    
def find_segments_inside_rectangle(segments, rectangle):
    inside_segments = []
    start_x, start_y, end_x, end_y = rectangle
    for segment in segments:
        x1, y1, x2, y2 = segment
        if x1 >= start_x and x1 <= end_x and y1 >= start_y and y1 <= end_y and x2 >= start_x and x2 <= end_x and y2 >= start_y and y2 <= end_y:
            inside_segments.append(segment)
    return inside_segments

def find_segments_inside_rectangle_using_numpy(segments, rectangle):
    "use numpy to filter segments inside rectangles just like the above function"
    start_x, start_y, end_x, end_y = rectangle
    segments_np = np.array(segments)
    inside_segments_np = segments_np[(segments_np[:,0] >= start_x) & (segments_np[:,0] <= end_x) & (segments_np[:,1] >= start_y) & (segments_np[:,1] <= end_y) & (segments_np[:,2] >= start_x) & (segments_np[:,2] <= end_x) & (segments_np[:,3] >= start_y)
                                     & (segments_np[:,3] <= end_y)]
    return inside_segments_np.tolist()

rect = [4,4,6,10]

# NO NUMPY
start_time = time.time()
interested_segments = find_segments_inside_rectangle(segments, rect)
end_time = time.time()
print(f"Normal Time taken: {end_time - start_time} seconds")

# WITH NUMPY
start_time = time.time()
interested_segments_np = find_segments_inside_rectangle_using_numpy(segments, rect)
end_time = time.time()
print(f"Numpy Time taken: {end_time - start_time} seconds")

# Normal Time taken: 4.315376281738281e-05 seconds
# Numpy Time taken: 0.00020003318786621094 seconds

plt.subplot(1,2,1)
plt.grid()
plot_segments(segments, "All Lines")
plt.subplot(1,2,2)
plt.grid()
plot_segments(interested_segments, "Filtered Lines")
plt.show()