from flask import render_template, url_for, redirect
from estate_finder import app, db
from estate_finder.models import Location, Property
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

@app.route('/register')
def register():
    form = RegistrationForm()
    return render_template('register.html', title='Register', form=form)

@app.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html', title='Login', form=form)

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
