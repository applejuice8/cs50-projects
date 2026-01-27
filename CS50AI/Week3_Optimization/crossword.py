# generate.py

    def enforce_node_consistency(self):
        """
        Update `self.domains` such that each variable is node-consistent.
        (Remove any values that are inconsistent with a variable's unary
         constraints; in this case, the length of the word.)
        """
        # Remove var that are different length
        for var, doms in self.domains.items():
            for word in set(doms):
                if len(word) != var.length:
                    self.domains[var].remove(word)

    def revise(self, x, y):
        """
        Make variable `x` arc consistent with variable `y`.
        To do so, remove values from `self.domains[x]` for which there is no
        possible corresponding value for `y` in `self.domains[y]`.

        Return True if a revision was made to the domain of `x`; return
        False if no revision was made.
        """
        x_overlap, y_overlap = self.crossword.overlaps[(x, y)]

        changes_made = False
        for x_word in set(self.domains[x]):
            overlap_char = x_word[x_overlap]

            # Check if any word in y matches x
            if not any(overlap_char == y_word[y_overlap] for y_word in self.domains[y]):
                self.domains[x].remove(x_word)
                changes_made = True

        return changes_made

    def ac3(self, arcs=None):
        """
        Update `self.domains` such that each variable is arc consistent.
        If `arcs` is None, begin with initial list of all arcs in the problem.
        Otherwise, use `arcs` as the initial list of arcs to make consistent.

        Return True if arc consistency is enforced and no domains are empty;
        return False if one or more domains end up empty.
        """
        # Initial list
        queue = []
        if arcs is not None:
            queue = list(arcs)
        else:
            for var_tuple, overlap in self.crossword.overlaps.items():
                if overlap:
                    queue.append(var_tuple)

        while queue:
            x, y = queue.pop(0)

            if self.revise(x, y):
                # No solution
                if len(self.domains[x]) == 0:
                    return False

                # Ensure other arcs consistent
                for z in (self.crossword.neighbors(x)):
                    if z == y:
                        continue
                    queue.append((z, x))

        return True

    def assignment_complete(self, assignment):
        """
        Return True if `assignment` is complete (i.e., assigns a value to each
        crossword variable); return False otherwise.
        """
        # Check if all var assigned
        return len(assignment) == len(self.crossword.variables)

    def consistent(self, assignment):
        """
        Return True if `assignment` is consistent (i.e., words fit in crossword
        puzzle without conflicting characters); return False otherwise.
        """
        for var1, word1 in assignment.items():
            # Unary constraint
            if var1.length != len(word1):
                return False

            for var2, word2 in assignment.items():
                if var1 == var2:
                    continue

                # Binary constraint
                overlap = self.crossword.overlaps[(var1, var2)]
                if overlap is not None:
                    overlap1, overlap2 = overlap
                    if word1[overlap1] != word2[overlap2]:
                        return False
        return True

    def order_domain_values(self, var, assignment):
        """
        Return a list of values in the domain of `var`, in order by
        the number of values they rule out for neighboring variables.
        The first value in the list, for example, should be the one
        that rules out the fewest values among the neighbors of `var`.
        """
        counts = {}

        for word1 in self.domains[var]:
            count = 0

            for var2 in self.crossword.neighbors(var):
                if var2 in assignment:
                    continue

                overlap = self.crossword.overlaps[(var, var2)]
                if overlap is None:
                    continue

                overlap1, overlap2 = overlap
                for word2 in self.domains[var2]:
                    # Ruled out word2
                    if word1[overlap1] != word2[overlap2]:
                        count += 1
            counts[word1] = count

        # Sort by ascending words ruled out
        return sorted(counts, key=lambda word: counts[word])

    def select_unassigned_variable(self, assignment):
        """
        Return an unassigned variable not already part of `assignment`.
        Choose the variable with the minimum number of remaining values
        in its domain. If there is a tie, choose the variable with the highest
        degree. If there is a tie, any of the tied variables are acceptable
        return values.
        """
        # Get all unassigned
        unassigned = []
        for var in self.crossword.variables:
            if var not in assignment:
                unassigned.append(var)

        # Find minimum domain
        min_doms = min(len(self.domains[var]) for var in unassigned)
        vars_min = [var for var in unassigned if len(self.domains[var]) == min_doms]

        if len(vars_min) == 1:
            return vars_min[0]

        # Tie, choose highest degree
        max_count = -1
        max_var = None
        for var in vars_min:
            count = 0
            for neighbor in self.crossword.neighbors(var):
                if neighbor not in assignment:
                    count += 1
            if count > max_count:
                max_count = count
                max_var = var

        return max_var

    def backtrack(self, assignment):
        """
        Using Backtracking Search, take as input a partial assignment for the
        crossword and return a complete assignment if possible to do so.

        `assignment` is a mapping from variables (keys) to words (values).

        If no assignment is possible, return None.
        """
        # Base
        if self.assignment_complete(assignment):
            return assignment

        var = self.select_unassigned_variable(assignment)
        for value in self.order_domain_values(var, assignment):
            if self.consistent(assignment):
                assignment[var] = value
                result = self.backtrack(assignment)
                if result is not None:
                    return result
                del assignment[var]
        return None