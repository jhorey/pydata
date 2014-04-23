"""
Simple lookup for US Census requests. 
These codes are for the population & housing tables at the block level. 
https://www.census.gov/developers/data/sf1.xml
"""

econ = {
    'median': 'DP03_0062E',
    'mean': 'DP03_0063E',
    'capita' : 'DP03_0088E'
}

pop = {
    'population' : {
        'total' : 'P0010001',
        'white' : 'P0030002',
        'black' : 'P0030003',
        'native' : 'P0030004',
        'asian' : 'P0030005',
        'pacific' : 'P0030006',
        'latino' : 'P0040003'
        },
    'age' : {
        'male' : {
            'child' : ['P0120003', 'P0120004', 'P0120005'],
            'teenager' : ['P0120006', 'P0120007'],
            'young' : ['P0120008', 'P0120009', 'P0120010', 'P0120011', 'P0120012'],
            'adult' : ['P0120013', 'P0120014', 'P0120015'],
            'mid': ['P0120016', 'P0120017', 'P0120018'],
            'older': ['P0120019', 'P0120020', 'P0120021'],
            'oldest': ['P0120022', 'P0120023', 'P0120024', 'P0120025'] 
            },
        'female' : {
            'child' : ['P0120027', 'P0120028', 'P0120029'],
            'teenager' : ['P0120030', 'P0120031'],
            'young' : ['P0120032', 'P0120033', 'P0120034', 'P0120035', 'P0120036'],
            'adult' : ['P0120037', 'P0120038', 'P0120039'],
            'mid': ['P0120040', 'P0120041', 'P0120042'],
            'older': ['P0120043', 'P0120044', 'P0120045'],
            'oldest': ['P0120046', 'P0120047', 'P0120048', 'P0120049'] 
            }
        },
    'household' : {
        'family' : ['P0180002'],
        'pair' : ['P0180003'],
        'single' : ['P0180005', 'P0180006']
        },
    'families': {
        'total' : 'P0350001',
        'white' : 'P035A001',
        'black' : 'P035B001', 
        'native': 'P035C001',
        'asian': 'P035D001',
        'pacific': 'P035E001',
        'latino' : 'P035H001'
        }
    }
