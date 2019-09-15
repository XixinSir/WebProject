from django.conf.urls import url, include
from . import views

# 配置路由
urlpatterns = [
    url(r"^$", views.index, name="index"),
    url(r"^student/$", views.students),
    url(r"^good/(\d+)$", views.good, name="good"),
    url(r"^main/$", views.main),
    url(r"^detail/$", views.detail),
    url(r"^postfile/$", views.postfile),
    url(r"^showinfo/$", views.showinfo),
    url(r"^verifycode/$", views.verifycode),
    url(r"^verifycodecheck/$", views.verifycodecheck),
    url(r"^verifycodefile/$", views.verifycodefile),
]


