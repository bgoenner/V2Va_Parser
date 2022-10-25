
#import PySpice as sp

from hspiceParser import import_export
import numpy as np
import pandas as pd


def parseSpiceOut(filePath, fileList):
    TRdata = []
    TR_c   = []

    # for single output this is the output port
    outputC = " v_outc0"

    spOutList = open(filePath + fileList)

    concentrationDF = pd.DataFrame()

    for line in spOutList:
        line = line.replace("\n", "")
        inputFileBase = line.replace(".sp", "_o.tr0")
        csvFile= line.replace(".sp", "_o_tr0.csv")

        import_export(inputFileBase, "csv")

        df = pd.read_csv(csvFile, delimiter = ",")

        TRdata.append(df)

        #print(df.columns)

        TR_c.append(df.loc[0, outputC])

        concentrationDF = concentrationDF({'Outlet':hold, 'Chemical':hold, 'OutConcentration':outputC})

    

    total_C = sum(TR_c)

    TR_c_r  = TR_c/total_C * 100

    print(TR_c) 
    print(TR_c_r)     
    pass
