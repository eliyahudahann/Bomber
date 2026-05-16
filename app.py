import os
import sys
import subprocess
from concurrent.futures import ThreadPoolExecutor, as_completed
from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = "change_this_secret_key"

SCRIPTS_FOLDER = "Spam"
ALWAYS_RUN = "main.py"

# פרטי התחברות
USERNAME = "Elid"
PASSWORD = "9818"


def get_scripts():

    if not os.path.isdir(SCRIPTS_FOLDER):
        return []

    scripts = []

    for filename in os.listdir(SCRIPTS_FOLDER):

        if (
            filename.endswith(".py")
            and not filename.startswith("._")
            and filename != ALWAYS_RUN
        ):

            scripts.append(filename)

    return sorted(scripts)


def run_script(filename, message):

    path = os.path.join(
        SCRIPTS_FOLDER,
        filename
    )

    if not os.path.exists(path):

        return (
            f"===== {filename} =====\n"
            f"שגיאה: הקובץ לא נמצא"
        )

    try:

        result = subprocess.run(
            [sys.executable, path, message],
            capture_output=True,
            text=True,
            timeout=30
        )

        output = (
            result.stdout
            if result.stdout
            else result.stderr
        )

        return (
            f"===== {filename} =====\n"
            f"{output}"
        )

    except Exception as e:

        return (
            f"===== {filename} =====\n"
            f"שגיאה: {e}"
        )


@app.route("/login", methods=["GET", "POST"])
def login():

    error = ""

    if request.method == "POST":

        username = request.form["username"]
        password = request.form["password"]

        if (
            username == USERNAME
            and password == PASSWORD
        ):

            session["logged_in"] = True

            return redirect(
                url_for("home")
            )

        error = "שם משתמש או סיסמה שגויים"

    return render_template(
        "login.html",
        error=error
    )


@app.route("/logout")
def logout():

    session.clear()

    return redirect(
        url_for("login")
    )


@app.route("/", methods=["GET", "POST"])
def home():

    if not session.get(
        "logged_in"
    ):

        return redirect(
            url_for("login")
        )

    scripts = get_scripts()

    if request.method == "POST":

        message = request.form.get(
            "message",
            ""
        )

        try:

            times = int(
                request.form.get(
                    "times",
                    1
                )
            )

            # מקסימום 10 סבבים
            times = min(
                max(times, 1),
                10
            )

        except:

            times = 1

        selected_scripts = (
            request.form.getlist(
                "scripts"
            )
        )

        # main.py תמיד מתווסף
        # גם אם הוא כבר קיים
        selected_scripts.insert(
            0,
            ALWAYS_RUN
        )

        outputs = []

        for i in range(times):

            workers = min(
                len(selected_scripts),
                10
            )

            with ThreadPoolExecutor(
                max_workers=workers
            ) as executor:

                futures = [

                    executor.submit(
                        run_script,
                        filename,
                        message
                    )

                    for filename
                    in selected_scripts

                ]

                for future in as_completed(
                    futures
                ):

                    outputs.append(
                        future.result()
                    )

            outputs.append(
                f"\n✅ סבב {i+1} הסתיים\n"
            )

        session[
            "response"
        ] = "\n".join(
            outputs
        )

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

    app.run(
        debug=True,
        threaded=True
    )