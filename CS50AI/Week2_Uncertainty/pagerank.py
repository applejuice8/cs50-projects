def transition_model(corpus, page, damping_factor):
    """
    Return a probability distribution over which page to visit next,
    given a current page.

    With probability `damping_factor`, choose a link at random
    linked to by `page`. With probability `1 - damping_factor`, choose
    a link at random chosen from all pages in the corpus.
    """
    # Equal chance for random jump
    random_jump = (1 - damping_factor) / len(corpus)
    probs = {page: random_jump for page in corpus.keys()}

    # Higher chance for local jump
    links = corpus[page]

    # If no links, assume all
    if not links:
        links = list(corpus.keys())

    local_jump = damping_factor / len(links)
    for link in links:
        probs[link] += local_jump

    return probs


def sample_pagerank(corpus, damping_factor, n):
    """
    Return PageRank values for each page by sampling `n` pages
    according to transition model, starting with a page at random.

    Return a dictionary where keys are page names, and values are
    their estimated PageRank value (a value between 0 and 1). All
    PageRank values should sum to 1.
    """
    # Start count at 0
    pages = corpus.keys()
    counts = {page: 0 for page in pages}

    # Start from random page
    current_page = random.choice(list(pages))

    for _ in range(n):
        # Get probabilities of each page
        probs = transition_model(corpus, current_page, damping_factor)

        # Jump randomly based on probabilities
        current_page = random.choices(
            population=list(probs.keys()),
            weights=list(probs.values()),
            k=1
        )[0]
        counts[current_page] += 1

    # Convert count to ranks
    ranks = {}
    for page, count in counts.items():
        ranks[page] = count / n

    return ranks


def iterate_pagerank(corpus, damping_factor):
    """
    Return PageRank values for each page by iteratively updating
    PageRank values until convergence.

    Return a dictionary where keys are page names, and values are
    their estimated PageRank value (a value between 0 and 1). All
    PageRank values should sum to 1.
    """
    # Start from equal rank
    pages = corpus.keys()
    initial = 1 / len(pages)
    ranks = {page: initial for page in pages}

    # Chance for random jump
    random_jump = (1 - damping_factor) / len(pages)

    not_accurate = True
    while not_accurate:
        not_accurate = False
        new_ranks = {page: random_jump for page in pages}

        for page in pages:
            sum_links = 0

            for from_page, to_pages in corpus.items():
                # If no links, assume all
                if not to_pages:
                    to_pages = pages

                # Take rank from parent
                if page in to_pages:
                    sum_links += (ranks[from_page] / len(to_pages))
            new_ranks[page] += (damping_factor * sum_links)

        # Repeat until change less than 0.001
        for page, rank in ranks.items():
            if abs(new_ranks[page] - rank) > 0.001:
                not_accurate = True
                break
        ranks = new_ranks

    return new_ranks