from .forms import UserCreateForm

def __init__(self, *args, **kwargs):
    
    super(UserCreateForm, self).__init__(*args, **kwargs)
    
    self.fields['password1'].widget = forms.PasswordInput(attrs={
        'placeholder': ("New password"),
        'class': ("form-control form-control-user"),
    })
    
    self.fields['password2'].widget = forms.PasswordInput(attrs={
        'placeholder': ("Confirm password"),
        'class': ("form-control form-control-user"),
    })