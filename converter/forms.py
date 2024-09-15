from django import forms

class ImageUploadForm(forms.Form):
    image = forms.ImageField()
    format_choices = [
        ('JPEG', 'JPEG'),
        ('PNG', 'PNG'),
        ('WEBP', 'WEBP'),
    ]
    format = forms.ChoiceField(choices=format_choices)
    reduce_size = forms.BooleanField(required=False, label="Reduce file size?")
