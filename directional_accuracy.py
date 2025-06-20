import numpy as np
def calculate_directional_accuracy(actual_prices, predicted_prices):
    """
    Calculate the directional accuracy of price predictions.

    Parameters:
        actual_prices (np.array): Actual prices.
        predicted_prices (np.array): Predicted prices.

    Returns:
        float: Directional accuracy as a percentage.
    """
    # Calculate directions (1 for up, -1 for down)
    actual_direction = np.sign(np.diff(actual_prices.flatten()))
    predicted_direction = np.sign(np.diff(predicted_prices.flatten()))

    # Compare directions
    correct_predictions = np.sum(actual_direction == predicted_direction)
    total_predictions = len(actual_direction)

    # Calculate accuracy
    directional_accuracy = (correct_predictions / total_predictions) * 100

    return directional_accuracy