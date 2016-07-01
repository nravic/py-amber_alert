from flask import request, flash, render_template, url_for, redirect, abort, Blueprint, g
from aalert import app, db
from flask_login import login_required, logout_user, login_user, current_user
from aalert.forms import *
from aalert.models import *
from sqlalchemy_searchable import search
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView


@app.before_request
def before_request():
    g.search_form = SearchForm()
    
@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, password=form.password.data)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('index'))
    
    return render_template('register.html', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first_or_404()
        if user.is_correct_password(form.password.data):
            login_user(user)
            flash(u'Logged in Successfully.', 'success')
            return redirect(url_for('index'))
        else:
            flash(u'Incorrect username/password combination.', 'error')
            return redirect(url_for('index'))
    return render_template('login.html', form=form)



@app.route('/', methods=['GET'])
def index():
    entries = db.session.query(Info.id, Info.firstname, Info.lastname, Info.age,
                               Info.height,Info.last_loc, Info.missing_since)
    return render_template('disp.html', entries=entries)


@app.route('/search', methods=['GET', 'POST'])
def search():
    if not g.search_form.validate_on_submit():
        flash(u'Incorrect format for search string.', 'error')
        return redirect(url_for('index'))
    return redirect(url_for('search_results', query=g.search_form.query.data)) 
        

@app.route('/search_results/<query>')
def search_results(query):
    results = Info.query.search(query).limit(20).all()
    if results == None:
        flash('No hits. Try a different search string.')
    return render_template('search_results.html', query=query, results=results)

@app.route('/logout')
def logout():
    logout_user()
    flash(u'Logged out successfully.', 'success')
    return redirect(url_for('index'))


#admin views
admin = Admin(app, name='Amber Alert Database', template_mode='bootstrap')
class ProtectedView(ModelView):
    def is_accessible(self):
        return current_user.is_authenticated

    def inaccessible_callback(self, name, **kwargs):
        return redirect(url_for('index'))

admin.add_view(ProtectedView(Info, db.session))
