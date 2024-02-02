from estate_finder import db
from estate_finder.models import Location, PropertyType, Property, PropertAgent, Testimonials


# method to add location
def add_location(name):
    location = Location.query.filter_by(name=name).first()
    if not location:
        location = Location(name=name)
        db.session.add(location)

# method to add property type
def add_property_type(name):
    property_type = PropertyType.query.filter_by(name=name).first()
    if not property_type:
        property_type = PropertyType(name=name)
        db.session.add(property_type)

# Method to add property
def add_property(property_type_name, location_name, status, size_sqft, bedrooms, bathrooms, price, property_img):
    property_type = PropertyType.query.filter_by(name=property_type_name).first()
    location = Location.query.filter_by(name=location_name).first()

    # checking our db
    if property_type and location:
        property_obj = Property.query.filter_by(
            property_type=property_type,
            location=location,
            status=status,
            size_sqft=size_sqft,
            bedrooms=bedrooms,
            bathrooms=bathrooms,
            price=price,
            property_img=property_img
        ).first()

        if not property_obj:
            property_obj = Property(
                property_type=property_type,
                location=location,
                status=status,
                size_sqft=size_sqft,
                bedrooms=bedrooms,
                bathrooms=bathrooms,
                price=price,
                property_img=property_img
            )
            db.session.add(property_obj)
            
def add_property_agent(name, contact_info, agent_img):
    property_agent = PropertAgent.query.filter_by(
            name=name,
            contact_info=contact_info,
            agent_img=agent_img
        ).first()
    if not property_agent:
        property_agent = PropertAgent(
            name=name,
            contact_info=contact_info,
            agent_img=agent_img
        )
        db.session.add(property_agent)
            
def add_testimonial(client_name, testimonial_text, client_img, property_obj):
    client_testimonials = Testimonials.query.filter_by(
        client_name=client_name,
        testimonial_text=testimonial_text,
        client_img=client_img,
        property=property_obj
    ).first()
    if not client_testimonials:
        testimonials = Testimonials(
            client_name=client_name,
            testimonial_text=testimonial_text,
            client_img=client_img,
            property=property_obj
        )
        db.session.add(testimonials)
