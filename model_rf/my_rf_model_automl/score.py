import os

from cloudpickle import cloudpickle

"""
   Inference script. This script is used for prediction by scoring server when schema is unknown.
"""


def load_model():
    """
    Loads model from the serialized format

    Returns
    -------
    model:  a model instance on which predict API can be invoked
    """
    with open(os.path.join(os.path.dirname(os.path.realpath(__file__)), "model.pkl"), "rb") as file:
        return cloudpickle.load(file)


def predict(model, data):
    """
    Returns prediction given the model and data to predict

    Parameters
    ----------
    model: Model instance returned by load_model API
    data: Data in binary format received by scoring server
        This data should be converted to the format that the model.predict() API expects

    Returns
    -------
    predictions: Output from scoring server
        This result is sent over ReST

    """
    data = _handle_input(data)
    return _handle_output(model.predict(data))


def _handle_input(data):
    """
    Convert input data to the format that model expects

    Parameters
    ----------
    data: input data

    Returns
    -------
    transformed_input: Should match the input format for model.predict() API
    """
    #############################
    # To be updated if required #
    #############################
    return data


def _handle_output(predictions):
    """
    Converts output to the format that model prediction endpoint should return

    Returns
    -------
    transformed_output: Predict endpoint response
    """
    #############################
    # To be updated if required #
    #############################
    return predictions
