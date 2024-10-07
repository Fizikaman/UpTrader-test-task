from django.core.management.base import BaseCommand
from menus.models import Menu, MenuItem


class Command(BaseCommand):
    help = 'Заполняет базу данных примерным меню'

    def handle(self, *args, **options):
        main_menu = Menu.objects.create(name='main_menu')

        home = MenuItem.objects.create(
            menu=main_menu, title='Главная', url='/', order=1
        )

        about = MenuItem.objects.create(
            menu=main_menu, title='О нас', named_url='about', order=2
        )

        services = MenuItem.objects.create(
            menu=main_menu, title='Услуги', url='/services/', order=3
        )

        web_dev = MenuItem.objects.create(
            menu=main_menu, title='Веб-разработка', parent=services, url='/services/web-development/', order=1
        )

        seo = MenuItem.objects.create(
            menu=main_menu, title='SEO', parent=services, url='/services/seo/', order=2
        )

        contact = MenuItem.objects.create(
            menu=main_menu, title='Контакты', url='/contact/', order=4
        )

        self.stdout.write(self.style.SUCCESS('База данных успешно заполнена примерным меню.'))
