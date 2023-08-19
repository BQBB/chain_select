from crispy_forms.layout import Submit, Layout, Row, Column, Div
from django import forms
from crispy_forms.helper import FormHelper
from django.urls import reverse

from chain.models import Manufacture, Model, Price


class ProductForm(forms.Form):
    manufacture = forms.ModelChoiceField(queryset=Manufacture.objects.all()[:5], required=False)
    model = forms.ModelChoiceField(queryset=Model.objects.none(), required=False)
    price = forms.ModelChoiceField(queryset=Price.objects.none(), required=False)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['manufacture'].widget.attrs = {'hx-target': '#childs', 'hx-swap': 'outerHTML',
                                                   'hx-get': reverse('chain:get_model_by_manufacture'),
                                                   'hx-select': '#childs',
                                                   'hx-include': 'form select',
                                                   'hx-trigger': 'keyup changed delay:1000ms, search, change'}

        self.fields['model'].widget.attrs = {'hx-target': '#div_id_price', 'hx-swap': 'outerHTML',
                                             'hx-get': reverse('chain:get_price_by_model'),
                                             'hx-select': '#div_id_price',
                                             'hx-include': 'form select',
                                             'hx-trigger': 'keyup changed delay:1000ms, search, change'}

        self.fields['price'].widget.attrs = {'hx-target': '#div_id_price', 'hx-swap': 'outerHTML',
                                             'hx-get': reverse('chain:add_price'),
                                             'hx-select': '#div_id_price',
                                             'hx-include': 'form select',
                                             'hx-trigger': 'keyup changed delay:1000ms, search, change'}

        self.helper = FormHelper()
        self.helper.form_id = 'id'
        self.helper.form_class = 'blueForms'
        self.helper.form_method = 'post'

        self.helper.layout = Layout(
            Row(
                Column('manufacture'),
                Div(
                    Column('model'),
                    Column('price'),
                    css_id="childs"
                ),
                (Submit('submit', 'Submit', css_class='btnForm')),
            )
        )
