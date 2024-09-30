

from django.urls import path
from .views import delete_user, upload_data_view, query_builder_view, QueryBuilderAPIView, user_list

urlpatterns = [
    # upload data
    path('', upload_data_view, name='upload_data'),
    
    # query builder
    path('query/', query_builder_view, name='query_builder'),
    path('api/query/', QueryBuilderAPIView.as_view(), name='query_builder_api'),
    
    # user management
    path('users/', user_list, name='user_list'),
    path('users/delete/<int:user_id>/', delete_user, name='delete_user'),
]