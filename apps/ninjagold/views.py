from django.shortcuts import render, HttpResponse, redirect
import random
import datetime

def index(request):
    if not 'gold' in request.session:
        request.session['gold']=0
    if not 'activity' in request.session:
        request.session['activity']=""
    if not "activitylog" in request.session:
        request.session['activitylog']=""
    print "Get POST Info"
    print request.session['gold']
    return render(request, 'ninjagold/index.html')

def process_money(request, building):
    now = datetime.datetime.now()
    timestamp = datetime.datetime.strftime(now, '%Y/%m/%d %I:%M %p')
    if request.POST['building']=='farm':
        gold_earned = random.randrange(10,21)
        request.session['activity']  = "<p>Earned " + str(gold_earned) + " golds from the farm! " + "("+str(timestamp)+")</p>"
        print gold_earned
        request.session['gold'] += gold_earned

    elif request.POST['building']=='cave':
        gold_earned = int(random.randrange(5,11))
        request.session['activity'] = "<p>Earned " + str(gold_earned) + " golds from the farm! " + "("+str(timestamp)+")</p>"
        print gold_earned
        request.session['gold'] += gold_earned

    elif request.POST['building']=='house':
        gold_earned = int(random.randrange(2,6))
        request.session['activity'] = "<p>Earned " + str(gold_earned) + " golds from the farm! " +"("+str(timestamp)+")</p>"
        print gold_earned
        request.session['gold'] += gold_earned

    elif request.session['building']=='casino':
        gold_earned = int(random.randrange(-50,51))
        request.session['activity'] = "<p>Earned " + str(gold_earned) + " golds from the farm! " +"("+str(timestamp)+")</p>"
        print gold_earned
        request.session['gold'] += gold_earned

    request.session['activitylog'] = request.session['activity'] + request.session['activitylog']
    return render(request, 'ninjagold/index.html')

def reset(request):
    for key in request.session.keys():
        request.session.pop(key, None)
    return redirect('/')
