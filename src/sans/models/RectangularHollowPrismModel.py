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
   src/sans/models/include/RectangularHollowPrism.h
   AND RE-RUN THE GENERATOR SCRIPT
"""

from sans.models.BaseComponent import BaseComponent
from sans.models.sans_extension.c_models import CRectangularHollowPrismModel

def create_RectangularHollowPrismModel():
    """
       Create a model instance
    """
    obj = RectangularHollowPrismModel()
    # CRectangularHollowPrismModel.__init__(obj) is called by
    # the RectangularHollowPrismModel constructor
    return obj

class RectangularHollowPrismModel(CRectangularHollowPrismModel, BaseComponent):
    """ 
    Class that evaluates a RectangularHollowPrismModel model. 
    This file was auto-generated from src/sans/models/include/RectangularHollowPrism.h.
    Refer to that file and the structure it contains
    for details of the model.
    
    List of default parameters:

    * scale           = 1.0 
    * short_side      = 35.0 [A]
    * b2a_ratio       = 1.0 [adim]
    * c2a_ratio       = 1.0 [adim]
    * thickness       = 1.0 [A]
    * sldPipe         = 6.3e-06 [1/A^(2)]
    * sldSolv         = 1e-06 [1/A^(2)]
    * background      = 0.0 [1/cm]

    """
        
    def __init__(self, multfactor=1):
        """ Initialization """
        self.__dict__ = {}
        
        # Initialize BaseComponent first, then sphere
        BaseComponent.__init__(self)
        #apply(CRectangularHollowPrismModel.__init__, (self,)) 

        CRectangularHollowPrismModel.__init__(self)
        self.is_multifunc = False
		        
        ## Name of the model
        self.name = "RectangularHollowPrismModel"
        ## Model description
        self.description = """
         Form factor for a hollow rectangular prism with uniform scattering length density.
		scale:Scale factor
		short_side: shortest side of the rectangular prism  [A]
		b2a_ratio: ratio b/a [adim]
		c2a_ratio: ratio c/a [adim]
		thickness: thickness of the walls [A]
		sldPipe: Pipe_sld
		sldSolv: solvent_sld
		background:Incoherent Background [1/cm]
        """
       
        ## Parameter details [units, min, max]
        self.details = {}
        self.details['scale'] = ['', None, None]
        self.details['short_side'] = ['[A]', None, None]
        self.details['b2a_ratio'] = ['[adim]', None, None]
        self.details['c2a_ratio'] = ['[adim]', None, None]
        self.details['thickness'] = ['[A]', None, None]
        self.details['sldPipe'] = ['[1/A^(2)]', None, None]
        self.details['sldSolv'] = ['[1/A^(2)]', None, None]
        self.details['background'] = ['[1/cm]', None, None]

        ## fittable parameters
        self.fixed = ['short_side.width',
                      'b2a_ratio.width',
                      'c2a_ratio.width',
                      'thicness.width']
        
        ## non-fittable parameters
        self.non_fittable = []
        
        ## parameters with orientation
        self.orientation_params = []

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
        return (create_RectangularHollowPrismModel, tuple(), state, None, None)
        
    def clone(self):
        """ Return a identical copy of self """
        return self._clone(RectangularHollowPrismModel())   
       	
    def run(self, x=0.0):
        """ 
        Evaluate the model
        
        :param x: input q, or [q,phi]
        
        :return: scattering function P(q)
        
        """
        return CRectangularHollowPrismModel.run(self, x)
   
    def runXY(self, x=0.0):
        """ 
        Evaluate the model in cartesian coordinates
        
        :param x: input q, or [qx, qy]
        
        :return: scattering function P(q)
        
        """
        return CRectangularHollowPrismModel.runXY(self, x)
        
    def evalDistribution(self, x):
        """ 
        Evaluate the model in cartesian coordinates
        
        :param x: input q[], or [qx[], qy[]]
        
        :return: scattering function P(q[])
        
        """
        return CRectangularHollowPrismModel.evalDistribution(self, x)
        
    def calculate_ER(self):
        """ 
        Calculate the effective radius for P(q)*S(q)
        
        :return: the value of the effective radius
        
        """       
        return CRectangularHollowPrismModel.calculate_ER(self)
        
    def calculate_VR(self):
        """ 
        Calculate the volf ratio for P(q)*S(q)
        
        :return: the value of the volf ratio
        
        """       
        return CRectangularHollowPrismModel.calculate_VR(self)
              
    def set_dispersion(self, parameter, dispersion):
        """
        Set the dispersion object for a model parameter
        
        :param parameter: name of the parameter [string]
        :param dispersion: dispersion object of type DispersionModel
        
        """
        return CRectangularHollowPrismModel.set_dispersion(self,
               parameter, dispersion.cdisp)
        
   
# End of file

