from flask import Flask, render_template, request, redirect

app = Flask(__name__)

# Temporary task data
tasks = [
    {"id": 1, "title": "Learn Flask", "completed": False},
    {"id": 2, "title": "Practice Python", "completed": False},
    {"id": 3, "title": "Push project to GitHub", "completed": True}
]


@app.route("/")
def home():
    total_tasks = len(tasks)
    completed_tasks = len([task for task in tasks if task["completed"]])

    return render_template(
        "index.html",
        tasks=tasks,
        total_tasks=total_tasks,
        completed_tasks=completed_tasks
    )


@app.route("/add-task", methods=["POST"])
def add_task():
    task_title = request.form.get("task")

    if task_title:
        new_task = {
            "id": len(tasks) + 1,
            "title": task_title,
            "completed": False
        }

        tasks.append(new_task)

    return redirect("/")


@app.route("/complete/<int:task_id>")
def complete_task(task_id):

    for task in tasks:
        if task["id"] == task_id:
            task["completed"] = not task["completed"]

    return redirect("/")


@app.route("/delete/<int:task_id>")
def delete_task(task_id):

    for task in tasks:
        if task["id"] == task_id:
            tasks.remove(task)
            break

    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)
