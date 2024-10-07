from django.http import JsonResponse
from django.shortcuts import render
import firebase_admin
from firebase_admin import db
import threading
import time

event_triggered = False

def poll_firebase():
    global event_triggered
    while True:
        try:
            # Replace 'your-database-path' with the correct Firebase node
            ref = db.reference('events/trigger')
            data = ref.get()

            print(f"Fetched data from Firebase: {data}")

            # Update event_triggered based on Firebase data
            if data == 1:
                event_triggered = True
                print("Event triggered from Firebase!")
                
                # Reset the event in Firebase
                ref.set(0)
            else:
                event_triggered = False
        except Exception as e:
            print(f"Error fetching data from Firebase: {e}")

        time.sleep(20)  # Poll every 5 seconds

def start_firebase_polling():
    thread = threading.Thread(target=poll_firebase)
    thread.daemon = True
    thread.start()

# Event status views for Django
def check_event_status(request):
    global event_triggered
    return JsonResponse({'event_triggered': event_triggered})

def trigger_event(request):
    global event_triggered
    event_triggered = True
    return JsonResponse({'status': 'Event Triggered'})

def reset_event_status(request):
    global event_triggered
    event_triggered = False
    return JsonResponse({'status': 'Event Reset'})

def index(request):
    return render(request, 'index.html', {})

def static_page(request):
    return render(request, 'static_page.html')
