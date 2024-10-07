from django.apps import AppConfig
import firebase_admin
from firebase_admin import credentials

class VideoStreamConfig(AppConfig):
    name = 'main'

    def ready(self):
        # Firebase Initialization
        try:
            # Only initialize if it hasn't been initialized yet
            if not firebase_admin._apps:
                cred = credentials.Certificate('main\security-cam-d48b9-firebase-adminsdk-gb1ho-2883a96bd0.json')
                firebase_admin.initialize_app(cred, {
                    'databaseURL': 'https://security-cam-d48b9-default-rtdb.asia-southeast1.firebasedatabase.app/'
                })
                print("Firebase initialized successfully.")
        except Exception as e:
            print(f"Error initializing Firebase: {e}")

        # Start the Firebase polling
        from .views import start_firebase_polling
        start_firebase_polling()
