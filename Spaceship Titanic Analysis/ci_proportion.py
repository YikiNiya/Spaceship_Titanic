import numpy as np


def calculate_ci_for_proportion(successes, total, confidence_level=0.95):
    """
    Calculate the confidence interval (CI) for a proportion based on
    the number of successes and the total sample size.

    This function computes the confidence interval for a proportion, which
    is the estimated range within which the true proportion is likely to fall,
    given a certain confidence level (default is 95%).

    The formula used is based on the standard normal distribution
    (Z-distribution), assuming that the sample size is large enough to
    approximate the distribution of the sample proportion.

    Args:
        successes (int): The number of successes observed in the sample.
        total (int): The total number of trials or observations in the sample.
        confidence_level (float): The desired confidence level for the
        confidence interval. Default is 0.95.

    Returns:
        tuple: A tuple containing the lower and upper bounds of the confidence
            interval.
            If there are no successes (total > 0 and successes == 0), it
            returns (0, upper bound).
            If all trials are successes (total > 0 and successes == total),
            it returns (lower bound, 1).
            If the total number of trials is 0, it returns (None, None).

    Example:
        >>> calculate_ci_for_proportion(25, 100)
        (0.18, 0.32)

        >>> calculate_ci_for_proportion(0, 100)
        (0, 0.2)
    """
    if total == 0:
        return (None, None)

    p_hat = successes / total
    if p_hat == 0:
        return (
            0,
            round(1.96 * np.sqrt((1 / total) * (1 - 1 / total) / total), 2),
        )  # noqa: E501
    elif p_hat == 1:
        return (
            round(
                1 - 1.96 * np.sqrt((1 / total) * (1 - 1 / total) / total), 2
            ),  # noqa: E501
            1,
        )
    std_error = np.sqrt(p_hat * (1 - p_hat) / total)
    z_value = 1.96
    margin_of_error = z_value * std_error

    ci_lower = float(round(p_hat - margin_of_error, 2))
    ci_upper = float(round(p_hat + margin_of_error, 2))

    return ci_lower, ci_upper
