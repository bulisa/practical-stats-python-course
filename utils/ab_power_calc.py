import math
from scipy.stats import norm

def ab_power(n_per_group, p_control, uplift=0.02, alpha=0.05, two_tailed=True):
    p_variant = p_control * (1 + uplift)
    p_pool = (p_control + p_variant) / 2.0
    z_alpha = norm.ppf(1 - alpha/2 if two_tailed else 1 - alpha)
    se = math.sqrt(2 * p_pool * (1 - p_pool) / n_per_group)
    z = (p_variant - p_control) / se
    # Approximate power
    return float(norm.cdf(z - z_alpha))

if __name__ == "__main__":
    print("Power:", ab_power(5000, 0.1, uplift=0.05))
