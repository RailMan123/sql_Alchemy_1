from flask import render_template, Flask
from data.db_session import global_init, create_session
from data.jobs import Jobs


app = Flask(__name__)


@app.route("/")
def index():
    global_init('db/blogs.sqlite')
    session = create_session()
    jobs = session.query(Jobs).all()
    return render_template("job_table.html", jobs=jobs)


def main():
    app.run()

if __name__ == '__main__':
    main()