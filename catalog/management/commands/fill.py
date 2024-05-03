from django.core.management import BaseCommand
from django.conf import settings
from catalog.models import Product, Category


class Command(BaseCommand):
    requires_migrations_checks = True

    def handle(self, *args, **options) -> None:
        Category.objects.all().delete()
        Product.objects.all().delete()
        json_path = settings.BASE_DIR.joinpath('catalog.json')
        if not json_path.exists():
            self.stdout.write('Path not found', self.style.NOTICE)
            return

