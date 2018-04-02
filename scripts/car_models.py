#TODO: Redo these after revising list comprehension

cars = {
    'Ford': ['Falcon', 'Focus', 'Festiva', 'Fairlane'],
    'Holden': ['Commodore', 'Captiva', 'Barina', 'Trailblazer'],
    'Nissan': ['Maxima', 'Pulsar', '350Z', 'Navara'],
    'Honda': ['Civic', 'Accord', 'Odyssey', 'Jazz'],
    'Jeep': ['Grand Cherokee', 'Cherokee', 'Trailhawk', 'Trackhawk']
}


def get_all_jeeps():
    """return a comma separated string of jeep models (original order)"""
    return ", ".join(cars['Jeep'])
    


def get_first_model_each_manufacturer():
    """return a list of matching models (original ordering)"""
    first_model = []
    for model in cars.keys():
        first_model.append(cars[model][0])
        
    return first_model


def get_all_matching_models(grep='trail'):
    """return a list of all models containing the case insensitive
       'grep' string which defaults to 'trail' for this exercise,
       sort the resulting sequence alphabetically"""
    trail_models = []
    for keys in cars.keys():
        for model in cars[keys]:
            if grep.lower() in model.lower():
                trail_models.append(model)
    
    trail_models.sort()
    return trail_models


def sort_car_models():
    """sort the car models (values) and return the resulting cars dict"""
    sorted_cars = {}
    for model, model_cars in cars.items():
        model_cars.sort()
        sorted_cars[model] = model_cars
        
    return sorted_cars
