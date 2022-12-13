
#import PySpice as sp

from hspiceParser import import_export
import numpy as np
import pandas as pd

# exception import
#from  


def parseSpiceOut(filePath, fileList, device):
    TRdata = []
    TR_c   = []

    # for single output this is the output port
    outputC = " v_outc0"

    # List of outputs
    spOutList = pd.read_csv(filePath + fileList)

    # Output dataframe
    concentrationDF = pd.DataFrame(columns=['Outlet', 'Chemical', 'OutConcentration', 'ExpectedConcentration', 'Error'])

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
        #specFile = filePath.replace('sliceFiles/', '') + device 

        for o in outletA:
            concentrationDF = concentrationDF.append({'Outlet':o, 'Chemical':chem, 'OutConcentration':outC}, ignore_index=True)

    
    concentrationDF.to_csv(filePath.replace('sliceFiles/', '') + 'chemicalOutput.csv')

    total_C = sum(TR_c)

    TR_c_r  = TR_c/total_C * 100

    print(TR_c) 
    print(TR_c_r)     
    pass
