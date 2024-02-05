from flask import render_template, url_for, redirect, flash
from estate_finder import app, db, bcrypt
from flask_login import login_user, logout_user, current_user, login_required
from estate_finder.models import Location, Property, PropertyType, User
from estate_finder.form import PropertyForm, LoginForm, RegistrationForm



@app.route('/')
@app.route('/home')
def home():
    locations = Location.query.all()
    prop_type = PropertyType.query.all()
    properties = Property.query.all()
    return render_template('home.html', locations=locations,  prop_type=prop_type,
                           properties=properties)


@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/property-list')
def property_list():
    properties = Property.query.all()
    return render_template('property-list.html', properties=properties)


@app.route('/property-type')
def property_type():
    prop_type = PropertyType.query.all()
    return render_template('property-type.html', prop_type=prop_type)


@app.route('/property-agent')
def property_agent():
    return render_template('property-agent.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = (bcrypt.generate_password_hash
                           (form.password.data)
                           .decode('utf-8'))
        user = User(username=form.username.data,
                    email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash('Account created successfully!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password,
                                               form.password.data):
            login_user(user, remember=form.remember.data)
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful, Please check email and password', 'danger')
    return render_template('login.html', title='Login', form=form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('home'))


@app.route('/add_property', methods=['GET', 'POST'])
def add_property():
    form = PropertyForm()
    return render_template('add_property.html', form=form)


@app.route('/testimonial')
def testimonial():
    return render_template('testimonial.html')

@app.route('/404')
def not_found():
    return render_template('404.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')
