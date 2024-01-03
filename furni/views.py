from django.shortcuts import render
from django.views.generic import TemplateView
from furni.forms import ContactForm, CheckoutForm
from .models import Home
from django.shortcuts import redirect
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.


def index(request):
    return render(request, 'index.html')


def thanks(request):
    return render(request, 'thankyou.html')


def checkout(request):
    return render(request, 'checkout.html')


def about(request):
    return render(request, 'about.html')


def shop(request):
    return render(request, 'shop.html')


def services(request):
    return render(request, 'services.html')


def blog(request):
    return render(request, 'blog.html')


def cart(request):
    return render(request, 'cart.html')


class IndexView(TemplateView):
    template_name = 'contact.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        obj = Home.objects.filter(is_visible=True)
        context['home'] = obj
        context['contact_form'] = ContactForm()
        return context

    def post(self, request, *args, **kwargs):
        contact_form = ContactForm(request.POST)
        if contact_form.is_valid():
            contact_form.save()
            messages.success(request, 'Ваше повідомлення успішно наділсано!')
            return redirect('main:index')
        context = super().get_context_data(**kwargs)
        context['contact_form'] = ContactForm()
        messages.error(request, "Помилки!")
        return render(request, 'contact.html', context)


class ReserveView(TemplateView):
    template_name = 'checkout.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['checkout_form'] = CheckoutForm()
        return context

    def post(self, request, *args, **kwargs):
        checkout_form = CheckoutForm(request.POST)

        if checkout_form.is_valid():
            checkout_form.save()
            messages.success(request, 'Done!')
            return redirect('main:successful_order')
        context = super().get_context_data(**kwargs)
        context['checkout_form'] = CheckoutForm()
        messages.error(request, "Error")
        return render(request, 'index.html', context)
