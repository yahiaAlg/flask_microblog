import os
from pprint import pprint
from flask import Flask, render_template, request
from datetime import datetime
import json
from dotenv import find_dotenv, load_dotenv
def create_app():
    app = Flask(__name__)
    load_dotenv(find_dotenv(), override=True)
    @app.route("/", methods=["GET", "POST"])
    def index():
        if "DATABASE_PATH" in os.environ:
            if os.path.exists(os.environ['DATABASE_PATH']):
                with open(os.environ['DATABASE_PATH']) as db:
                    comments = json.load(db)
            else:
                comments = []
            if request.method == "POST":
                if "add" in request.form:
                    comments.append({
                        "title":request.form.get("comment")[:15],
                        "content":request.form.get("comment"),
                        "publish_date":datetime.today().strftime("%Y-%M-%d"),
                        "formatted_date":datetime.today().strftime("%b %d")
                    })
                    with open(os.environ['DATABASE_PATH'], "w") as db:
                        json.dump(comments,db)
                        print("dumped:")
                        pprint(comments)       
                        print("into database successfully")
                elif "delete" in request.form:
                    os.unlink(os.environ['DATABASE_PATH'])
                    print("database deleted successfully!")
                    
            else:
                print("loaded:")
                pprint(comments)
                print("from database successfully")
        else:
            comments = ["No database path was found in env vars!"]

        return render_template("index.html", comments=comments)
    
    return app