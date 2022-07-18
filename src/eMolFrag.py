
import sys
from eMolFrag2.src.representation import Molecule
from pathlib import Path
from rdkit import Chem
from eMolFrag2.src.input import AcquireFiles, AcquireMolecules, Configuration, Options

def main():
    dataset = []
    
	#Verify Tools and Parse Command Line
    #args = sys.argv
    initializer = Options.Options()
    initializer = Configuration.readConfigurationInput(initializer, ARGS)
    
    #Input System
    files = AcquireFiles.acquireMoleculeFiles(initializer)
    dataset = AcquireMolecules.acquireMolecules(files)
    print("Amount of Molecules:", len(dataset))
    #Process
    
    #Post-Process
	
	





if __name__ == '__main__':
  from argparse import ArgumentParser
  parser = ArgumentParser(description='eMolFrag2')
  parser.add_argument("-i",
  type=str,
  help='Set the input path')
  
  parser.add_argument("-o",
  type=str,
  help='Set the output path')
  
  parser.add_argument("-m",
  type=int, choices=range(0,3),
  help='Set the execution type')
  
  parser.add_argument("-c",
  type=int, choices=range(0,3),
  help='Set the output type')
  
  
  
  
  ARGS = parser.parse_args()
  #logging.basicConfig(level=args.loglevel)
  main()





if __name__ == "__main__":
	main()