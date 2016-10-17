import unittest
import importlib
import glob
import io
import sys
import json

import w6_dft_test

suppress_output = True

def check_all_files():
    passed,failed = [],[]

    Trials = glob.glob('w6_dft.py')

    for file_name in Trials:
        loader = unittest.loader.TestLoader()
        results = unittest.result.TestResult()

        try:

            if suppress_output:
                s = io.StringIO()
                sys.stdout = s

        
            tests = loader.loadTestsFromTestCase(w6_dft_test.DFTTestCase)
            tests.run(results)

            tests_passed = results.testsRun - len(results.failures) - len(results.errors)     
  
            if results.wasSuccessful():
                passed.append(file_name) 
            else:
                failed.append(file_name)   
            if suppress_output:
                sys.stdout = sys.__stdout__
    
        except Exception as e:
            if suppress_output:
                sys.stdout = sys.__stdout__

            print('exception',file_name,e)
            failed.append(file_name)

        finally:
            print(file_name[:-3])
    print("Passed=",len(passed))
    print("Failed=",len(failed))

    return passed,failed

if __name__ == "__main__":
    passed,failed = check_all_files()
    Results={'failed':failed,'passed':passed,'authors':w6_dft_test.authors}
    with open('week6_results.json','w') as f:
        json.dump(Results,f,indent=4)