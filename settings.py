def getSettings():
        
    settings = {        
        # Amputee model. COM velocity weight at zero
        '0': {
            'model': 'Hamner_modified_amp',
            'targetSpeed': 1.33,
            'N': 25,
            'comVelocityTerm': 0},
      
        # Amputee model. COM velocity weight to 1000 (default)
          '1': {
              'model': 'Hamner_modified_amp',
              'targetSpeed': 1.33,
              'N': 25},
        
        # Amputee model. COM velocity weight to 50000
        '2': {
            'model': 'Hamner_modified_amp',
            'targetSpeed': 1.33,
            'N': 25,
            'comVelocityTerm': 50000},
      
        # Amputee model. COM velocity weight to 1000000
        '3': {
            'model': 'Hamner_modified_amp',
            'targetSpeed': 1.33,
            'N': 25,
            'comVelocityTerm': 1000000},
            
        }    
    
    return settings
