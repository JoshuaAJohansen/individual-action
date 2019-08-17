from flask import Flask, render_template
from pandas import pandas as pd


app = Flask(__name__)


def load_solutions():
    df = pd.read_csv('./data/drawdown-solutions.csv')
    df = df[
        ['Rank', 'Solution', 'Sector', 'Individual',
         'Savings (BILLIONS US $)']]
    return df

@app.route("/individual")
@app.route("/")
def solutions():
    df = load_solutions()
    df = df[df['Individual'] == 1.0]
    return render_template("solutions.html", df=df, header="Solutions for Individuals")


@app.route("/all")
def raw_solutions():
    df = load_solutions()
    return render_template("solutions.html", df=df, header="Top 100 Solutions for Drawdown")


app.run(debug=True)