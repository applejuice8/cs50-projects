def load_data(filename):
    """
    Load shopping data from a CSV file `filename` and convert into a list of
    evidence lists and a list of labels. Return a tuple (evidence, labels).

    evidence should be a list of lists, where each list contains the
    following values, in order:
        - Administrative, an integer
        - Administrative_Duration, a floating point number
        - Informational, an integer
        - Informational_Duration, a floating point number
        - ProductRelated, an integer
        - ProductRelated_Duration, a floating point number
        - BounceRates, a floating point number
        - ExitRates, a floating point number
        - PageValues, a floating point number
        - SpecialDay, a floating point number
        - Month, an index from 0 (January) to 11 (December)
        - OperatingSystems, an integer
        - Browser, an integer
        - Region, an integer
        - TrafficType, an integer
        - VisitorType, an integer 0 (not returning) or 1 (returning)
        - Weekend, an integer 0 (if false) or 1 (if true)

    labels should be the corresponding list of labels, where each label
    is 1 if Revenue is true, and 0 otherwise.
    """
    evidence = []
    labels = []

    # Read as strings
    with open('shopping.csv') as f:
        reader = csv.reader(f)
        next(reader)

        for row in reader:
            evidence.append([cell for cell in row[:-1]])
            labels.append(1 if row[-1] == 'TRUE' else 0)

    # Convert months
    month_names = ['Jan', 'Feb', 'Mar', 'Apr', 'May',
                   'June', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    months = {}
    for i, month in enumerate(month_names):
        months[month] = i

    # Convert data types
    int_cols = [0, 2, 4, 11, 12, 13, 14]
    float_cols = [1, 3, 5, 6, 7, 8, 9]
    month_col = 10
    visitor_type_col = 15
    weekend_col = 16

    for e in evidence:
        for i, cell in enumerate(e):
            if i in int_cols:
                e[i] = int(cell)
            elif i in float_cols:
                e[i] = float(cell)
            elif i == month_col:
                e[i] = months[cell]
            elif i == visitor_type_col:
                e[i] = 0 if cell == 'New_Visitor' else 1
            elif i == weekend_col:
                e[i] = 0 if cell == 'TRUE' else 1

    return (evidence, labels)


def train_model(evidence, labels):
    """
    Given a list of evidence lists and a list of labels, return a
    fitted k-nearest neighbor model (k=1) trained on the data.
    """
    model = KNeighborsClassifier(n_neighbors=1)
    model.fit(evidence, labels)
    return model


def evaluate(labels, predictions):
    """
    Given a list of actual labels and a list of predicted labels,
    return a tuple (sensitivity, specificity).

    Assume each label is either a 1 (positive) or 0 (negative).

    `sensitivity` should be a floating-point value from 0 to 1
    representing the "true positive rate": the proportion of
    actual positive labels that were accurately identified.

    `specificity` should be a floating-point value from 0 to 1
    representing the "true negative rate": the proportion of
    actual negative labels that were accurately identified.
    """
    total_pos = 0
    total_neg = 0
    true_pos = 0
    true_neg = 0

    for i, label in enumerate(labels):
        if label == 1:
            total_pos += 1
        else:
            total_neg += 1

        # True
        if label == predictions[i]:
            if label == 1:
                true_pos += 1
            else:
                true_neg += 1

    sensitivity = true_pos / total_pos
    specificity = true_neg / total_neg
    return (sensitivity, specificity)
