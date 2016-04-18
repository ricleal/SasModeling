import sys
sys.path.append('/Users/rhf/git/SasModeling/build/temp.macosx-10.11-x86_64-2.7/src/sas')

"""

Test plotting sphere

"""
import numpy as np
import matplotlib.pyplot as plt

from sas.models.SphereModel import SphereModel
comp = SphereModel()
comp.setParam("radius", 30.0)
comp.setParam("background", 0.01)

# Generate Q and calculate I
q = np.linspace(0.001, 1, num=200)
i = map(comp.run,q)

# Plot I(q)
plt.figure()
plt.plot(q,np.log(i))


qx = np.linspace(-1, 1, num=400)
qy = qx
xv, yv = np.meshgrid(qx, qy)
xv= xv.flatten()
yv= yv.flatten()
qxy = np.column_stack((xv,yv))

ixy = [ comp.runXY(list(i)) for i in qxy]
ixy = np.array(ixy)


ixy = ixy.reshape(400,400)
ixy = np.log(ixy)

plt.figure()
plt.imshow(ixy)
plt.show()
