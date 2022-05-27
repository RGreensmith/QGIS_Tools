from qgis.core import *
from qgis.gui import *

def get_m_c(coord1,coord2):
    dy = coord2['y']-coord1['y']
    dx = coord2['x']-coord1['x']
    
    m = dy/dx
    mx = m*coord1['x']
    c = coord1['y']-mx
    
    return (m,c)


def get_SI(coord1,coord2,pond_shade):
    m,c = get_m_c(coord1,coord2)
    SI = m*pond_shade+c
    
    return SI

@qgsfunction(args='auto', group='Custom', referenced_columns=['pond_shade'])
def pond_shade_SI(feature, parent):
    """
    Calculates the pond shade GCN HSI score using straight line equation: y = mx + c
    <h2>Example usage:</h2>
    <ul>
      <li>pond_shade_SI()</li>
    </ul>
    """
    pond_shade = feature.attribute('pond_shade')
    
    if (pond_shade > 60):
        coord1 = {'x':60,'y':1}
        coord2 = {'x':100,'y':0.2}
        return get_SI(coord1,coord2,pond_shade)
        
    return 1