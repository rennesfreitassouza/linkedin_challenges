# Example file for Python Essential Libraries course by Joe Marini
# demonstrates simple image operations using the Pillow library

from PIL import Image
import glob
import os

# define a thumbnail size
thumbsize = (128, 128)

images = glob.glob("ImagesArc/*.*")
for image in images:
    if image.endswith(".gif"): #or image.endswith(".png") or image.endswith(".gif"):
        fn = os.path.basename(image)
        # filename, ext = os.path.splitext(fn)
        filename, ext = fn.split(".")[0], fn.split(".")[1]
        with Image.open(image) as imgfile:
            imgfile.thumbnail(thumbsize)
            ext = "png"
            path_a_file = '.'.join([filename, "thumb", ext])
            imgfile.save("ImagesArc/" + path_a_file, ext)
