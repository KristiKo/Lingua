from django import forms

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


class FeedbackForm(forms.Form):
    
    FRIENDLINESS = (
        (" ", " "),
        ("Very satisfied", "Very satisfied"),
        ("Satisfied", "Satisfied"),
        ("Neutral", "Neutral"),
        ("Unsatisfied", "Unsatisfied"),
        ("Very unsatisfied", "Very unsatisfied"),
    )
    KNOWLEDGE = (
        (" ", " "),
        ("Very satisfied", "Very satisfied"),
        ("Satisfied", "Satisfied"),
        ("Neutral", "Neutral"),
        ("Unsatisfied", "Unsatisfied"),
        ("Very unsatisfied", "Very unsatisfied"),

    )
    QUICKNESS = (
        (" ", " "),
        ("Very satisfied", "Very satisfied"),
        ("Satisfied", "Satisfied"),
        ("Neutral", "Neutral"),
        ("Unsatisfied", "Unsatisfied"),
        ("Very unsatisfied", "Very unsatisfied"),
    )
    YESNOMAYBE = (
        (" ", " "),
        ("Yes", "Yes"),
        ("No", "No"),
        ("Maybe", "Maybe"),
    )

    Friendliness = forms.ChoiceField(choices=FRIENDLINESS, label="Friendliness")
    Knowledge = forms.ChoiceField(choices=KNOWLEDGE, label="Knowledge")
    Quickness = forms.ChoiceField(choices=QUICKNESS, label="Quickness")
    YesNoMaybe = forms.ChoiceField(choices=YESNOMAYBE, label="Would you suggest Lingua International to a friend?")
    message = forms.CharField(widget=forms.Textarea, required = False, label="How can we improve our service?")

