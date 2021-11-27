import math

import geopy.distance
from data import storage_boxes
from states import NaturalPerson


def get_nearest_storage_boxes(user_location):
    """Get nearest (in ascending order) storage boxes to user

    The function calculates for each given box the distance to the user.
    Afterward sorts it by distance and creates new ordered dictionary of boxes.
    """
    if not user_location:
        return storage_boxes
    boxes_with_distance = {}
    for box_id, box_location in storage_boxes.items():
        distance = geopy.distance.distance(user_location,
                                           box_location.get('coordinates')).km
        boxes_with_distance[box_id] = distance

    sorted_boxes_with_distance = dict(sorted(boxes_with_distance.items(), key=lambda box: box[1]))

    # sorted_boxes = {box_id: storage_boxes[box_id] for box_id in sorted_boxes.keys()}
    sorted_boxes = {}
    for box_id, box_distance in sorted_boxes_with_distance.items():
        sorted_boxes[box_id] = storage_boxes[box_id]
        sorted_boxes[box_id]['distance_to_user'] = f'{math.ceil(box_distance)} км'

    return sorted_boxes
