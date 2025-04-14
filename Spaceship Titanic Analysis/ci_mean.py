import numpy as np


def calculate_ci_for_mean(data, confidence_level=0.95):
    """
    Calculates the confidence interval for the mean of a dataset.

    This function computes the confidence interval for the mean of a sample,
    using the normal distribution approximation. The confidence interval is
    calculated based on the sample data and a specified confidence level
    (default is 95%).

    Parameters:
    -----------
    data : array-like
        The sample data for which the confidence interval is calculated.

    confidence_level : float, optional (default=0.95)
        The confidence level for the interval. For example, 0.99 represents
        a 95% confidence level.

    Returns:
    --------
    tuple : (float, float)
        A tuple containing the lower and upper bounds of the confidence
          interval for the mean.
    """
    mean = np.mean(data)
    n = len(data)
    std_error = np.std(data, ddof=1) / np.sqrt(n)
    z_value = 1.96
    margin_of_error = z_value * std_error
    ci_lower = float(round(mean - margin_of_error, 2))
    ci_upper = float(round(mean + margin_of_error, 2))
    return ci_lower, ci_upper
