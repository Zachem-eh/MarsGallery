import os
from flask import Flask, render_template, url_for
from flask_wtf import FlaskForm
from werkzeug.utils import redirect
from wtforms import SubmitField, FileField
from wtforms.validators import DataRequired

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum'


class LoadForm(FlaskForm):
    image = FileField('Приложите фотографию',
                      validators=[DataRequired()],
                      render_kw={'accept': 'image/*'})
    submit = SubmitField('Отправить')


@app.route('/carousel', methods=['GET', 'POST'])
def mars_gallery():
    form = LoadForm()
    images = [url_for('static', filename=f'images/{file}') for file in os.listdir('static/images')]
    print(images)
    if form.validate_on_submit():
        file = form.image.data
        filename = f'mars{len(os.listdir("static/images")) + 1}.jpg'
        save_path = os.path.join('static/images', filename)
        file.save(save_path)
        return redirect('/carousel')
    return render_template('index.html', form=form,  images=images)


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080)