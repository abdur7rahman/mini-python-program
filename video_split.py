from moviepy.editor import *

clip= VideoFileClip("a.mp4")

edit =clip.subclip(0,5)

edit.write_videofile("edita.mp4")