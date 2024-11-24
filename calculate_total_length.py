def calculate_total_length(tracks: dict, transitions: list) -> float:
    """
    Calculate the total length of the output video.

    The total length is determined by the longest track.
    To find the longest track, locate the very last clip
    and add its duration to its start time.

    :param tracks: A dictionary representing the video tracks.
    :param transitions: A list of transition objects (not used in this implementation).
    :return: The total length of the output video as a float.
    """
    max_length = 0

    # Iterate over all tracks and their clips
    for track in tracks.values():
        for clip in track["clips"]:
            end = clip["timelineTrackStart"] + clip["duration"]
            if end > max_length:
                max_length = end

    return max_length