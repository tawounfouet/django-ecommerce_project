from django.core.management.base import BaseCommand
from accounts.models import UserProfile

class Command(BaseCommand):
    help = 'Deletes a user profile record'

    def add_arguments(self, parser):
        parser.add_argument('user_id', type=int, help='The ID of the user profile to delete')

    def handle(self, *args, **kwargs):
        user_id = kwargs['user_id']
        try:
            profile = UserProfile.objects.get(user_id=user_id)
            profile.delete()
            self.stdout.write(self.style.SUCCESS('User profile with ID {} deleted successfully'.format(user_id)))
        except UserProfile.DoesNotExist:
            self.stdout.write(self.style.ERROR('User profile with ID {} does not exist'.format(user_id)))
