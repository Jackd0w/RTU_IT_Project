from flask import Flask, redirect, url_for, render_template
from website import create

app = create()

#TODO Add custom error-handlers

if __name__ == "__main__":
    
    app.run(debug=True)