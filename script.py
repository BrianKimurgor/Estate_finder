from estate_finder import app, db
from estate_finder.models import Location, PropertyType, Property


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

with app.app_context():
    db.create_all()

    # Add locations
    locations_data = ["Ruiru", "Westlands", "Karen", "Kilimani", "Muthaiga", "Parklands", "Kahawa", "Kasarani", "Utawala"]
    for location_name in locations_data:
        add_location(location_name)

    # Add property types
    property_types_data = ["House", "Apartment"]
    for property_type_name in property_types_data:
        add_property_type(property_type_name)

    # Add properties
    add_property("House", "Ruiru", "For sell", 1500, 2, 1, 1500.0, "/estate_finder/static/img/property-4.jpg")
    add_property("Apartment", "Westlands", "For Rent", 2000, 3, 2, 2000.0, "/estate_finder/static/img/property-5.jpg")

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
