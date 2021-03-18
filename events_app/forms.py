from django import forms

from events_app.models import EventUsers, AboutUser, UserGoals


class UserForm(forms.ModelForm):
    class Meta:
        model = EventUsers
        exclude = ('user_id',)
        widgets = {
            'password': forms.PasswordInput()
        }
class AboutForm(forms.ModelForm):
    
    class Meta:
        model = AboutUser
        exclude=["user"]
        widgets = {
            'gender': forms.Select(),
            'status': forms.Select(),
            'occupation': forms.Select()
        }
class GoalForm(forms.ModelForm):
    
    class Meta:
        model = UserGoals
        exclude=["user"]
        widgets = {
            'bio': forms.Textarea()
        }
