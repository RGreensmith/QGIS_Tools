from qgis.core import *
from qgis.gui import *

@qgsfunction(args='auto', group='Custom', referenced_columns=['pond_count'])
def pond_count_div_pi(feature, parent):
    """
    Calculates the pond count divided by pi (3.14)
    <h2>Example usage:</h2>
    <ul>
      <li>pond_count_div_pi()</li>
    </ul>
    """
    pond_count = feature.attribute('pond_count')
    return pond_count/3.14