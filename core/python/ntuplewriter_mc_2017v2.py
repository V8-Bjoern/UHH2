import FWCore.ParameterSet.Config as cms
from UHH2.core.ntuple_generator import generate_process  # use CMSSW type path for CRAB
from UHH2.core.optionsParse import setup_opts, parse_apply_opts


"""NTuple config for 2017v2 MC datasets.

You should try and put any centralised changes in generate_process(), not here.
"""


process = generate_process(year="2017v2", useData=False)

# Please do not commit changes to source filenames - used for consistency testing
process.source.fileNames = cms.untracked.vstring([
    'file:///nfs/dust/cms/user/tiedemab/FastSimulation/FastSim/CMSSW_9_4_12/src/Output_ZPrimeTT_M1000_1/TTZprime_FastSim_1.root'
])

# Do this after setting process.source.fileNames, since we want the ability to override it on the commandline
options = setup_opts()
parse_apply_opts(process, options)

with open('pydump_mc_2017v2.py', 'w') as f:
    f.write(process.dumpPython())
