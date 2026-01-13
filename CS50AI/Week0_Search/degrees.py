def shortest_path(source, target):
    """
    Returns the shortest list of (movie_id, person_id) pairs
    that connect the source to the target.

    If no possible path, returns None.
    """
    frontier = QueueFrontier()
    start = Node(source, None, None)
    frontier.add(start)

    explored = set()
    while not frontier.empty():
        node = frontier.remove()
        explored.add(node.state)

        # If found target, backtrack
        if node.state == target:
            path = []
            while node.parent:
                path.append((node.action, node.state))
                node = node.parent
            path.reverse()
            return path

        # Explore each movie
        movie_ids = people[node.state]['movies']
        for movie_id in movie_ids:
            stars = movies[movie_id]['stars']
            for star in stars:
                if star not in explored and not frontier.contains_state(star):
                    frontier.add(Node(star, node, movie_id))
    return None
