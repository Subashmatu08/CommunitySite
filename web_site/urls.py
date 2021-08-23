from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("login/", views.login_page, name="login"),
    path("register/", views.register_page, name="register"),
    path("profile/", views.profile_view, name="profile"),
    # path("<str:category_name>/", views.feed_page, name="feed_page" ),
    # path("<str:category_name>/blogs/", views.blogs_page, name="blogs_page"),
    # path("<str:category_name>/codegists/", views.code_gists_page, name="code_gists_page"),
    path("createarticle/", views.create_blog, name="create_blog"),
    path("creategist/", views.create_code_gist, name="create_gist"),
    path("blog/<int:blog_id>/", views.view_blog, name="view_blog"),
    path("codegist/<int:code_gist_id>/", views.view_code_gist, name="view_code_gist"),
    path("logout", views.logout_view, name="logout"),
]
