from estate_finder import app, db
from estate_finder.models import Location, PropertyType


def add_locations():
    locations_data = [
        {"name": "Ruiru"},
        {"name": "Westlands"},
        {"name": "Karen"},
        {"name": "Kilimani"},
        {"name": "Muthaiga"},
        {"name": "Parklands"},
        {"name": "Kahawa"},
        {"name": "Kasarani"},
        {"name": "Utawala"},
        # we will  more locations as needed
    ]

    for location_data in locations_data:
        location = Location(**location_data)
        db.session.add(location)

    db.session.commit()
    
    
with app.app_context():
    db.create_all()
    add_locations()
    
    locations = Location.query.all()
    for location in locations:
        print(location)