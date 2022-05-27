def pond_location_SI(feature, parent):
    """
    Calculates the pond location GCN HSI score
    <h2>Example usage:</h2>
    <ul>
      <li>pond_location_SI()</li>
    </ul>
    """
    pond_location = feature.attribute('pond_location')
    
    if (pond_location == 'a'):
        return 1
        
    if (pond_location == 'b'):
        return 0.5
        
    return 0.01