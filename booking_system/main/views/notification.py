from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from main.models import Attachment

# Create your views here.
@login_required
def notification(request,attachment_id):
    try:
        attachment = Attachment.objects.get(id=attachment_id)
        if attachment.booking.manager == request.user:
            booking_id = attachment.booking.id
            attachment.delete()
            return redirect(f"/admin/main/booking/{booking_id}")
        else:
            return redirect(".")
    except Attachment.DoesNotExist:
        return redirect(".")
