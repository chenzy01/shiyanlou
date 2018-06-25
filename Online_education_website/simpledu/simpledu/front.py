from simpledu.forms import LoginForm, RegisterForm


@front.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html', form=form)


@front.register('/register')
def register():
    form = RegisterForm()
    return render_template('register.html', form=form)
