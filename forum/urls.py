from django.urls import path
from .views import ForumListView, ForumThreadView, ForumThreadCreateView, ForumThreadDeleteView, ForumAddCommentView, ForumDeleteCommentView


app_name = "forum"

urlpatterns = [
    path("", ForumListView.as_view(), name="index"),                                    # forum index url
    path("<int:pk>/", ForumThreadView.as_view(), name="thread"),                        # thread detail url
    path("new/", ForumThreadCreateView.as_view(), name="thread_create"),                # thread create url
    path("<int:pk>/delete/", ForumThreadDeleteView.as_view(), name="thread_delete"),             # thread delete url
    path("<int:pk>/add_comment/", ForumAddCommentView.as_view(), name="add_comment"),            # add comment url
    path("<int:pk>/delete_comment/", ForumDeleteCommentView.as_view(), name="delete_comment")   # delete comment url
]
