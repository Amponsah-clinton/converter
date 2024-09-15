from django.shortcuts import render
from django.http import HttpResponse
from PIL import Image
from .forms import ImageUploadForm, ResizeImageForm, ReduceSizeForm
import os

# Image format conversion
def convert_image(request):
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            image = Image.open(request.FILES['image'])
            format = form.cleaned_data['format']
            response = HttpResponse(content_type=f'image/{format.lower()}')
            response['Content-Disposition'] = f'attachment; filename=converted_image.{format.lower()}'
            image.save(response, format=format)
            return response
    else:
        form = ImageUploadForm()
    return render(request, 'convert_image.html', {'form': form})

# Image size reduction
def reduce_image_size(request):
    if request.method == 'POST':
        form = ReduceSizeForm(request.POST, request.FILES)
        if form.is_valid():
            image = Image.open(request.FILES['image'])
            quality = form.cleaned_data['quality']
            response = HttpResponse(content_type='image/jpeg')
            response['Content-Disposition'] = 'attachment; filename=reduced_image.jpeg'
            image.save(response, 'JPEG', quality=quality)
            return response
    else:
        form = ReduceSizeForm()
    return render(request, 'reduce_image_size.html', {'form': form})


def home(request):
    return render(request, 'home.html')


# Image resize
def resize_image(request):
    if request.method == 'POST':
        form = ResizeImageForm(request.POST, request.FILES)
        if form.is_valid():
            image = Image.open(request.FILES['image'])
            width = form.cleaned_data['width']
            height = form.cleaned_data['height']
            resized_image = image.resize((width, height))
            response = HttpResponse(content_type='image/jpeg')
            response['Content-Disposition'] = 'attachment; filename=resized_image.jpeg'
            resized_image.save(response, 'JPEG')
            return response
    else:
        form = ResizeImageForm()
    return render(request, 'resize_image.html', {'form': form})
