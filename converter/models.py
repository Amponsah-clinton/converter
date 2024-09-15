from django import forms

class ImageUploadForm(forms.Form):
    image = forms.ImageField()
    format = forms.ChoiceField(choices=[
        ('JPEG', 'JPEG'),
        ('PNG', 'PNG'),
        ('TIFF', 'TIFF'),
        ('BMP', 'BMP'),
        ('WEBP', 'WEBP'),
    ])  # For format conversion

class ResizeImageForm(forms.Form):
    image = forms.ImageField()
    width = forms.IntegerField()
    height = forms.IntegerField()

class ReduceSizeForm(forms.Form):
    image = forms.ImageField()
    quality = forms.IntegerField(min_value=1, max_value=100)  # For quality reduction
