#  Write a function that stores info about a car in a dict.
# The funct should always receive a manufacturere and a model name.
def custom(manufacturer, model, **car_info):
    """Build a dictionary that sotres info on a car."""
    car_info['maker'] = manufacturer
    car_info['model'] = model
    return car_info
