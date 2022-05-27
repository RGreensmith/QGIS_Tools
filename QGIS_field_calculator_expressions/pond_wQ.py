def pond_waterQ_SI(feature, parent):
    """
    Calculates the pond water quality GCN HSI score
    pond_drying ('good', 'moderate','poor','bad')
    <h2>Example usage:</h2>
    <ul>
      <li>pond_drying_SI()</li>
    </ul>
    """
    pond_waterQ = feature.attribute('pond_waterQ')
    
    if (pond_waterQ == 'good'):
        return 1.0
        
    if (pond_waterQ == 'moderate'):
        return 0.67

    if (pond_waterQ == 'poor'):
        return 0.33
        
    return 0.01