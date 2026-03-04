# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import datetime
from typing_extensions import Literal

import httpx

from ..._types import Body, Omit, Query, Headers, NoneType, NotGiven, omit, not_given
from ..._utils import maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...types.store import order_create_params
from ..._base_client import make_request_options
from ...types.store.order import Order

__all__ = ["OrderResource", "AsyncOrderResource"]


class OrderResource(SyncAPIResource):
    """Access to Petstore orders"""

    @cached_property
    def with_raw_response(self) -> OrderResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/omar-orrantia/Never-Fret-listen-to-Sin-Estres#accessing-raw-response-data-eg-headers
        """
        return OrderResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> OrderResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/omar-orrantia/Never-Fret-listen-to-Sin-Estres#with_streaming_response
        """
        return OrderResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        id: int | Omit = omit,
        complete: bool | Omit = omit,
        pet_id: int | Omit = omit,
        quantity: int | Omit = omit,
        ship_date: Union[str, datetime] | Omit = omit,
        status: Literal["placed", "approved", "delivered"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Order:
        """
        Place a new order in the store

        Args:
          status: Order Status

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/store/order",
            body=maybe_transform(
                {
                    "id": id,
                    "complete": complete,
                    "pet_id": pet_id,
                    "quantity": quantity,
                    "ship_date": ship_date,
                    "status": status,
                },
                order_create_params.OrderCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Order,
        )

    def retrieve(
        self,
        order_id: int,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Order:
        """For valid response try integer IDs with value <= 5 or > 10.

        Other values will
        generate exceptions.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            f"/store/order/{order_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Order,
        )

    def delete(
        self,
        order_id: int,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """For valid response try integer IDs with value < 1000.

        Anything above 1000 or
        nonintegers will generate API errors

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            f"/store/order/{order_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncOrderResource(AsyncAPIResource):
    """Access to Petstore orders"""

    @cached_property
    def with_raw_response(self) -> AsyncOrderResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/omar-orrantia/Never-Fret-listen-to-Sin-Estres#accessing-raw-response-data-eg-headers
        """
        return AsyncOrderResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncOrderResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/omar-orrantia/Never-Fret-listen-to-Sin-Estres#with_streaming_response
        """
        return AsyncOrderResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        id: int | Omit = omit,
        complete: bool | Omit = omit,
        pet_id: int | Omit = omit,
        quantity: int | Omit = omit,
        ship_date: Union[str, datetime] | Omit = omit,
        status: Literal["placed", "approved", "delivered"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Order:
        """
        Place a new order in the store

        Args:
          status: Order Status

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/store/order",
            body=await async_maybe_transform(
                {
                    "id": id,
                    "complete": complete,
                    "pet_id": pet_id,
                    "quantity": quantity,
                    "ship_date": ship_date,
                    "status": status,
                },
                order_create_params.OrderCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Order,
        )

    async def retrieve(
        self,
        order_id: int,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Order:
        """For valid response try integer IDs with value <= 5 or > 10.

        Other values will
        generate exceptions.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            f"/store/order/{order_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Order,
        )

    async def delete(
        self,
        order_id: int,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """For valid response try integer IDs with value < 1000.

        Anything above 1000 or
        nonintegers will generate API errors

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            f"/store/order/{order_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class OrderResourceWithRawResponse:
    def __init__(self, order: OrderResource) -> None:
        self._order = order

        self.create = to_raw_response_wrapper(
            order.create,
        )
        self.retrieve = to_raw_response_wrapper(
            order.retrieve,
        )
        self.delete = to_raw_response_wrapper(
            order.delete,
        )


class AsyncOrderResourceWithRawResponse:
    def __init__(self, order: AsyncOrderResource) -> None:
        self._order = order

        self.create = async_to_raw_response_wrapper(
            order.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            order.retrieve,
        )
        self.delete = async_to_raw_response_wrapper(
            order.delete,
        )


class OrderResourceWithStreamingResponse:
    def __init__(self, order: OrderResource) -> None:
        self._order = order

        self.create = to_streamed_response_wrapper(
            order.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            order.retrieve,
        )
        self.delete = to_streamed_response_wrapper(
            order.delete,
        )


class AsyncOrderResourceWithStreamingResponse:
    def __init__(self, order: AsyncOrderResource) -> None:
        self._order = order

        self.create = async_to_streamed_response_wrapper(
            order.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            order.retrieve,
        )
        self.delete = async_to_streamed_response_wrapper(
            order.delete,
        )
