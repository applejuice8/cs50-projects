@app.route("/")
@login_required
def index():
    """Show portfolio of stocks"""
    user_id = session['user_id']
    infos = db.execute(
        'SELECT symbol, SUM(CASE WHEN price > 0 THEN shares ELSE -shares END) AS quantity FROM transactions WHERE user_id = ? GROUP BY symbol HAVING quantity > 0', user_id
    )
    cash = db.execute('SELECT cash FROM users WHERE id = ?', user_id)[0]['cash']

    total = cash

    stocks = []
    for info in infos:
        stock = lookup(info['symbol'])
        stock['shares'] = info['quantity']
        stock['value'] = stock['shares'] * stock['price']
        total += stock['value']
        stocks.append(stock)

    return render_template('index.html', stocks=stocks, cash=cash, total=total)


@app.route("/buy", methods=["GET", "POST"])
@login_required
def buy():
    """Buy shares of stock"""
    if request.method == 'POST':
        user_id = session['user_id']
        symbol = request.form.get('symbol')
        n_shares = request.form.get('shares')

        # Validate inputs
        if not symbol:
            return apology('Missing stock symbol')
        if not n_shares:
            return apology('Missing number of shares')

        try:
            n_shares = int(n_shares)
            if n_shares < 0:
                raise ValueError
        except ValueError:
            return apology('Invalid number of shares')

        # Check if user has enough cash
        rows = db.execute('SELECT * FROM users WHERE id = ?', user_id)
        cash = rows[0]['cash']

        info = lookup(symbol)
        if not info:
            return apology('Stock not found')

        cost = info['price'] * n_shares
        if cash < cost:
            return apology('Not enough money')

        # Add to db
        db.execute('INSERT INTO transactions (user_id, symbol, price, shares) VALUES(?, ?, ?, ?)',
                   user_id, symbol, info['price'], n_shares)
        db.execute('UPDATE users SET cash = ? WHERE id = ?',
                   cash - cost, user_id)
        flash(f"Bought {n_shares} {symbol} at {info['price']}")
        return redirect('/')

    return render_template('buy.html')


@app.route("/history")
@login_required
def history():
    """Show history of transactions"""
    transactions = db.execute('SELECT * FROM transactions WHERE user_id = ?', session['user_id'])
    return render_template('history.html', transactions=transactions)


@app.route("/quote", methods=["GET", "POST"])
@login_required
def quote():
    """Get stock quote."""
    if request.method == 'POST':
        symbol = request.form.get('symbol')
        if not symbol:
            return apology('Missing symbol')

        stock = lookup(symbol)
        if not stock:
            return apology('Stock not found')
        return render_template('quoted.html', stock=stock)

    return render_template('quote.html')


@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""
    if request.method == 'POST':
        username = request.form.get('username')
        pw = request.form.get('password')
        confirm_pw = request.form.get('confirmation')

        # Validate inputs
        if not username:
            return apology('Missing username')
        if not pw:
            return apology('Missing password')
        if pw != confirm_pw:
            return apology('Passwords do not match')

        # Add to db if username valid
        try:
            pw_hash = generate_password_hash(pw)
            db.execute('INSERT INTO users(username, hash) VALUES(?, ?)', username, pw_hash)
        except ValueError:
            return apology('Username unavailable')

        # Log user in
        rows = db.execute('SELECT * FROM users WHERE username = ?', username)
        session['user_id'] = rows[0]['id']
        return redirect('/')

    return render_template('register.html')


@app.route("/sell", methods=["GET", "POST"])
@login_required
def sell():
    """Sell shares of stock"""
    user_id = session['user_id']
    rows = db.execute(
        'SELECT symbol, SUM(shares) AS quantity FROM transactions WHERE user_id = ? GROUP BY symbol HAVING quantity > 0', user_id
    )
    symbols = [row['symbol'] for row in rows]

    if request.method == 'POST':
        symbol = request.form.get('symbol')
        n_shares = request.form.get('shares')

        # Validate inputs
        if not symbol:
            return apology('Missing stock symbol')
        if symbol not in symbols:
            return apology('Invalid stock')
        if not n_shares:
            return apology('Missing number of shares')

        try:
            n_shares = int(n_shares)
        except ValueError:
            return apology('Invalid number of shares')

        # Check if user has enough shares
        for row in rows:
            if row['symbol'] == symbol and row['quantity'] < n_shares:
                return apology('Not enough shares to sell')

        # Sell
        info = lookup(symbol)
        if not info:
            return apology('Stock not found')

        cash = db.execute('SELECT cash FROM users WHERE id = ?', user_id)[0]["cash"]
        cost = info['price'] * n_shares
        db.execute('INSERT INTO transactions (user_id, symbol, price, shares) VALUES(?, ?, ?, ?)',
                   user_id, symbol, -info['price'], n_shares)
        db.execute('UPDATE users SET cash = ? WHERE id = ?',
                   cash + cost, user_id)
        flash(f"Sold {n_shares} {symbol} at {info['price']}")
        return redirect('/')

    return render_template('sell.html', symbols=symbols)


@app.route('/change-password', methods=['GET', 'POST'])
def change_password():
    if request.method == 'POST':
        user_id = session['user_id']
        old_pw = request.form.get('old-password')
        new_pw = request.form.get('new-password')
        confirm_pw = request.form.get('confirmation')

        # Validate inputs
        if not old_pw or not new_pw or not confirm_pw:
            return apology('Missing password')
        if new_pw != confirm_pw:
            return apology('Passwords do not match')

        # Validate old password
        old_hash = db.execute('SELECT hash FROM users WHERE id = ?', user_id)[0]['hash']
        if not check_password_hash(old_hash, old_pw):
            return apology('Wrong password')

        new_hash = generate_password_hash(new_pw)
        db.execute('UPDATE users SET hash = ? WHERE id = ?', new_hash, user_id)
        flash('Password changed')
        return redirect('/')

    return render_template('change_password.html')
