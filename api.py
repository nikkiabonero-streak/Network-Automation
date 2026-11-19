
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():

    results = None
    error = None

    if request.method == "POST":
        task = request.form.get("task", "").strip()

        if task:
            results = f"Task received successfully: {task}"
        else:
            error = "Please enter a task."

    return render_template(
        "index.html",
        results=results,
        error=error
    )

if __name__ == "__main__":
    app.run(debug=True)
