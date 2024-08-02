from django.shortcuts import render,get_object_or_404,redirect
from user.forms import RegisterUserForm
from .models import Ticket,Order
from django.contrib import messages
from django.core.paginator import Paginator
from .forms import TicketUpdateform
from django.db import transaction
from django.contrib.auth.decorators import user_passes_test


from django.contrib.auth import get_user_model

from .filters import TicketFilter
from django.db.models import Q

User = get_user_model()


def index_views(request):
    tickets = Ticket.objects.filter(is_active=True)[::-1][:2]

    register_views = RegisterUserForm()

    return render(
        request=request,
        template_name='product/index.html',
        context={
            'tickets': tickets,
            'register_views': register_views
        }
    )


def event_detail(request, pk):
    tickets = get_object_or_404(Ticket, id=pk)

    register_views = RegisterUserForm()

    if not request.user.is_authenticated:
        messages.error(request, 'Для покупки билета, пожалуйста зарегистрируйтесь.')


    if request.method == 'POST':
        if 'delete' in request.POST:
            with transaction.atomic():
                Order.objects.filter(ticket=tickets).delete()
                tickets.delete()
                messages.success(request, 'Успешно удалено')
            return redirect('index')
        else:
            form = TicketUpdateform(request.POST,request.FILES,instance=tickets)
            if form.is_valid():
                form.save()
                messages.success(request,'Успешно изменено')

            else:
                quantity = request.POST.get('quantity')
                event_total = tickets.price * int(quantity)
                current_user = User.objects.get(id=request.user.id)

                if event_total <= current_user.wallet:
                    order = Order(
                        user=request.user,
                        ticket=tickets,
                        quantity=quantity,
                        total_price=event_total
                    )
                    order.save()

                    current_user.wallet -= event_total
                    current_user.save()

                    messages.success(request, 'Вы успешно купили билет')
                else:
                    messages.error(request, 'У вас недостаточно средств')

    form = TicketUpdateform(instance=tickets)

    return render(
        request=request,
        template_name='product/event-detail.html',
        context={
            'tickets': tickets,
            'register_views': register_views,
            'form': form

        }
    )


def profile_views(request):
    tickets = Ticket.objects.filter(is_active=True)[::-1][:2]
    user = get_object_or_404(User, id=request.user.id)

    return render(
        request=request,
        template_name='product/profile.html',
        context={
            'tickets':tickets,
            'user':user

        }
    )

def event_listing(request):
    event_filter = TicketFilter(request.GET, queryset=Ticket.objects.filter(is_active=True))
    listings = event_filter.qs

    register_views = RegisterUserForm()

    if 'search' in request.GET:
        search_text = request.GET['search']
        listings = listings.filter(Q(title__iregex=search_text) | Q(description__iregex=search_text))

    paginator = Paginator(listings,2)
    page_event = request.GET.get('page')
    page_obj = paginator.get_page(page_event)

    return render(
        request=request,
        template_name='product/event-listing.html',
        context={
            'listings': listings,
            'filter': event_filter,
            'page_obj': page_obj,
            'register_views': register_views
        }
    )


@user_passes_test(lambda u: u.is_authenticated and (u.is_admin or u.status == 2), login_url='index')
def event_create_views(request):
    # if not request.user.is_authenticated:
    #     messages.error(request,'Войдите в систему')
    #     return redirect('index')
    #
    # elif request.user.status != 2 and request.user.is_admin == False:
    #     messages.error(request,'У вас нет доступа к этой странице')
    #     return redirect('index')

    if request.method == "POST":
        title = request.POST['title']
        description = request.POST['description']
        price = request.POST['price']
        location_event = request.POST['location_event']
        image = request.FILES['image']
        event_date = request.POST['event_date']
        date_duration = request.POST['date_duration']
        quantity = request.POST['quantity']

        events = Ticket(
            title = title,
            description = description,
            price = price,
            location_event = location_event,
            image = image,
            event_date = event_date,
            date_duration = date_duration,
            quantity = quantity
        )
        events.save()
        messages.success(request, 'Успешно создана')

        return redirect('index')


    return render(
        request=request,
        template_name='product/event_create.html',
    )
