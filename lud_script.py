### SHHHH
### WHAT ARE YOU DOING HERE!


# Don't judge it, it's a simple code and probably have bugs
# luckily you won't read this, HA HA
# so... if you keep reading this, what's up!?
def record_temp(list_temps, function, classification = 3):
    """Calculates the maximum record of consecutive days with that classification of temperature given a list.

    Args:
        list_temps (list): List of temperatures
        function (function): Function to classify them (exercise 3)
        classification (int, optional): Type of day to get the max record. Defaults to 3.

    Returns:
        Max record (int): Maximum number of consecutive days with that classification. If there were not prints a message and returns 0.
    """
    lst = [function(i) for i in list_temps]
    i = 0
    lens = []
    while i < len(lst):
        c = 0
        if lst[i] == classification:
            c += 1
            #start counting
            i += 1
            while i < len(lst):
                if lst[i] == classification:
                    c += 1
                    i += 1
                else:
                    break
            lens.append(c)
                
        i += 1
    if len(lens) == 0:
        print("There were no days with that kind of temperature")
        return 0
    else:
        return max(lens)