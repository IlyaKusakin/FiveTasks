"""
Module with variables that define features, it types and codes,
which are necessary for classifier.

"""
cat_features = ['month', 'job']
cont_features = ['age',  'nr.employed']

check_types_dict = {'job': [str], 'month': [str],
                    'age': [float, int], 'nr.employed': [float, int]}

cat_labels_dict = {
    'contact':
        {'cellular': 0, 'telephone': 1},
    'job':{
        'admin.': 0,
        'blue-collar': 1,
        'entrepreneur': 2,
        'housemaid': 3,
        'management': 4,
        'retired': 5,
        'self-employed': 6,
        'services': 7,
        'student': 8,
        'technician': 9,
        'unemployed': 10,
        'unknown': 11
        },
    'month':{
        'apr': 0,
        'aug': 1,
        'dec': 2,
        'jul': 3,
        'jun': 4,
        'mar': 5,
        'may': 6,
        'nov': 7,
        'oct': 8,
        'sep': 9,
        'feb': 10,
        'jan': 11
        },
    'poutcome':
        {'failure': 0, 'nonexistent': 1, 'success': 2}
    }    