ffmpeg -y -i %1 -vf eq=contrast=3 -c:a copy %1_contrast.jpg
del %1
