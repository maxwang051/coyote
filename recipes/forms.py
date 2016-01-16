from django import forms

class IngredientForm(forms.Form):
    CHOICES = (
        ("eggs", "Eggs"),
        ("milk", "Milk"),
        ("cheese", "Cheese"),
        ("bread", "Bread"),
        ("bacon", "Bacon"),
        ("bagel", "Bagel"),
        
    )

    picked = forms.MultipleChoiceField(choices=CHOICES, widget=forms.CheckboxSelectMultiple())
