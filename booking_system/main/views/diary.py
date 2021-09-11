from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from main.models import Booking, Event
from main.forms import DiaryForm
import datetime

# Create your views here.
@login_required
def diary(request):
    if request.user.is_staff:
        bookings = Booking.objects.filter(~Q(status=3))
        data = {}
        if request.method == "POST":
            days = int(request.POST["days"])
            start_date = request.POST["start_date"]
            date = datetime.datetime.strptime(start_date, '%m/%d/%Y')
            date_list = [date + datetime.timedelta(days=x) for x in range(days)]
            for booking in bookings:
                tmp_events = []
                events = Event.objects.filter(Q(booking=booking)&Q(date__gte=date_list[0])&Q(date__lte=date_list[-1]))
                for event in events:
                    if event.hall in data:
                        data[event.hall].append(event)
                    else:
                        data[event.hall] = [event]
        else:
            base = datetime.datetime.today()
            date_list = [base]
            for booking in bookings:
                events = Event.objects.filter(Q(booking=booking)&Q(date=base))
                if events.count()>0:
                    booking.hall = events[0].hall
                    data[booking] = events
        hours = (7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,0,1,2,3,4,5,6)
        return render(
            request,
            "diary.html",
            {
                "data":data,
                "days":date_list,
                "days_range":hours,
                "form":DiaryForm()
            }
            )
    else:
        return redirect("/admin")