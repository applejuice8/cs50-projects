class Sentence():
    """
    Logical statement about a Minesweeper game
    A sentence consists of a set of board cells,
    and a count of the number of those cells which are mines.
    """

    def known_mines(self):
        """
        Returns the set of all cells in self.cells known to be mines.
        """
        if len(self.cells) == self.count:
            return self.cells
        return set()

    def known_safes(self):
        """
        Returns the set of all cells in self.cells known to be safe.
        """
        if self.count == 0:
            return self.cells
        return set()

    def mark_mine(self, cell):
        """
        Updates internal knowledge representation given the fact that
        a cell is known to be a mine.
        """
        if cell in self.cells:
            self.cells.remove(cell)
            self.count -= 1

    def mark_safe(self, cell):
        """
        Updates internal knowledge representation given the fact that
        a cell is known to be safe.
        """
        if cell in self.cells:
            self.cells.remove(cell)


class MinesweeperAI():
    """
    Minesweeper game player
    """

    def add_knowledge(self, cell, count):
        """
        Called when the Minesweeper board tells us, for a given
        safe cell, how many neighboring cells have mines in them.

        This function should:
            1) mark the cell as a move that has been made
            2) mark the cell as safe
            3) add a new sentence to the AI's knowledge base
               based on the value of `cell` and `count`
            4) mark any additional cells as safe or as mines
               if it can be concluded based on the AI's knowledge base
            5) add any new sentences to the AI's knowledge base
               if they can be inferred from existing knowledge
        """
        # Mark as move made
        self.moves_made.add(cell)
        self.mark_safe(cell)

        # 3x3 around
        (x, y) = cell
        cells = set()
        for i in range(x - 1, x + 2):
            for j in range(y - 1, y + 2):
                c = (i, j)

                # Ignore self and safes
                if c == cell or c in self.safes:
                    continue

                # Ignore mines
                if c in self.mines:
                    count -= 1
                    continue

                if 0 <= i < self.height and 0 <= j < self.width:
                    cells.add(c)

        # New sentence
        self.knowledge.append(Sentence(cells, count))

        modified = True
        while modified:
            modified = False

            # Mark safes and mines based on knowledge
            safes = set()
            mines = set()

            for sentence in self.knowledge:
                safes = safes | sentence.known_safes()
                mines = mines | sentence.known_mines()

            if safes:
                modified = True
                for safe in safes:
                    self.mark_safe(safe)

            if mines:
                modified = True
                for mine in mines:
                    self.mark_mine(mine)

            # Loop through knowledge
            for s1 in self.knowledge:
                for s2 in self.knowledge:
                    # Skip self
                    if s1 == s2:
                        continue

                    # Subtract subset
                    if s1.cells.issubset(s2.cells):
                        new_cells = s2.cells - s1.cells
                        new_count = s2.count - s1.count
                        new_sentence = Sentence(new_cells, new_count)

                        # Add new knowledge
                        if new_sentence not in self.knowledge:
                            modified = True
                            self.knowledge.append(new_sentence)

    def make_safe_move(self):
        """
        Returns a safe cell to choose on the Minesweeper board.
        The move must be known to be safe, and not already a move
        that has been made.

        This function may use the knowledge in self.mines, self.safes
        and self.moves_made, but should not modify any of those values.
        """
        for move in self.safes:
            if move not in self.moves_made:
                return move
        return None

    def make_random_move(self):
        """
        Returns a move to make on the Minesweeper board.
        Should choose randomly among cells that:
            1) have not already been chosen, and
            2) are not known to be mines
        """
        for i in range(self.height):
            for j in range(self.width):
                move = (i, j)
                if move not in self.moves_made and move not in self.mines:
                    return move
        return None
