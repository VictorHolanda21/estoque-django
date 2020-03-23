from django.urls import path
from projeto.estoque import views as v

app_name = "estoque"

urlpatterns = [
	path('', v.estoque_entrada_list, name="estoque_entrada_list"),
	# path('<int:pk>/', v.estoque_detail, name="estoque_detail"),
	# path('<int:pk>/edit/', v.EstoqueUpdate.as_view(), name="estoque_update"),
	# path('add/', v.EstoqueCreate.as_view(), name="estoque_add"),
]