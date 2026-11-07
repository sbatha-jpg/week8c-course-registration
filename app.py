
from flask import Flask, request, render_template_string

app = Flask(__name__)

students = []

html = """
<h2>Online Student Course Registration</h2>

<form method="POST">
    Student Name:
    <input type="text" name="name" required><br><br>

    Department:
    <input type="text" name="department" required><br><br>

    Select Course:
    <select name="course">
        <option>Python</option>
        <option>Java</option>
        <option>Web Development</option>
        <option>Data Science</option>
    </select><br><br>

    <button type="submit">Register</button>
</form>

<h3>Registered Students</h3>

<table border="1" cellpadding="10">
<tr>
    <th>Name</th>
    <th>Department</th>
    <th>Course</th>
</tr>

{% for s in students %}
<tr>
    <td>{{ s.name }}</td>
    <td>{{ s.department }}</td>
    <td>{{ s.course }}</td>
</tr>
{% endfor %}
</table>
"""

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        students.append({
            "name": request.form["name"],
            "department": request.form["department"],
            "course": request.form["course"]
        })

    return render_template_string(html, students=students)

if __name__ == "__main__":
    app.run(debug=True)
