import csv
import io

from app.db import CONNECTION as db
from app.auth import requires_auth

from flask import Flask, render_template, request, make_response
app = Flask(__name__)

def getValue(data, key):
    return list(filter(lambda d: d['name'] == key, data))[0]['value']

def getBusRiders(query={}):
    return db.users.find({
        'applied': True,
        'accepted': True,
        'attending': True,
        'confirmationBranch': 'Bus',
        **query
    })

def mapUser(user):
    return {
        'confirmationDate': user['confirmationSubmitTime'],
        'name': user['name'],
        'email': user['email'],
        'school': getValue(user['applicationData'], 'school')
    }

@app.route('/')
@requires_auth
def dashboard():
    buses = {}
    for user in getBusRiders():
        bus = getValue(user['confirmationData'], 'bus-selection')
        if bus not in buses:
            buses[bus] = []
        buses[bus].append(mapUser(user))
    for riders in buses.values():
        riders.sort(key=lambda r: r['confirmationDate'])
    return render_template('dashboard.html', buses=list(buses.items()))

@app.route('/export', methods=['POST'])
@requires_auth
def exportBus():
    bus = str(request.form['bus'])
    riders = [mapUser(rider) for rider in getBusRiders({
        'confirmationData': {
            '$elemMatch': {
                'name': 'bus-selection',
                'value': bus
            }
        }
    })]
    si = io.StringIO()
    cw = csv.DictWriter(si, fieldnames=['confirmationDate', 'name', 'email', 'school'])
    cw.writeheader()
    cw.writerows(riders)
    output = make_response(si.getvalue())
    output.headers['Content-Disposition'] = 'attachment; filename=bus.csv'
    output.headers['Content-type'] = 'text/csv'
    return output
