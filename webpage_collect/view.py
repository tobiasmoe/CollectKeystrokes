#import functools
import json

from flask import (
        Blueprint, g, request, render_template, redirect, url_for
)

from webpage_collect.db import get_db

bp = Blueprint('view', __name__)

@bp.route('/')
def index():
    return redirect(url_for('view.input'))

@bp.route('/input', methods=('GET', 'POST'))
def input():
    if request.method == 'POST':
        req = request.get_json()
        #for x in range(len(req)):

         #   db = get_db()
          #  db.execute(
          #          'INSERT INTO keystrokes (user_id, clocktime, time, altkey, key, keycode)'
          #          ' VALUES (?, ?, ?, ?, ?, ?)',
          #          (req[x]['user_id'], req[x]['clockTime'], req[x]['timestamp'], req[x]['altkey'], req[x]['key'], req[x]['keyCode'])
          #  )
          #  db.commit()
        db = get_db()
        db.execute(
                'INSERT INTO keystrokes (user_id, session_id, type, key, keycode, clocktime, lastkey)'
                ' VALUES (?, ?, ?, ?, ?, ?, ?)',
                (req['user_id'], req['session_id'], req['type'], req['key'], req['keyCode'], req['clockTime'], req['lastkey'])
        )
        db.commit()
    return render_template('input.html')

@bp.route('/textarea', methods=('GET', 'POST'))
def textarea():
    return render_template('textarea.html')

