import math
import time

def solar_profile():
    # Simulate solar power as sine function + trend
    t = time.time() % 86400
    # peak at noon (43200 seconds)
    base = max(0, 100 * (math.sin((t - 21600) * (2*math.pi/86400))))
    return base

def wind_profile():
    # Random with periodic gusts
    t = time.time() % 3600
    return 40 + 30 * abs(math.sin(t * (2*math.pi/3600)))

def hybrid_profile():
    # Average of solar and wind
    return (solar_profile() + wind_profile()) / 2
