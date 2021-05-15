import PythonMagick
 
img = PythonMagick.Image('duck.jpg')

img.sample('128x128')
img.write('robin.ico')