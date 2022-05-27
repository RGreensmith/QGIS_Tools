def pond_wFowl_SI(feature, parent):
    """
    Calculates the pond water fowl GCN HSI score
    pond_wFowl ('absent', 'minor','major')
    <h2>Example usage:</h2>
    <ul>
      <li>pond_drying_SI()</li>
    </ul>
    """
    pond_wFowl = feature.attribute('pond_wFowl')
    
    if (pond_wFowl == 'absent'):
        return 1.0
        
    if (pond_wFowl == 'minor'):
        return 0.67
        
    return 0.01