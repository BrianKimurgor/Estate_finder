from flask import render_template
from estate_finder import app
from estate_finder.models import Location, Property, PropertyType, PropertAgent, Testimonials


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

@app.route('/testimonial')
def testimonial():
    return render_template('testimonial.html')

@app.route('/404')
def not_found():
    return render_template('404.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')