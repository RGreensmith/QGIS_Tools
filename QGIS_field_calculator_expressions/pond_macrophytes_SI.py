from qgis.core import *
from qgis.gui import *

def get_m_c(coord1,coord2):
    dy = coord2['y']-coord1['y']
    dx = coord2['x']-coord1['x']
    
    m = dy/dx
    mx = m*coord1['x']
    c = coord1['y']-mx
    
    return (m,c)


def get_SI(coord1,coord2,pond_macrophytes):
    m,c = get_m_c(coord1,coord2)
    SI = m*pond_macrophytes+c
    
    return SI


@qgsfunction(args='auto', group='Custom', referenced_columns=['pond_macrophytes'])
def pond_macrophytes_SI(feature, parent):
    """
    Calculates the pond macrophytes GCN HSI score using straight line equation: y = mx + c
    <h2>Example usage:</h2>
    <ul>
      <li>pond_macrophytes_SI()</li>
    </ul>
    """
    pond_macrophytes = feature.attribute('pond_macrophytes')
    
    if (pond_macrophytes < 70):
        coord1 = {'x':0,'y':0.3}
        coord2 = {'x':70,'y':1}
        return get_SI(coord1,coord2,pond_macrophytes)
        
    if (pond_macrophytes > 80):
        coord1 = {'x':80,'y':1}
        coord2 = {'x':100,'y':0.8}
        return get_SI(coord1,coord2,pond_macrophytes)
        
    return 1