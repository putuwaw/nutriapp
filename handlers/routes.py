from flask import render_template, request
from modules import branch_and_bound as bnb

def configure_routes(app):
    @app.route("/", methods=["GET", "POST"])
    def index():
        if request.method == "POST":
            limit = request.form["limit"]
            detail = request.form["detail"]
            # solve
            result = bnb.solve(limit, detail)
            # result
            maxProfit = result[0]
            selectedItems = result[1]
            graph = result[2]
            time = result[3]
            # template data
            templateData = {
                "isSubmit": True,
                "maxProfit" : maxProfit,
                "selectedItems": selectedItems,
                "graph": graph,
                "time": time
            }
            return render_template("index.html", **templateData)
        else:
            return render_template("index.html")
