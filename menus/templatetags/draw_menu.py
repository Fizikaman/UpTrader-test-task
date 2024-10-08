from django import template
from django.urls import reverse, NoReverseMatch

register = template.Library()


@register.inclusion_tag('menu.html', takes_context=True)
def render_menu(context, menu):
    return {'menu': menu, 'request': context['request']}


def resolve_url(item):
    try:
        return reverse(item['url_resolved'])
    except NoReverseMatch:
        return item['url_resolved']


@register.simple_tag
def render_menu_item(item):
    url = resolve_url(item)
    return f'<a href="{url}">{item["title"]}</a>'

