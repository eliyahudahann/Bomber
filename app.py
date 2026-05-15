import os
import subprocess
from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = "change_this_secret_key"

SCRIPTS_FOLDER = "Spam"
ALWAYS_RUN = "main.py"

# פרטי התחברות
USERNAME = "Elid"
PASSWORD = "9818"


def get_scripts():
    scripts = []

    for filename in os.listdir(SCRIPTS_FOLDER):
        if (
            filename.endswith(".py")
            and not filename.startswith("._")
            and filename != ALWAYS_RUN
        ):
            scripts.append(filename)

    return sorted(scripts)


# התחברות
@app.route("/login", methods=["GET", "POST"])
def login():
    error = ""

    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        if username == USERNAME and password == PASSWORD:
            session["logged_in"] = True
            return redirect(url_for("home"))
        else:
            error = "שם משתמש או סיסמה שגויים"

    return render_template(
        "login.html",
        error=error
    )


# התנתקות
@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("login"))


@app.route("/", methods=["GET", "POST"])
def home():

    # אם לא מחובר → מסך התחברות
    if not session.get("logged_in"):
        return redirect(url_for("login"))

    scripts = get_scripts()

    if request.method == "POST":
        message = request.form["message"]
        times = int(request.form.get("times", 1))

        selected_scripts = request.form.getlist("scripts")

        # main.py תמיד ראשון
        selected_scripts.insert(0, ALWAYS_RUN)

        outputs = []

        for i in range(times):

            for filename in selected_scripts:

                path = os.path.join(
                    SCRIPTS_FOLDER,
                    filename
                )

                if not os.path.exists(path):
                    continue

                try:

                    result = subprocess.run(
                        ["py", path, message],
                        capture_output=True,
                        text=True,
                        timeout=30
                    )

                    output = (
                        result.stdout
                        if result.stdout
                        else result.stderr
                    )

                    outputs.append(
                        f"===== {filename} =====\n{output}"
                    )

                except Exception as e:

                    outputs.append(
                        f"===== {filename} =====\nשגיאה: {e}"
                    )

            outputs.append(
                f"\n✅ סבב {i+1} הצליח\n"
            )

        session["response"] = "\n".join(outputs)

        return redirect(
            url_for("home")
        )

    response = session.pop(
        "response",
        ""
    )

    return render_template(
        "index.html",
        scripts=scripts,
        response=response
    )


if __name__ == "__main__":
    app.run(debug=True)