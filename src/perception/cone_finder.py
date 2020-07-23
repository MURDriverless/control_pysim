from ..world.cone import Cone


def find_nearest_cone(x, y, cones, previous_index, searchable_size):
    """
    Calculate the index of the nearest forward cone from the car

    Args:
        x (float): x-position of car in global frame
        y (float): y-position of car in global frame
        cones (list of Cone): either all of left or right cones in the track
        previous_index (int): the index of the previously captured cone
        searchable_size (int): max. number of cones included in the search

    Returns:
        int: the index of the closes cone in front of the car, from a list of cones
    """
    # Only search within the position_index up to searchable_size
    searchable_cones = cyclic_fetch_elements_in_array(cones, previous_index, searchable_size)

    # Calculate difference in x and y to compute distance from one cone to next
    dx = [x - cone.x for cone in searchable_cones]
    dy = [y - cone.y for cone in searchable_cones]

    # Build a list of distances and find the minimum squared distance
    squared_distances = [idx ** 2 + idy ** 2 for (idx, idy) in zip(dx, dy)]
    min_squared_dist = min(squared_distances)

    # Since we have built a list of distances, we can just get the next cone index by searching for
    # the index of the minimum squared distance value.
    next_index = squared_distances.index(min_squared_dist) + previous_index
    # To account for overflown elements in our searchable_cones, we adjust the index by using
    # the modulo operator "%" over the total number of cones
    adjusted_index = next_index % len(cones)
    return adjusted_index


def cyclic_fetch_elements_in_array(array, start_index, searchable_size):
    """
    Fetch elements without worrying about reaching the end of the array

    Args:
        array (list of Any): anything in the form of array, can be an array of ADT
        start_index (int): the starting index to slice from
        searchable_size (int): the number of elements included from start_index

    Returns:
        list of Any
    """
    array_length = len(array)
    # Determine if start_index + searchable_size will cause an overflow, and if so,
    # calculate how many elements will exceed.
    overflow_n = start_index + searchable_size - array_length
    # If it is larger than 0, that means we have an overflow
    if overflow_n > 0:
        # We need to return 2 concatenated arrays:
        # 1. Elements from the current index to the maximum length of the array
        # 2. Elements from the start to the overflow_n
        return array[start_index:array_length] + array[0:overflow_n]
    else:
        # Else, return elements as usual using slicing
        return array[start_index:(start_index + searchable_size)]
