from django.shortcuts import render
from django.contrib.auth.decorators import user_passes_test
from apps.models import Order
from django.db.models import Sum

@user_passes_test(lambda u: u.is_authenticated and (u.is_admin or u.status == 2), login_url='index')
def event_crm_list(request):
    events = Order.objects.all().order_by('-id')
    total = events.aggregate(total=Sum('total_price'))['total']

    return render(
        request=request,
        template_name='crm/event_list.html',
        context={
            'events': events,
            'total': total
        }
    )
