from flask import Flask, redirect, url_for, render_template
from website import create

app = create()

@app.route('/')
def home():
    return (render_template('base.html'))

#TODO Add custom error-handlers



if __name__ == "__main__":
    app.run(debug=True)