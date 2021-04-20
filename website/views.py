from flask import Blueprint, render_template, request, flash, redirect, url_for, session

views = Blueprint('views', __name__, template_folder='templates')

@views.route('/', methods = ['GET', 'POST'])
def home():
    return render_template('home.html')