
#import PySpice as sp

from hspiceParser import import_export
import numpy as np
import pandas as pd

# exception import
#from  

def parseSuffix(value):
    if value[-1] == 'm':
        return float(value[:-1]) * 1e-3


def parseSpiceOut(filePath, fileList, device):
    TRdata = []
    TR_c   = []

    # for single output this is the output port
    outputC = " v_outc0"

    # List of outputs
    spOutList = pd.read_csv(filePath + fileList)

    # Output dataframe
    concentrationDF = pd.DataFrame(columns=['Outlet', 'Chemical', 'OutConcentration', 'ExpectedConcentration', 'Error'])

    print('Device: ' + device)

    for line in spOutList.iterrows():
        outFile       = line[1]['OutputFile']#.replace("\n", "")
        inputFileBase = outFile.replace(".sp", "_o.tr0")
        csvFile       = outFile.replace(".sp", "_o_tr0.csv")

        chem   = line[1]['Chemical']
        
        #import_export(inputFileBase, "csv")
        
        try:
            import_export(inputFileBase, "csv")
        except:
            print()


        df = pd.read_csv(csvFile, delimiter = ",")

        TRdata.append(df)

        #print(df.columns)

        # Get concetration of output
        outC = df.loc[0, outputC]
        TR_c.append(outC)

        outlets = line[1]['Outlets']
        outletA = outlets.split(';')[:-1]

        # Read spec file
        specFile = filePath.replace('spiceFiles/', '') + device + '_spec.csv'
        specDF = pd.read_csv(specFile)

        # get value for output and chem
        #expecedOut = specDF[specDF['out'] == value and specDF['Solution'] == ]


        for o in outletA:
            v_outName = o.replace('c0', '')
            expectedOut = specDF[specDF['Outlet'] == v_outName]
            expectedOut = expectedOut[expectedOut['Solution'] == chem]

            if len(expectedOut.index) == 1:
                expectedOutC = str(expectedOut.iloc[0]['OutConcentration'])
                expectedOutC = parseSuffix(expectedOutC)
            elif len(expectedOut.index) == 0:
                print("No spec for, chem:" + chem + " out:" + v_outName)
            elif len(expectedOut.index) > 1:
                print("Multiple values for chem:" + chem + " out:" + v_outName)
                print(expectedOut)
                #print("Taking highest value:")
                
            # Calculate Error
            chemError = abs((expectedOutC - outC)/expectedOutC) * 100

            # output concentration
            concentrationDF = concentrationDF.append({
                'Outlet':o, 
                'Chemical':chem, 
                'OutConcentration':outC,
                'ExpectedConcentration':expectedOutC,
                'Error':chemError}, 
                ignore_index=True)

            print('Error:' + "{:.2f}".format(chemError) + '\tchem:' + chem + '\tout:' + v_outName)

    
    concentrationDF.to_csv(filePath.replace('spiceFiles/', '') + device + '_chemicalOutput.csv')

    total_C = sum(TR_c)

    TR_c_r  = TR_c/total_C * 100

    #print(TR_c) 
    #print(TR_c_r)     
    pass
