def predict(pages, frame, index):
    farthest, res = index, -1
    for f in frame:
        if f not in pages[index:]:
            return frame.index(f)
        next_use = pages[index:].index(f) + index
        if next_use > farthest:
            farthest, res = next_use, frame.index(f)
    return res if res != -1 else 0

def optimal(pages, frames):
    frame = []
    faults = 0
    for i, p in enumerate(pages):
        if p not in frame:
            if len(frame) < frames:
                frame.append(p)
            else:
                pos = predict(pages, frame, i + 1)
                frame[pos] = p
            faults += 1
    return faults

pages = list(map(int, input("Enter page reference string: ").split()))
frames = int(input("Enter number of frames: "))
print("Page Faults =", optimal(pages, frames))
