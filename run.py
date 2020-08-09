import lithophane as li

imagefile = './pengha_edit_sq.jpg'
width = 102 #Width in mm
x,y,z = li.jpg2stl(imagefile, width=width, h = 3, d = 0.5)
li.showstl(x,y,z)
model = li.makemesh(x,y,z);
filename=imagefile[:-4] + '_Flat.stl'
model.save(filename)
