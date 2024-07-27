#POST: To create something new
# PATCH:Update something
# DELETE
#POST:Create something
from flask import request,jsonify
from config import app,db
from models import Contact

@app.route('/contacts',methods=['GET'])
def get_contacts():
    contacts=Contact.query.all()
    json_contacts=list(map(lambda x:x.to_json(),contacts))
    return jsonify({'contacts':json_contacts})

@app.route('/create_contact', methods=['POST'])
def create_contact():
    data = request.get_json()
    first_name = data.get('firstName')
    last_name = data.get('lastName')
    email = data.get('email')

    if not first_name or not last_name or not email:
        return jsonify({'message': 'You must enter first name, last name, and email'}), 400

    # E-posta adresinin mevcut olup olmadığını kontrol et
    existing_contact = Contact.query.filter_by(email=email).first()
    if existing_contact:
        return jsonify({'message': 'A contact with this email already exists'}), 400

    new_contact = Contact(first_name=first_name, last_name=last_name, email=email)
    try:
        db.session.add(new_contact)
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        return jsonify({'message': str(e)}), 400

    return jsonify({'message': 'Contact created!'}), 201

@app.route('/update_contact/<int:user_id>', methods=['POST'])
def update_contact(user_id):
    contact = Contact.query.get(user_id)
    if not contact:
        return jsonify({'message': 'user not found'}), 404
    data = request.json
    contact.first_name = data.get('firstName', contact.first_name)
    contact.last_name = data.get('lastName', contact.last_name)
    contact.email = data.get('email', contact.email)

    db.session.commit()

    return jsonify({'message': 'User updated'}), 200


@app.route('/delete_contact/<int:user_id>', methods=['DELETE'])
def delete_contact(user_id):
    contact = Contact.query.get(user_id)
    
    if not contact:
        return jsonify({'message': 'User not found'}), 404
    
    db.session.delete(contact)
    db.session.commit()

    return jsonify({'message': 'User deleted!'}), 200


if __name__=='__main__':
    with app.app_context():
        db.create_all()

    app.run(debug=True)