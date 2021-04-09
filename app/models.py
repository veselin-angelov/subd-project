from app.extensions import db


class Item(db.Model):
    __tablename__ = "items"

    id = db.Column(db.Integer, primary_key=True)
    uuid = db.Column(db.String(10), unique=True, nullable=False)
    name = db.Column(db.String(50), unique=True, nullable=False)
    material = db.Column(db.String(50))
    three_d_file = db.Column(db.String(50))
    sub_group_id = db.Column(db.Integer, db.ForeignKey('sub_groups.id'), nullable=False)
    sub_group = db.relationship('SubGroup')

    def __repr__(self):
        return self.name


class Group(db.Model):
    __tablename__ = "groups"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)

    def __repr__(self):
        return self.name


class SubGroup(db.Model):
    __tablename__ = "sub_groups"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)
    group_id = db.Column(db.Integer, db.ForeignKey('groups.id'), nullable=False)
    group = db.relationship('Group', backref='subgroups')

    def __repr__(self):
        return self.name


class Change(db.Model):
    __tablename__ = "changes"

    id = db.Column(db.Integer, primary_key=True)
    change = db.Column(db.String(50), nullable=False)
    description = db.Column(db.Text, nullable=False)
    person = db.Column(db.String(250), nullable=False)
    date = db.Column(db.Date, nullable=False)
    item_id = db.Column(db.Integer, db.ForeignKey('items.id'), nullable=False)
    item = db.relationship('Item', backref='changes')

    def __repr__(self):
        return f'Change {self.change}, ID: {self.id}'


class BluePrint(db.Model):
    __tablename__ = "blueprints"

    id = db.Column(db.Integer, primary_key=True)
    number = db.Column(db.String(50), unique=True, nullable=False)
    format = db.Column(db.String(2), nullable=False)
    file = db.Column(db.String(50), unique=True, nullable=False)
    created_by = db.Column(db.String(250), nullable=False)
    created_on = db.Column(db.Date, nullable=False)
    checked_by = db.Column(db.String(250), nullable=False)
    checked_on = db.Column(db.Date, nullable=False)
    technology_by = db.Column(db.String(250), nullable=False)
    technology_on = db.Column(db.Date, nullable=False)
    norm_control_by = db.Column(db.String(250), nullable=False)
    norm_control_on = db.Column(db.Date, nullable=False)
    accepted_by = db.Column(db.String(250), nullable=False)
    accepted_on = db.Column(db.Date, nullable=False)
    item_id = db.Column(db.Integer, db.ForeignKey('items.id'), nullable=False)
    item = db.relationship('Item', backref='blueprints')

    def __repr__(self):
        return f'Blueprint: {self.number}'
