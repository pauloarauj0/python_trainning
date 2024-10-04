from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Restaurant, Client, Reservation

def index(request):

    restaurants = Restaurant.objects.all()
    client = Client.objects.filter(client_name=request.user.username).first()
    reservations = Reservation.objects.filter(client=client)


    if request.method == 'POST':
        reserve_restaurant(request)
    return render(request, 'index.html', {'restaurants': restaurants, 'reservations': reservations})


def reserve_restaurant(request):

    client_name = request.user.username
    restaurant_id = request.POST['restaurant']
    reservation_date = request.POST['reservation_date']
    number_of_people = int(request.POST['number_of_people'])

    client, created = Client.objects.get_or_create(client_name=client_name)
    restaurant = Restaurant.objects.get(id=restaurant_id)

    tables_needed = number_of_people // 4
    
    if number_of_people % 4 > 0:
        tables_needed +=1
    
    capacity_reserved = tables_needed * 4



    if restaurant.restaurant_current_capacity >= number_of_people:
        Reservation.objects.create(
                client = client,
                restaurant = restaurant,
                reservation_date = reservation_date,
                number_of_people = number_of_people,
                canceled = False,
                ended = False
            )
        
        restaurant.restaurant_current_capacity -= capacity_reserved
        restaurant.save()
    
    else:
        messages.error(request, 'Not enough tables available for the requested number of people.')

def remove_restaurant(request):
    if request.method == 'POST':
        restaurant_id = request.POST.get('restaurant_id')
        restaurant = Restaurant.objects.filter(id=restaurant_id).first()
        restaurant.delete()
        return redirect('/')

def register_restaurant(request):
    if request.method == 'POST':
        restaurant_name = request.POST['restaurant_name']  
        restaurant_max_capacity = request.POST['restaurant_max_capacity']
        restaurant_current_capacity = restaurant_max_capacity

        Restaurant.objects.create(
            restaurant_name = restaurant_name,
            restaurant_max_capacity = restaurant_max_capacity,
            restaurant_current_capacity = restaurant_current_capacity
        )
        return render(request,'restaurant_creation_success.html')

    return render(request, 'restaurant_register.html')




def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('/')  
        else:
            messages.error(request, 'Invalid credentials')

    return render(request, 'login.html')  


def user_register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        is_staff = request.POST.get('is_staff')  
        if password != confirm_password:
            messages.error(request, "Passwords do not match.")
        else:
            try:
                user = User.objects.create_user(username=username, password=password)

                if is_staff:
                    user.is_staff = True
                    user.save()

                messages.success(request, "Registration successful! You can log in now.")
                return redirect('/') 
            except Exception as e:
                messages.error(request, f"Error: {e}")

    return render(request, 'register.html')


def user_logout(request):
    logout(request)
    return redirect("/")

def checkout_reservation(request):
    if request.method == 'POST':
        reservation_id = request.POST.get('reservation_id')
        reservation = Reservation.objects.filter(id=reservation_id).first()
        
        restaurant = reservation.restaurant

        tables_needed = reservation.number_of_people // 4
    
        if reservation.number_of_people % 4 > 0:
            tables_needed +=1
        
        capacity_reserved = tables_needed * 4

        reservation.canceled = True
        reservation.ended = True
        reservation.save()

        restaurant.restaurant_current_capacity += capacity_reserved
        restaurant.save()


        #reservation.delete()
        return redirect("/")
    else:
        return redirect("/")
    

def restaurant_pov(request):
    reservations = Reservation.objects.all()
    restaurants = Restaurant.objects.all()

    return render(request, 'restaurant_pov.html', {'reservations': reservations, 'restaurants':restaurants})
