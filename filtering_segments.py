import random

def segment_generator(num):
    segments_list = []
    for i in range(num):
        segment = [round(random.uniform(0, 10),3) for _ in range(4)]
        segments_list.append(segment)
    return segments_list

segments = segment_generator(10)
print(segments)