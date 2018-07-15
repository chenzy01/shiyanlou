from simpledu.forms import LoginForm, RegisterForm
from flask import flash

@front.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html', form=form)


@front.route('/register', methods=['GET','POST'])
def register():
    form = RegisterForm()
    if form.validte_on_submit():
        form.create_user()
        flash('注册成功，请登录！', 'success')
        return redirect(url_for('.login'))
    return render_template('register.html', form=form)
