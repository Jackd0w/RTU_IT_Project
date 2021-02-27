from flask import Flask, redirect, url_for, render_template
from website import create

app = create()

#TODO Add custom error-handlers
#TODO Add database
#TODO Creating new user accounts
#TODO Login


if __name__ == "__main__":
    
    app.run(debug=True)