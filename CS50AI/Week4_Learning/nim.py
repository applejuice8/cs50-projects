    def get_q_value(self, state, action):
        """
        Return the Q-value for the state `state` and the action `action`.
        If no Q-value exists yet in `self.q`, return 0.
        """
        q_val = self.q.get((tuple(state), tuple(action)))
        return q_val if q_val else 0

    def update_q_value(self, state, action, old_q, reward, future_rewards):
        """
        Update the Q-value for the state `state` and the action `action`
        given the previous Q-value `old_q`, a current reward `reward`,
        and an estiamte of future rewards `future_rewards`.

        Use the formula:

        Q(s, a) <- old value estimate
                   + alpha * (new value estimate - old value estimate)

        where `old value estimate` is the previous Q-value,
        `alpha` is the learning rate, and `new value estimate`
        is the sum of the current reward and estimated future rewards.
        """
        new_q = old_q + self.alpha * ((reward + future_rewards) - old_q)
        self.q[(tuple(state), tuple(action))] = new_q

    def best_future_reward(self, state):
        """
        Given a state `state`, consider all possible `(state, action)`
        pairs available in that state and return the maximum of all
        of their Q-values.

        Use 0 as the Q-value if a `(state, action)` pair has no
        Q-value in `self.q`. If there are no available actions in
        `state`, return 0.
        """
        available = Nim.available_actions(state)
        if not available:
            return 0

        state_tuple = tuple(state)
        max_q = 0
        for (s, a), q_val in self.q.items():
            if s == state_tuple and a in available:
                max_q = max(max_q, q_val)
        return max_q

    def choose_action(self, state, epsilon=True):
        """
        Given a state `state`, return an action `(i, j)` to take.

        If `epsilon` is `False`, then return the best action
        available in the state (the one with the highest Q-value,
        using 0 for pairs that have no Q-values).

        If `epsilon` is `True`, then with probability
        `self.epsilon` choose a random available action,
        otherwise choose the best action available.

        If multiple actions have the same Q-value, any of those
        options is an acceptable return value.
        """
        available = list(Nim.available_actions(state))

        # Random
        if epsilon and random.random() < self.epsilon:
            return random.choice(available)

        # Greedy
        best_q = self.best_future_reward(state)
        best_move = None
        state_tuple = tuple(state)
        for (s, a), q_val in self.q.items():
            if s == state_tuple and a in available and q_val == best_q:
                best_move = a

        if best_move:
            return best_move
        return random.choice(available)
