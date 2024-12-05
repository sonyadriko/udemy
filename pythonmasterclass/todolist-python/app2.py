from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Konfigurasi koneksi database
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:@localhost/to_do_list_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Model Task
class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    done = db.Column(db.Boolean, default=False)

# Route utama
@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        task_name = request.form.get("task")  # Ambil input dari form
        print("Received Task:", task_name)  # Tambahkan untuk cek input
        if task_name:
            new_task = Task(name=task_name)   # Buat instance Task baru
            db.session.add(new_task)          # Tambahkan ke session
            db.session.commit()
        else:
            print("No task name provided.")# Simpan perubahan ke database
        return redirect(url_for("index"))
    
    tasks = Task.query.all()                  # Ambil semua task untuk ditampilkan
    return render_template("index.html", tasks=tasks)


@app.route("/delete/<int:task_id>")
def delete_task(task_id):
    task = Task.query.get_or_404(task_id)
    db.session.delete(task)
    db.session.commit()
    return redirect(url_for("index"))

@app.route("/toggle/<int:task_id>")
def toggle_task(task_id):
    task = Task.query.get_or_404(task_id)
    task.done = not task.done
    db.session.commit()
    return redirect(url_for("index"))

if __name__ == "__main__":
    with app.app_context():
        db.create_all()  # Membuat tabel jika belum ada
    app.run(debug=True)
