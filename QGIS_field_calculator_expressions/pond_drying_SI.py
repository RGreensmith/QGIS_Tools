def pond_drying_SI(feature, parent):
    """
    Calculates the pond drying GCN HSI score
    pond_drying ('never', 'rarely','sometimes','annually')
    <h2>Example usage:</h2>
    <ul>
      <li>pond_drying_SI()</li>
    </ul>
    """
    pond_drying = feature.attribute('pond_drying')
    
    if (pond_drying == 'never'):
        return 0.9
        
    if (pond_drying == 'rarely'):
        return 1.0

    if (pond_drying == 'sometimes'):
        return 0.5
        
    return 0.1