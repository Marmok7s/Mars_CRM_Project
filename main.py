from flask import Flask, render_template, redirect
from scripts import db_session
from scripts.models.registration_form import RegisterForm
from scripts.models.users import User
from scripts.getter import get_data


app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


@app.route('/')
def starting_page():
    return render_template('base.html')


@app.route('/register', methods=['GET', 'POST'])
def reqister():
    form = RegisterForm()
    if form.validate_on_submit():
        if form.password.data != form.password_again.data:
            return render_template('register.html', title='Registration', form=form,
                                   message="Passwords are not same")
        session = db_session.create_session()
        if session.query(User).filter(User.email == form.email.data).first():
            return render_template('register.html', title='Registration', form=form,
                                   message="There are already user with this name")
        user = User(
            name=form.name.data,
            email=form.email.data)
        user.set_password(form.password.data)
        session.add(user)
        session.commit()
        return redirect('/login')
    return render_template('register.html', title='Registration', form=form)


@app.route('/a/<page>')
def page(page):
    return render_template('items.html', title=page, items=get_data("db/mars_workers.db", 'items'))


@app.route('/a/<page>/<part>')
def part_page(page, part):
    return render_template('base.html', title=part)


def main():
    db_session.global_init("db/mars_workers.db")

    app.run(port=8081, host='127.0.0.1')


if __name__ == '__main__':
    main()