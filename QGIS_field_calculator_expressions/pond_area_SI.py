from qgis.core import *
from qgis.gui import *

def get_m_c(coord1,coord2):
    dy = coord2['y']-coord1['y']
    dx = coord2['x']-coord1['x']
    
    m = dy/dx
    mx = m*coord1['x']
    c = coord1['y']-mx
    
    return (m,c)


def get_SI(coord1,coord2,pond_area):
    m,c = get_m_c(coord1,coord2)
    SI = m*pond_area+c
    
    return SI


@qgsfunction(args='auto', group='Custom', referenced_columns=['pond_area'])
def pond_area_SI(feature, parent):
    """
    Calculates the pond area GCN HSI score using straight line equation: y = mx + c
    <h2>Example usage:</h2>
    <ul>
      <li>pond_area_SI()</li>
    </ul>
    """
    pond_area = feature.attribute('pond_area')
    
    if (pond_area < 500):
        coord1 = {'x':0,'y':0}
        coord2 = {'x':400,'y':0.8}
        return get_SI(coord1,coord2,pond_area)
    
    if (pond_area <700):
        return 1
        
    if (pond_area < 2000):
        coord1 = {'x':700,'y':1}
        coord2 = {'x':2000,'y':0.8}
        return get_SI(coord1,coord2,pond_area)
        
    return -9999