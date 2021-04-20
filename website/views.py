import os
from flask import Blueprint, render_template, request, redirect, flash
from website import ALLOWED_IMAGE_EXTENSION, MAXIMUM_MEMORY
from werkzeug.utils import secure_filename

views = Blueprint('views', __name__, template_folder='templates')

def check_extension(image):

    if not '.' in image:
        return False

    extension = image.split('.')[-1]
    if extension.lower() not in ALLOWED_IMAGE_EXTENSION:
        return False
    return True

def check_filesize(filesize):

    if int(filesize) > MAXIMUM_MEMORY:
        return False
    return True


@views.route('/', methods = ['GET', 'POST'])
def home():
    if request.method == 'POST':
        if request.files:
            image = request.files['image']

            if image.filename == '':
                flash('Image must have a name', category='error')
                return redirect(request.url)

            elif not check_extension(image.filename):
                flash('Image is of a wrong type (types allowed are: jpg, jpeg and png).', category='error')
                return redirect(request.url)
            elif not check_filesize(request.cookies.get('filesize')):
                flash('Image exceeded 1 MB, try a smaller one.', category='error')
                return redirect(request.url)
            else:
                filename = secure_filename(image.filename)
                image.save(os.path.join('images', filename))
                flash('Image uploaded successfully.', category='succes')

            return redirect(request.url)

    return render_template('home.html')