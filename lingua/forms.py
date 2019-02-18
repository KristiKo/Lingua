from django import forms
from users.models import Subscriber

class ContactForm(forms.Form):
    DAYS = (
                ("Monday", "Monday"),
                ("Tuesday", "Tuesday"),
                ("Wednesday", "Wednesday"),
                ("Thursday", "Thursday"),
                ("Friday", "Friday"),
                )
    TIMES = (
                ("8:30", "8:30"),
                ("9:00", "9:00"),
                ("9:30", "9:30"),
                ("10:00", "10:00"),
                ("10:30", "10:30"),
                ("11:00", "11:00"),
                ("11:30", "11:30"),
                ("12:00", "12:00"),
                ("12:30", "12:30"),
                ("13:00", "13:00"),
                ("13:30", "13:30"),
                ("14:00", "14:00"),
                ("14:30", "14:30"),
                ("15:00", "15:00"),
                ("15:30", "15:30"),
                ("16:00", "16:00"),
                ("16:30", "16:30"),
                ("17:00", "17:00"),
                ("17:30", "17:30"),
                ("18:00", "18:00"),
                )

    from_email = forms.EmailField(required=True, label="From")
    subject = forms.CharField(required=True, label="Subject")
    phone_number = forms.CharField(required=False, label="Your Phone Number")
    day = forms.ChoiceField(choices=DAYS, label="Day")
    time = forms.ChoiceField(choices=TIMES, label="Time")
    message = forms.CharField(widget=forms.Textarea, label="Your Message")

class SubscriberForm(forms.ModelForm):
    email = forms.EmailField(required=False, label="Email Address",
            widget=forms.TextInput(attrs={'placeholder': 'Email Address'}))

    class Meta:
        model = Subscriber
        fields = ['email']