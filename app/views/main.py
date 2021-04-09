from flask import Blueprint, redirect, url_for, render_template, request
from app.models import Item, Group, SubGroup, BluePrint, Change


main = Blueprint('main', __name__)


@main.route('/')
def index():
    return 'hello'


@main.route('/search', methods=['GET', 'POST'])
def search():
    if request.method == 'GET':
        items = []
        pass

    if request.method == 'POST':
        criteria = request.form.get('criteria')

        if criteria == 'group':
            group = request.form.get('group')
            subgroups = Group.query.get(group).subgroups
            subgroups_ids = [subgroup.id for subgroup in subgroups]
            items = Item.query.filter(Item.sub_group_id.in_(subgroups_ids)).all()

        elif criteria == 'subgroup':
            subgroup = request.form.get('subgroup')
            items = Item.query.filter(Item.sub_group_id == subgroup).all()

        else:
            search_query = request.form.get('search')
            if search_query == '':
                return redirect(url_for('main.search'))

            if criteria == 'uuid':
                items = Item.query.filter(Item.uuid.like(f'%{search_query}%')).all()

            elif criteria == 'name':
                items = Item.query.filter(Item.name.like(f'%{search_query}%')).all()

            elif criteria == 'bp_number':
                blueprints = BluePrint.query.filter(BluePrint.number.like(f'%{search_query}%')).all()
                items = [blueprint.item for blueprint in blueprints]

            elif criteria == 'creator':
                blueprints = BluePrint.query.filter(BluePrint.created_by.like(f'%{search_query}%')).all()
                items = [blueprint.item for blueprint in blueprints]

    groups = Group.query.all()
    subgroups = SubGroup.query.all()

    return render_template('search.html', groups=groups, subgroups=subgroups, items=items)


@main.route('/items/<int:item_id>')
def item(item_id):
    item = Item.query.get(item_id)
    blueprints = BluePrint.query.filter(BluePrint.item_id == item_id).all()
    changes = Change.query.filter(Change.item_id == item_id).all()

    return render_template('item.html', item=item, blueprints=blueprints, changes=changes)


if __name__ == '__main__':
    main.app.run()
