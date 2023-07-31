from django.apps import AppConfig


class UsersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'users'

    def ready(self):
        from users.urls import router
        from agent.router import router as main_router

        main_router.extend(router)
