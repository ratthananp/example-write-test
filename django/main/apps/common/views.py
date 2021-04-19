import asyncio

from django.db import transaction
from django.utils.decorators import classonlymethod, method_decorator
from django.views import View


@method_decorator(transaction.non_atomic_requests, name='dispatch')
class AsyncView(View):
    @classonlymethod
    def as_view(cls, **initkwargs):
        view = super().as_view(**initkwargs)
        view._is_coroutine = asyncio.coroutines._is_coroutine
        return view
