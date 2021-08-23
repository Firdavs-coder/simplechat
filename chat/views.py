from django.shortcuts import render, redirect
from chat.models import Room, Message
from django.http import HttpResponse, JsonResponse
from django.contrib.auth import authenticate, login, logout
# Create your views here.
def home(request):
    return render(request, 'home.html')
def test(request):
    return render(request, 'test.html')
def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username2') # username input value sini oladi
        password = request.POST.get('password2') # password input value sini oladi
        user = authenticate(request, username = username, password = password) # olingan value uzgaruvchilarini yana boshqa uzgaruvchilarga tenglashtiramiz va shularni authenkatsiya qilamiz
        if user is not None: # user to'g'rimi
            login(request,user) # userni login qil
            # lol = Profile.objects.filter(user=request.user).exists()
            # if lol==False:
            #     obj = Profile.objects.create(user=request.user,country=request.ipinfo.country)
            return redirect('/',)
        else:
            messages.info(request, 'Username yoki parol noto\'g\'ri kiritildi.')
    return render(request,'login.html')


    
# def room(request, room):
    
#     username = request.GET.get('username')
#     room_details = Room.objects.get(name=room)
#     return render(request, 'room.html', {
#         'username': username,
#         'room': room,
#         'room_details': room_details
#     })

# def checkview(request):
#     room = request.POST['room_name']
#     username = request.POST['username']

#     if Room.objects.filter(name=room).exists():
#         return redirect('/'+room+'/?username='+username)
#     else:
#         new_room = Room.objects.create(name=room)
#         new_room.save()
#         return redirect('/'+room+'/?username='+username)

def send(request):
    message = request.POST['message']
    username = request.POST['username']
    room_id = request.POST['room_id']

    new_message = Message.objects.create(value=message, user=username, room=room_id)
    new_message.save()
    return HttpResponse('Message sent successfully')

def getMessages(request):
    # room_details = Room.objects.get(name=room)

    messages = Message.objects.all()
    return JsonResponse({"messages":list(messages.values())})