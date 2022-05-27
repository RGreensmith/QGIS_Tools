def pond_fish_SI(feature, parent):
    """
    Calculates the pond fish GCN HSI score
    pond_fish ('absent', 'possible','minor','major')
    <h2>Example usage:</h2>
    <ul>
      <li>pond_fish_SI()</li>
    </ul>
    """
    pond_fish = feature.attribute('pond_fish')
    
    if (pond_fish == 'absent'):
        return 1.0
        
    if (pond_fish == 'possible'):
        return 0.67

    if (pond_fish == 'minor'):
        return 0.33
        
    return 0.01