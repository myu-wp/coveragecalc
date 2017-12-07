import numpy as np


OUTPUTS = [
    'primary phone is valid',
    'primary phone to name',
    'primary phone to address',
    'primary phone line type',
    'primary phone is prepaid',
    'primary phone is commercial',
    'primary address is valid',
    'primary address diagnostic',
    'primary address to name',
    'primary address type',
    'primary address is active',
    'primary address is commercial',
    'primary address is forwarder',
    'secondary phone is valid',
    'secondary phone to name',
    'secondary phone to address',
    'secondary phone line type',
    'secondary phone is prepaid',
    'secondary phone is commercial',
    'secondary address is valid',
    'secondary address diagnostic',
    'secondary address to name',
    'secondary address type',
    'secondary address is active',
    'secondary address is commercial',
    'secondary address is forwarder',
    'email is valid',
    'email is disposable',
    'email is auto-generated',
    'email to name',
    'email first seen days binned',
    'ip is valid',
    'ip distance from address binned',
    'ip distance from phone binned',
    'ip is proxy',
    'ip connection type',
    'confidence score binned',
]

BINS = {
    'email first seen days': {
        'labels': ['Never', '< 3 months', '3 months to a year', '1-4 years', '5+ years'],
        'bins': [0, 1, 180, 365, 1825, np.inf],
    },
    'ip distance from address': {
        'labels': ['0-9', '10-99', '100-999', '1000+'],
        'bins': [0, 10, 100, 1000, np.inf],
    },
    'ip distance from phone': {
        'labels': ['0-9', '10-99', '100-999', '1000+'],
        'bins': [0, 10, 100, 1000, np.inf],
    },
    'confidence score': {
        'bins': np.arange(0,525,25),
        'labels': ['0-25', '25-50', '50-75', '75-100', '100-125', '125-150', 
                   '150-175', '175-200', '200-225', '225-250', '250-275',
                   '275-300', '300-325', '325-350', '350-375', '375-400',
                   '400-425', '425-450', '450-475', '475-500',],
    },
}

to_name = [
    'Match',
    'No match',
    'No name found',
]
to_address = [
    'Match',
    'Zip+4 match',
    'Postal match',
    'City/State match',
    'No match',
]
line_type = [
    'Mobile',
    'Landline',
    'Fixed VOIP',
    'Non-fixed VOIP',
    'Premium',
    'Tollfree',
    'Voicemail',
    'Other',
    'Unknown',
]
address_type = [
    'Commercial mail drop',
    'Multi unit',
    'Single unit',
    'PO box',
    'PO box throwback',
    'Unknown address type',
]
address_diagnostic = [
    'Validated',
    'Validated with  corrections',
    'Validated only Street, Postcode, City, Country. Premise not validated',
    'Validated only Postcode, City, Country',
    'Validated only City, Country',
    'Validated only Country',
]
CATEGORIES = {
    'primary phone to name': to_name,
    'secondary phone to name': to_name,
    'primary address to name': to_name,
    'secondary address to name': to_name,
    'email to name': to_name,
    'primary phone to address': to_address,
    'secondary phone to address': to_address,
    'primary phone line type': line_type,
    'secondary phone line type': line_type,
    'primary address type': address_type,
    'secondary address type': address_type,
    'primary address diagnostic': address_diagnostic,
    'secondary address diagnostic': address_diagnostic,
    'ip connection type': [
        'Cable/DSL',
        'Corporate',
        'Cellular',
        'Dialup',
    ],
}