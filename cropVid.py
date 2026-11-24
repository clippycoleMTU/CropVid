from hhmmss import getTimes
import subprocess
from pathlib import Path

sourceVid = input("What is the path to the source video?").strip().strip('"')
outputPath = input("Output .mp4 path?").strip().strip('"')

if not Path(sourceVid).is_file():
    raise FileNotFoundError(f"Source video not found: {sourceVid}")

if Path(sourceVid).resolve() == Path(outputPath).resolve():
    raise ValueError("Choose a different output as to not overwrite another file.")

startTime, endTime = getTimes()
duration = endTime - startTime

command = [
    "ffmpeg",
    "-ss", str(startTime),
    "-i", sourceVid,
    "-t", str(duration),
    "-vf", "scale=720:1280:force_original_aspect_ratio=increase,crop=720:1280",
    "-c:v", "libx264",
    "-crf", "22",
    "-preset", "medium",
    "-c:a", "aac",
    "-n",
    outputPath
]

subprocess.run(command, check=True)
print(f"Finished: {outputPath} \n May the force be with you" )
