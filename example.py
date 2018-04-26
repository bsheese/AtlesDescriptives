from pathlib import Path
datadir = Path("research/")
print(datadir)

files = datadir.glob("**/*.decoded")
processors = [TrackProcessor(f) for f in files]

#stats = [proc.get_stats() for proc in processors]
stats = []
for proc in processors:
        stats.append(proc.get_stats())
