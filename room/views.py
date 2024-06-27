from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect,get_object_or_404
from .models import Message, Room ,Open_room,JoinRequest
from  django.contrib.auth import login
from django.db.models import Q
from django.db.models import Count
from django.core.mail import send_mail
from django.contrib.auth.models import User

from .forms import InvitationForm, JoinRequestForm
from django.http import HttpResponse
@login_required
def rooms(request):
    rooms = Room.objects.all()
    if request.method=="GET":
        rn = request.GET.get('rname')
        if rn!=None:
            rooms = Room.objects.filter(name__icontains=rn)

    return render(request, 'room/rooms.html', {'rooms': rooms})





@login_required
def enter_room(request):
    
    if request.method == 'POST':
        room_name = request.POST['room_name']

        try:
            room = Room.objects.get(name=room_name)
        except Room.DoesNotExist:
            error_message = 'Invalid room name or password.'
            return redirect(join_room)
        if(request.user==room.owner):
            messages = Message.objects.filter(room=room)[0:25]
        
            return render(request, 'room/room.html',{'room': room, 'messages': messages})
        

        if(request.user in room.members.all()):
            messages = Message.objects.filter(room=room)[0:25]
        
            return render(request, 'room/room.html',{'room': room, 'messages': messages})

        password = request.POST['password']

        if room.password==password:
            room.members.add(request.user)
            messages = Message.objects.filter(room=room)[0:25]
        
            return render(request, 'room/room.html',{'room': room, 'messages': messages})
        return redirect(join_room)
    return redirect(join_room)
@login_required
def create_room(request):
    if request.method == 'POST':
        room_name = request.POST['room_name']
        password = request.POST['password']
        owner= request.user
        newroom = Room(name=room_name, password=password,owner=owner)
        newroom.save()
        
        
        return redirect(rooms)
    return render(request, 'room/create_room.html')
    




@login_required
def search_rooms(request):
    query = request.GET.get('q')
    if query:
        rooms = Room.objects.annotate(match_count=Count('name')).filter(name__icontains=query).order_by('-match_count')
        all_rooms = Room.objects.exclude(name__icontains=query)
    else:
        rooms = Room.objects.none()
        all_rooms = Room.objects.all()

    return render(request, 'room/rooms.html', {'rooms': rooms, 'all_rooms': all_rooms})

   
@login_required
def open_rooms(request):
    open_rooms = Open_room.objects.all()
    
        
            
    if request.method=="GET":
        rn = request.GET.get('open_name')
        if rn!=None:
            open_rooms = Open_room.objects.filter(name__icontains=rn)
    return render(request, 'room/open_rooms.html', {'open_rooms': open_rooms})		

@login_required
def create_open_room(request):
    if request.method == 'POST':
        room_name = request.POST['room_name']
        
        newroom = Open_room(name=room_name,owner = request.user)
        newroom.save()
        
        return redirect(open_rooms)
    return render(request, 'room/create_open_room.html')
    
@login_required
def enter_open_room(request):
    
    if request.method == 'POST':
        room_name = request.POST['room_name']
        

        try:
            open_room = Open_room.objects.get(name=room_name)
        except open_room.DoesNotExist:
            error_message = 'Invalid room name or password.'
            return redirect(open_rooms)

        # Perform actions after successful room entry
        # For example, you could redirect the user to a success page or perform additional logic here.
       
        messages = Message.objects.filter(open_room=open_room)[0:25]
       
        return render(request, 'room/room.html',{'open_room': open_room ,'messages':messages})

    return render(request, 'room/rooms.html',{'open_room': open_room })

@login_required
def my_rooms(request):
    my_rooms = Room.objects.filter(owner=request.user)
    rooms = Room.objects.all()
    user = request.user
    if request.method=="GET":
        mrn = request.GET.get('mrname')
        if mrn!=None:
            my_rooms = Room.objects.filter(name__icontains=mrn)
    return render(request,'room/my_rooms.html',{'my_rooms':my_rooms,'user':user,'rooms':rooms})

@login_required
def invite_users(request):
    if request.method == 'POST':
        form = InvitationForm(request.POST)
        if form.is_valid():
            password = form.cleaned_data['password']
            chat_room = form.cleaned_data['chat_room']
            invitees = form.cleaned_data['invitees']

            recipients = User.objects.filter(id__in=invitees.values_list('id', flat=True))

            subject = f'Invitation to join {chat_room} chat room'
            message = f'Hi,\n\nYou are invited to join the chat room "{chat_room}" with password "{password}".\n\n Please do not share this password with any other users.\n\n Thank You.'

            recipient_emails = recipients.values_list('email', flat=True)
            rooms = Room.objects.filter(owner=request.user)
            
            send_mail(subject, message, 'headmail0607@gmail.com', recipient_emails)

            return redirect(my_rooms)
    else:
        form = InvitationForm()

    return render(request, 'room/invite_users.html', {'form': form})


@login_required
def join_room(request):
    if request.method == 'POST':
        form = JoinRequestForm(request.POST)
        if form.is_valid():
            req_room = form.cleaned_data['req_room']
            password = form.cleaned_data['password']
            room = Room.objects.get(name=req_room)
            # Create a new join request
            join_request = JoinRequest(sender=request.user, room=room)
            join_request.save()

            # Redirect to a success page or show a success message
            
            return HttpResponse('Done')
    else:
        form = JoinRequestForm()   
    rooms = Room.objects.all()
    if request.method=="GET":
        rn = request.GET.get('rname')
        if rn!=None:
            rooms = Room.objects.filter(name__icontains=rn)     
    return render(request,'room/rooms.html',{'rooms':rooms,'form':form})


@login_required
def manage_join_requests(request):
    # Get the join requests for rooms owned by the user
    join_requests = JoinRequest.objects.filter(room__owner=request.user, status='pending')
    
    if request.method == 'POST':
        # Process the accepted or rejected join requests
        for join_request in join_requests:
            stat = request.POST.get(str(join_request.id))
            if stat == 'accept':
                # Accept the join request
                join_request.status = 'accepted'    
                join_request.save()
                # Add the user to the room members
                join_request.room.members.add(join_request.sender)

            elif stat == 'reject':
                # Reject the join request
                join_request.status = 'rejected'
                join_request.save()

        # Redirect to a success page or show a success message
        ##return render(request, 'room/manage_join_requests.html', {'join_requests': join_requests})

    return render(request, 'room/manage_join_requests.html', {'join_requests': join_requests})