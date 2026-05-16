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

        return {
            "filename": filename,
            "success": False,
            "error": "הקובץ לא נמצא"
        }

    try:

        result = subprocess.run(
            [sys.executable, path, message],
            capture_output=True,
            text=True,
            timeout=120
        )

        if result.returncode == 0:

            return {
                "filename": filename,
                "success": True,
                "error": ""
            }

        error = (
            result.stderr.strip()
            or result.stdout.strip()
            or "שגיאה לא ידועה"
        )

        return {
            "filename": filename,
            "success": False,
            "error": error
        }

    except subprocess.TimeoutExpired:

        return {
            "filename": filename,
            "success": False,
            "error": "חריגה ממגבלת זמן (120 שניות)"
        }

    except Exception as e:

        return {
            "filename": filename,
            "success": False,
            "error": str(e)
        }


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

    if not session.get("logged_in"):

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
        selected_scripts.insert(
            0,
            ALWAYS_RUN
        )

        outputs = []

        for i in range(times):

            round_errors = []

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

                    result = future.result()

                    if not result[
                        "success"
                    ]:

                        round_errors.append(
                            result
                        )

            if not round_errors:

                outputs.append(
                    f"✅ סבב {i+1} הסתיים בהצלחה"
                )

            else:

                outputs.append(
                    f"❌ סבב {i+1} הסתיים עם תקלות"
                )

                for error in round_errors:

                    outputs.append(
                        f"\n📄 {error['filename']}"
                    )

                    outputs.append(
                        f"תקלה: {error['error']}"
                    )

            outputs.append("")

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