from flask import render_template

from org.hasii.pythonflask.fitbit import app

from org.hasii.pythonflask.fitbit.models.FitBitRecord import FitBitRecord


@app.route('/')
@app.route('/index')
def index():
    """"""
    user = {'username': 'Humberto A. Sanchez II'}

    # workouts = [
    #     {
    #         'date':           '2018-03-01',
    #         'steps':          '9,999',
    #         'calories': '2,701'
    #     },
    #     {
    #         'date':           '2018-04-27',
    #         'steps':          '15,000',
    #         'calories': '3,066'
    #     },
    #     {
    #         'date':           '2018-05-05',
    #         'steps':          '25,000',
    #         'calories': '6,666'
    #     }
    # ]

    workouts = FitBitRecord.query.all()
    return render_template('index.html', title='Home', user=user, workouts=workouts)