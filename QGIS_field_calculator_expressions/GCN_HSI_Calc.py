import GCNHSIPack as HSI
import pyToolBox as pyTB
import pandas as pd
from qgis.core import *
from qgis.gui import *

@qgsfunction(args='auto', group='Custom', referenced_columns=['pond_macrophytes'])

def pond_macrophytes_SI(
    SIRequiredList=['1_zone','2_pArea','3_pDrying','4_waterQ','5_shade','6_waterFowl','7_fish','8_pCount','9_terrestrialH','10_macrophytes'],
    numOfPonds = [1],
    outputFilePath = [''],
    feature, parent
    ):

    """
    Calculates GCN HSI scores and saves csv to user-specified file
    <h2>Example usage:</h2>
    <ul>
      <li>pond_macrophytes_SI()</li>
    </ul>
    """
    
    d = {'pond': [1:length(numOfPonds)], 'col2': [1:length(SIRequiredList)]}
    df = pd.DataFrame(data=d)

        SIRequiredList=['1_location','2_pArea','3_pDrying','4_waterQ','5_shade','6_waterFowl','7_fish','8_pCount','9_terrestrialH','10_macrophytes'],


    for (a in 1:length(SIRequired)):
        if (SIRequired[a] == '1_location'):

        if (SIRequired[a] == '2_pArea'):

        if (SIRequired[a] == '3_pDrying'):

        if (SIRequired[a] == '4_waterQ'):

        if (SIRequired[a] == '5_shade'):

        if (SIRequired[a] == '6_waterFowl'):

        if (SIRequired[a] == '7_fish'):

        if (SIRequired[a] == '8_pCount'):

        if (SIRequired[a] == '9_terrestrialH'):

        if (SIRequired[a] == '10_macrophytes'):