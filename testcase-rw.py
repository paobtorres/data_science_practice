import espressomd
from espressomd import interactions
from espressomd.io.writer import vtf
from espressomd import electrostatics 

import os
import sys
import inspect

import numpy as np


# Find path to pyMBE
current_dir= os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
path_end_index=current_dir.find("pyMBE")
pyMBE_path=current_dir[0:path_end_index]+"pyMBE"
sys.path.insert(0, pyMBE_path) 

# Create an instance of pyMBE library
import pyMBE
pmb = pyMBE.pymbe_library()



# Load some functions from the handy_scripts library for convinience
from handy_scripts.handy_functions import setup_electrostatic_interactions
from handy_scripts.handy_functions import minimize_espresso_system_energy
from handy_scripts.handy_functions import setup_langevin_dynamics
from handy_scripts.handy_functions import block_analyze

# # The trajectories of the simulations will be stored using espresso built-up functions in separed files in the folder 'frames'
if not os.path.exists('./frames'):
    os.makedirs('./frames')


# Simulation parameters
pmb.set_reduced_units(unit_length=0.4*pmb.units.nm)
pH_range = np.linspace(2, 12, num=20)
Samples_per_pH = 1000
MD_steps_per_sample = 1000
steps_eq = int(Samples_per_pH/3)
N_samples_print = 10  # Write the trajectory every 100 samples
probability_reaction =0.5 
SEED = 100
dt = 0.001
solvent_permitivity = 78.3



# path_to_interactions=pmb.get_resource("reference_parameters/interaction_parameters/Lunkad2021.txt")
# path_to_pka=pmb.get_resource("reference_parameters/pka_sets/Hass2015.txt")
# pmb.load_interaction_parameters (filename=path_to_interactions) 
# pmb.load_pka_set (path_to_pka)


pmb.define_residue(
    name = "Res_1",
    central_bead = "I",
    side_chains = ["A","B"])

pmb.define_residue(
    name = "Res_2",
    central_bead = "I",
    side_chains = ["Res_1"])   


pmb.define_molecule(
    name = "A_molecule",
    residue_list = ["Res_1", "Res_1",
                    "Res_2", "Res_1",
                    "Res_1", "Res_2",
                    "Res_2"])

