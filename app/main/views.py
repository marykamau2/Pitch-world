from flask import render_template,request, redirect, url_for,abort
from . import main
from ..models import Pitch, User, Comment
from .. import db
from flask_login import login_required,current_user
from .forms import UpdateProfile, PitchForm, CommentsForm

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/user/<uname>')
def profile(uname):
    user=User.query.filter_by(username=uname).first()

    if user is None:
        abort(404)
    return render_template('profile/profile.html',user=user)

@main.route('/user/<uname>/update',methods = ['GET','POST'])
@login_required
def update_profile(uname):
    user = User.query.filter_by(username = uname).first()
    if user is None:
        abort(404)

    form = UpdateProfile()

    if form.validate_on_submit():
        user.bio = form.bio.data

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('.profile',uname=user.username))

    return render_template('profile/update.html',form =form)

@main.route('/newpitch', methods = ['POST', 'GET'])
@login_required
def new_pitch():
    form = PitchForm()
    
    if form.validate_on_submit():
        pitch_title = form.pitch_title.data
        category = form.category.data
        pitch_idea = form.pitch_idea.data
        new_pitch = Pitch(pitch_title=pitch_title,category=category,pitch_idea=pitch_idea,user=current_user)

        new_pitch.save_pitch()
        db.session.add(new_pitch)
        db.session.commit()

        return redirect(url_for('main.single_pitch' ))
    else:
        all_pitches = Pitch.query.order_by(Pitch.posted).all()

  
    return render_template('newpitch.html',pitches=all_pitches, pitch_form=form)

@main.route('/pitches', methods=['POST','GET']) 
@login_required
def single_pitch():
    """get single  pitch"""
   
    commentform= CommentsForm()
    if commentform.validate_on_submit():
            new_comment= commentform.comment.data
            user_id = current_user._get_current_object().id
            # pitch_id = current_user._get_current_object().id
            #pitch_id=Pitches.query.get(Pitches.id)
            new_comment= Comment(comment=new_comment,user_id=user_id)
            new_comment.save_comment()
            db.session.add(new_comment)
            db.session.commit()
            return redirect(url_for('main.single_pitch'))
    else:

            all_pitches = Pitch.query.order_by(Pitch.posted).all()
            comments=Comment.query.order_by(Comment.comment).all()
        
    
    return render_template('pitches.html', pitches=all_pitches, comments=comments, commentform=commentform)
