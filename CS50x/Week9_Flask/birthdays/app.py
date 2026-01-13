@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":

        # TODO: Add the user's entry into the database
        try:
            name = request.form.get('name')
            month = int(request.form.get('month'))
            day = int(request.form.get('day'))

            if (name and month and day) and (1 <= month <= 12 and 1 <= day <= 31):
                db.execute('INSERT INTO birthdays(name, month, day) VALUES(?, ?, ?)', name, month, day)
            else:
                raise ValueError

        except ValueError:
            print('Invalid birthday')
        return redirect("/")

    else:

        # TODO: Display the entries in the database on index.html
        birthdays = db.execute('SELECT * FROM birthdays')
        return render_template("index.html", birthdays=birthdays)
