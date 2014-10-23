##############################################################################
# This software was developed by the University of Tennessee as part of the
# Distributed Data Analysis of Neutron Scattering Experiments (DANSE)
# project funded by the US National Science Foundation.
#
# If you use DANSE applications to do scientific research that leads to
# publication, we ask that you acknowledge the use of the software with the
# following sentence:
#
# This work benefited from DANSE software developed under NSF award DMR-0520547
#
# Copyright 2008-2011, University of Tennessee
##############################################################################

""" 
Provide functionality for a C extension model

.. WARNING::

   THIS FILE WAS GENERATED BY WRAPPERGENERATOR.PY
   DO NOT MODIFY THIS FILE, MODIFY
   src/sans/models/include/sc.h
   AND RE-RUN THE GENERATOR SCRIPT
"""

from sans.models.BaseComponent import BaseComponent
from sans.models.sans_extension.c_models import CSCCrystalModel

def create_SCCrystalModel():
    """
       Create a model instance
    """
    obj = SCCrystalModel()
    # CSCCrystalModel.__init__(obj) is called by
    # the SCCrystalModel constructor
    return obj

class SCCrystalModel(CSCCrystalModel, BaseComponent):
    """ 
    Class that evaluates a SCCrystalModel model. 
    This file was auto-generated from src/sans/models/include/sc.h.
    Refer to that file and the structure it contains
    for details of the model.
    
    List of default parameters:

    * scale           = 1.0 
    * dnn             = 220.0 [A]
    * d_factor        = 0.06 
    * radius          = 40.0 [A]
    * sldSph          = 3e-06 [1/A^(2)]
    * sldSolv         = 6.3e-06 [1/A^(2)]
    * background      = 0.0 [1/cm]
    * theta           = 0.0 [deg]
    * phi             = 0.0 [deg]
    * psi             = 0.0 [deg]

    """
        
    def __init__(self, multfactor=1):
        """ Initialization """
        self.__dict__ = {}
        
        # Initialize BaseComponent first, then sphere
        BaseComponent.__init__(self)
        #apply(CSCCrystalModel.__init__, (self,)) 

        CSCCrystalModel.__init__(self)
        self.is_multifunc = False
		        
        ## Name of the model
        self.name = "SCCrystalModel"
        ## Model description
        self.description = """
        P(q)=(scale/Vp)*V_lattice*P(q)*Z(q)+bkg where scale is the volume
		fraction of sphere,
		Vp = volume of the primary particle,
		V_lattice = volume correction for
		for the crystal structure,
		P(q)= form factor of the sphere (normalized),
		Z(q)= paracrystalline structure factor
		for a simple cubic structure.
		[Simple Cubic ParaCrystal Model]
		Parameters;
		scale: volume fraction of spheres
		bkg:background, R: radius of sphere
		dnn: Nearest neighbor distance
		d_factor: Paracrystal distortion factor
		radius: radius of the spheres
		sldSph: SLD of the sphere
		sldSolv: SLD of the solvent
		
        """
       
        ## Parameter details [units, min, max]
        self.details = {}
        self.details['scale'] = ['', None, None]
        self.details['dnn'] = ['[A]', None, None]
        self.details['d_factor'] = ['', None, None]
        self.details['radius'] = ['[A]', None, None]
        self.details['sldSph'] = ['[1/A^(2)]', None, None]
        self.details['sldSolv'] = ['[1/A^(2)]', None, None]
        self.details['background'] = ['[1/cm]', None, None]
        self.details['theta'] = ['[deg]', None, None]
        self.details['phi'] = ['[deg]', None, None]
        self.details['psi'] = ['[deg]', None, None]

        ## fittable parameters
        self.fixed = ['radius.width',
                      'phi.width',
                      'psi.width',
                      'theta.width']
        
        ## non-fittable parameters
        self.non_fittable = []
        
        ## parameters with orientation
        self.orientation_params = ['phi',
                                   'psi',
                                   'theta',
                                   'phi.width',
                                   'psi.width',
                                   'theta.width']

        ## parameters with magnetism
        self.magnetic_params = []

        self.category = None
        self.multiplicity_info = None
        
    def __setstate__(self, state):
        """
        restore the state of a model from pickle
        """
        self.__dict__, self.params, self.dispersion = state
        
    def __reduce_ex__(self, proto):
        """
        Overwrite the __reduce_ex__ of PyTypeObject *type call in the init of 
        c model.
        """
        state = (self.__dict__, self.params, self.dispersion)
        return (create_SCCrystalModel, tuple(), state, None, None)
        
    def clone(self):
        """ Return a identical copy of self """
        return self._clone(SCCrystalModel())   
       	
    def run(self, x=0.0):
        """ 
        Evaluate the model
        
        :param x: input q, or [q,phi]
        
        :return: scattering function P(q)
        
        """
        return CSCCrystalModel.run(self, x)
   
    def runXY(self, x=0.0):
        """ 
        Evaluate the model in cartesian coordinates
        
        :param x: input q, or [qx, qy]
        
        :return: scattering function P(q)
        
        """
        return CSCCrystalModel.runXY(self, x)
        
    def evalDistribution(self, x):
        """ 
        Evaluate the model in cartesian coordinates
        
        :param x: input q[], or [qx[], qy[]]
        
        :return: scattering function P(q[])
        
        """
        return CSCCrystalModel.evalDistribution(self, x)
        
    def calculate_ER(self):
        """ 
        Calculate the effective radius for P(q)*S(q)
        
        :return: the value of the effective radius
        
        """       
        return CSCCrystalModel.calculate_ER(self)
        
    def calculate_VR(self):
        """ 
        Calculate the volf ratio for P(q)*S(q)
        
        :return: the value of the volf ratio
        
        """       
        return CSCCrystalModel.calculate_VR(self)
              
    def set_dispersion(self, parameter, dispersion):
        """
        Set the dispersion object for a model parameter
        
        :param parameter: name of the parameter [string]
        :param dispersion: dispersion object of type DispersionModel
        
        """
        return CSCCrystalModel.set_dispersion(self,
               parameter, dispersion.cdisp)
        
   
# End of file

