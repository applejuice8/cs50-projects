def joint_probability(people, one_gene, two_genes, have_trait):
    """
    Compute and return a joint probability.

    The probability returned should be the probability that
        * everyone in set `one_gene` has one copy of the gene, and
        * everyone in set `two_genes` has two copies of the gene, and
        * everyone not in `one_gene` or `two_gene` does not have the gene, and
        * everyone in set `have_trait` has the trait, and
        * everyone not in set` have_trait` does not have the trait.
    """
    prob = 1
    for person in people:
        # Number of genes
        genes = 0
        if person in one_gene:
            genes = 1
        elif person in two_genes:
            genes = 2

        # Probability of trait given genes
        prob *= PROBS['trait'][genes][person in have_trait]

        mother = people[person]['mother']
        father = people[person]['father']

        # If no parents
        if not mother and not father:
            prob *= PROBS['gene'][genes]
            continue

        # Probability of parents passing gene
        parents_prob = {mother: 1, father: 1}
        for parent in parents_prob.keys():
            parent_prob = 1
            if parent in one_gene:
                parent_prob *= 0.5
            elif parent in two_genes:
                parent_prob *= (1 - PROBS['mutation'])
            else:
                parent_prob *= PROBS['mutation']
            parents_prob[parent] = parent_prob

        mother_prob = parents_prob[mother]
        father_prob = parents_prob[father]

        # Probability of parents passing gene, given child's gene
        if genes == 2:
            prob *= mother_prob * father_prob
        elif genes == 1:
            prob *= (mother_prob * (1 - father_prob)) + ((1 - mother_prob) * father_prob)
        else:
            prob *= (1 - mother_prob) * (1 - father_prob)
    return prob


def update(probabilities, one_gene, two_genes, have_trait, p):
    """
    Add to `probabilities` a new joint probability `p`.
    Each person should have their "gene" and "trait" distributions updated.
    Which value for each distribution is updated depends on whether
    the person is in `have_gene` and `have_trait`, respectively.
    """
    for person in probabilities.keys():
        # Count genes
        genes = 0
        if person in one_gene:
            genes = 1
        elif person in two_genes:
            genes = 2

        # Update genes, traits
        probabilities[person]['gene'][genes] += p
        probabilities[person]['trait'][person in have_trait] += p
    return probabilities


def normalize(probabilities):
    """
    Update `probabilities` such that each probability distribution
    is normalized (i.e., sums to 1, with relative proportions the same).
    """
    for person, data in probabilities.items():
        # Find total
        total_gene = sum(data['gene'].values())
        total_trait = sum(data['trait'].values())

        # Divide each by total
        for gene in data['gene'].keys():
            probabilities[person]['gene'][gene] /= total_gene
        for trait in data['trait'].keys():
            probabilities[person]['trait'][trait] /= total_trait

    return probabilities