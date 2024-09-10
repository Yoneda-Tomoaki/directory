from django import forms
from .models import Members
from django.utils.timezone import now

class MemberForm(forms.ModelForm):
    training_choices = [('','選択してください')] + list(Members.training_choices)
    training_fees = [('','選択してください')] + list(Members.training_fees)
    progress_choices = [('','選択してください')] + list(Members.progress_choices)
    
    
    class Meta:
        model = Members
        fields = ['name', 'input_day', 'enter_day', 'exit_day', 'training', 'participation_cost_submit_or_not']
        
    name = forms.CharField(
        label="名前",
        widget=forms.TextInput(attrs={"class": "form-control"})
    )
        
    input_day = forms.DateField(
        label='記入日',
        widget=forms.TextInput(attrs={"class": "form-control", "type": "date"}),
        initial=now
    )
    
    enter_day = forms.DateField(
        label="入所日",
        widget=forms.TextInput(attrs={"class": "form-control", "type": "date"})
    )
    
    exit_day = forms.DateField(
        label="退所日",
        widget=forms.TextInput(attrs={"class": "form-control", "type": "date"})
    )
    
    training = forms.ChoiceField(
        label = "修練区分",
        choices = training_choices,
        widget = forms.Select(attrs={"class" : "form-control"})
        )
    
    participation_cost_submit_or_not = forms.ChoiceField(
        label = "参加費納付",
        choices = training_fees,
        widget = forms.Select(attrs={"class" : "form-control"}),
    )
    
    progress_state = forms.ChoiceField(
    label="進捗状態",
    choices=progress_choices,
    widget=forms.Select(attrs={"class": "form-control"}),
    required=True  # Nullが許されないため必須に設定
)
