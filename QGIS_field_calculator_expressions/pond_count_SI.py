from qgis.core import *
from qgis.gui import *
from numpy import np

def get_a_b(coord1,coord2):
    dy = coord2['y']-coord1['y']
    dx = coord2['x']-coord1['x']
    
    b = dy/dx
    bx = b*coord1['x']
    a = coord1['y']-bx
    
    return (a,b)


def get_SI(coord1,coord2,pCount_divPi):
    a,b = get_a_b(coord1,coord2)
    SI = a+b*np.log(pCount_divPi)
    
    return SI


@qgsfunction(args='auto', group='Custom', referenced_columns=['pond_count'])
def pond_count_SI(feature, parent):
    """
    Calculates the pond count GCN HSI score using logarithmic regression equation: y = a+b*ln(x)
    <h2>Example usage:</h2>
    <ul>
      <li>pond_count_SI()</li>
    </ul>
    """
    pond_count = feature.attribute('pond_count')
    pCount_divPi = pond_count/3.14
    if (pCount_divPi < 4):
        coord1 = {'x':0,'y':0}
        coord2 = {'x':0,'y':0}
        return get_SI(coord1,coord2,pCount_divPi)
    

    return 1