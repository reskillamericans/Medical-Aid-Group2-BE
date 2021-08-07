from django.shortcuts import render
from django.http import HttpResponse

from .helper import multiple_forms, newsletter_form
# Create your views here.


def index(request):
    """ multiple_forms checks if the request  was post, and then depending by the sumit button's
    name, it saves the contents fo the submitted form's to the proper model.
    ex. contact-us button turns ContactUsForm | newsletter button runs NewsletterForm. """
    multiple_forms(request)

    return render(request, 'aidApp/index.html')


def about_us(request):
    """ newsletter_form checks if the request was post, and if it is saves the contents
    of the submitted form to the newletter model. """
    newsletter_form(request)

    return render(request, 'aidApp/about-us.html')


def faq(request):

    # It is important that in the html all fields in the newletter form be given the attribute : required
    # as well that between the <body> and next tag be:
    """
        {% if messages %}
        {% for message in messages %}
        <div class="alert alert-{{ message.tags }}" role="alert">{{ message }}</div>
        {% endfor %}
        {% endif %}
    """
    # same for in the css between the body {} and next tag be"

    """
        .alert {
        width: 100%;
        padding: 12px 16px;
        border-width: 1px;
        font-size: 16px;
    }
    
    .alert.alert-success {
        background-color: rgba(227, 253, 235, 1);
        color: rgba(60, 118, 61, 1);
    }

    .alert.alert-info {
        background-color: rgba(217, 237, 247, 1);
        color: rgba(49, 112, 143, 1);
        border-color: rgba(126, 182, 193, 1);
    }

    .alert.alert-warning {
        background-color: rgba(252, 248, 227, 1);
        border-color: rgba(177, 161, 129, 1);
        color: rgba(138, 109, 59, 1);
    }
    """

    """ newsletter_form checks if the request was post, and if it is saves the contents
    of the submitted form to the newletter model. """
    newsletter_form(request)

    return HttpResponse('<h1>FAQ Page</h1>')


def login(request):
    return HttpResponse('<h1>Login Page</h1>')


def sign_up(request):
    return HttpResponse('<h1>Sign Up Page</h1>')
