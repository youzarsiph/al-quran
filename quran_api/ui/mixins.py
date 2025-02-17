""" Generic View Mixins """

from typing import Any, Dict, Optional
from django.contrib.auth.mixins import UserPassesTestMixin


# Create your mixins here.
class AdminUserMixin(UserPassesTestMixin):
    """Check if the user is an admin"""

    def test_func(self) -> Optional[bool]:
        return self.request.user.is_staff


class ExtraContextMixin:
    """Passes extra context to templates"""

    extra_context = {}

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        return {**super().get_context_data(**kwargs), **self.extra_context}
