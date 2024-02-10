from estate_finder import app, db
from add_to_db import add_location, add_property, add_property_type, add_property_agent, add_testimonial, update_agent_image, update_testimonial_image
from estate_finder.models import Location, PropertyType, Property, PropertAgent, Testimonials, User


with app.app_context():
    """db.create_all()

    # Add locations
    locations_data = ["Ruiru", "Westlands", "Karen", "Kilimani", "Muthaiga",
                      "Parklands", "Kahawa", "Kasarani", "Utawala"]
    for location_name in locations_data:
        add_location(location_name)

    # Add property types
    property_types_data = ["House", "Apartment", "Home", "Shop", "Villa", "Garage",
                           "Building", "Townhouse", "Office"]
    for property_type_name in property_types_data:
        add_property_type(property_type_name)

    # Add properties
    add_property("House", "Ruiru", "For sell", 1500, 2, 1, 1500.0, "img/property-4.jpg")
    add_property("Apartment", "Westlands", "For Rent", 2000, 3, 2, 2000.0, "img/property-5.jpg")
    add_property("Shop", "Karen", "For sell", 1500, 3, 2, 2500.0, "img/property-1.jpg")
    add_property("Home", "Kilimani", "For Rent", 2000, 4, 2, 4000.0, "img/property-2.jpg")"""

    # Testimonials.query.filter(Testimonials.id >= 5).delete()

    # adding property agent
    """add_property_agent("Brian Kimurgor", "+25475556667", "default.jpg")
    add_property_agent("Jackson Maina", "+2547222333", "default.jpg")
    add_property_agent("Brenda Timina", "+254666554", "default.jpg")
    add_property_agent("Moses Omondi", "+25472424253", "img/team-4.jpg")
    update_agent_image(1, "img/team-1.jpg")
    update_agent_image(2, "img/team-2.jpg")
    update_agent_image(3, "img/team-3.jpg")

    # adding client testimonials
    property_obj = Property.query.filter_by(location_id=1).first()
    add_testimonial("John Doe", "Great property!", "john_doe.jpg", property_obj)
    update_testimonial_image(1, "img/testimonial-1.jpg")
    
    property_obj = Property.query.filter_by(location_id=2).first()
    add_testimonial("Moses Omondi", "Great property and awesome home to be!", "moses.jpg", property_obj)
    update_testimonial_image(2, "img/testimonial-2.jpg")
    
    property_obj = Property.query.filter_by(location_id=2).first()
    add_testimonial("Mirriam Njagi", "I really enjoyed staying", "Mirriam.jpg", property_obj)
    update_testimonial_image(3, "img/testimonial-4.jpg")
    
    property_obj = Property.query.filter_by(location_id=3).first()
    add_testimonial("Esther Auma", "Great property!", "auma.jpg", property_obj)
    update_testimonial_image(4, "img/testimonial-3.jpg")"""


    """Location.query.delete()
    PropertyType.query.delete()
    Property.query.delete()
    PropertAgent.query.delete()
    Testimonials.query.delete()"""

    db.session.commit()

    locations = Location.query.all()
    for location in locations:
        print(location)
    print('\n')

    property_types = PropertyType.query.all()
    for p_type in property_types:
        print(p_type)
    print('\n')

    properties = Property.query.all()
    for prop in properties:
        print(prop)
    print('\n')

    agents = PropertAgent.query.all()
    for agent in agents:
        print(agent)
    print('\n')

    testimonials = Testimonials.query.all()
    for testimonial in testimonials:
        print(testimonial)
    print('\n')
        
    users = User.query.all()
    for user in users:
        print(user)