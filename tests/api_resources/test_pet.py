# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from strezless_musick_nexus_metadata import StrezlessMusickNexusMetadata, AsyncStrezlessMusickNexusMetadata
from strezless_musick_nexus_metadata.types import (
    Pet,
    PetFindByTagsResponse,
    PetUploadImageResponse,
    PetFindByStatusResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestPet:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create(self, client: StrezlessMusickNexusMetadata) -> None:
        pet = client.pet.create(
            name="doggie",
            photo_urls=["string"],
        )
        assert_matches_type(Pet, pet, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: StrezlessMusickNexusMetadata) -> None:
        pet = client.pet.create(
            name="doggie",
            photo_urls=["string"],
            id=10,
            category={
                "id": 1,
                "name": "Dogs",
            },
            status="available",
            tags=[
                {
                    "id": 0,
                    "name": "name",
                }
            ],
        )
        assert_matches_type(Pet, pet, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: StrezlessMusickNexusMetadata) -> None:
        response = client.pet.with_raw_response.create(
            name="doggie",
            photo_urls=["string"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        pet = response.parse()
        assert_matches_type(Pet, pet, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: StrezlessMusickNexusMetadata) -> None:
        with client.pet.with_streaming_response.create(
            name="doggie",
            photo_urls=["string"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            pet = response.parse()
            assert_matches_type(Pet, pet, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: StrezlessMusickNexusMetadata) -> None:
        pet = client.pet.retrieve(
            0,
        )
        assert_matches_type(Pet, pet, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: StrezlessMusickNexusMetadata) -> None:
        response = client.pet.with_raw_response.retrieve(
            0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        pet = response.parse()
        assert_matches_type(Pet, pet, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: StrezlessMusickNexusMetadata) -> None:
        with client.pet.with_streaming_response.retrieve(
            0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            pet = response.parse()
            assert_matches_type(Pet, pet, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update(self, client: StrezlessMusickNexusMetadata) -> None:
        pet = client.pet.update(
            name="doggie",
            photo_urls=["string"],
        )
        assert_matches_type(Pet, pet, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update_with_all_params(self, client: StrezlessMusickNexusMetadata) -> None:
        pet = client.pet.update(
            name="doggie",
            photo_urls=["string"],
            id=10,
            category={
                "id": 1,
                "name": "Dogs",
            },
            status="available",
            tags=[
                {
                    "id": 0,
                    "name": "name",
                }
            ],
        )
        assert_matches_type(Pet, pet, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: StrezlessMusickNexusMetadata) -> None:
        response = client.pet.with_raw_response.update(
            name="doggie",
            photo_urls=["string"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        pet = response.parse()
        assert_matches_type(Pet, pet, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: StrezlessMusickNexusMetadata) -> None:
        with client.pet.with_streaming_response.update(
            name="doggie",
            photo_urls=["string"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            pet = response.parse()
            assert_matches_type(Pet, pet, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete(self, client: StrezlessMusickNexusMetadata) -> None:
        pet = client.pet.delete(
            0,
        )
        assert pet is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: StrezlessMusickNexusMetadata) -> None:
        response = client.pet.with_raw_response.delete(
            0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        pet = response.parse()
        assert pet is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: StrezlessMusickNexusMetadata) -> None:
        with client.pet.with_streaming_response.delete(
            0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            pet = response.parse()
            assert pet is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_find_by_status(self, client: StrezlessMusickNexusMetadata) -> None:
        pet = client.pet.find_by_status()
        assert_matches_type(PetFindByStatusResponse, pet, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_find_by_status_with_all_params(self, client: StrezlessMusickNexusMetadata) -> None:
        pet = client.pet.find_by_status(
            status="available",
        )
        assert_matches_type(PetFindByStatusResponse, pet, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_find_by_status(self, client: StrezlessMusickNexusMetadata) -> None:
        response = client.pet.with_raw_response.find_by_status()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        pet = response.parse()
        assert_matches_type(PetFindByStatusResponse, pet, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_find_by_status(self, client: StrezlessMusickNexusMetadata) -> None:
        with client.pet.with_streaming_response.find_by_status() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            pet = response.parse()
            assert_matches_type(PetFindByStatusResponse, pet, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_find_by_tags(self, client: StrezlessMusickNexusMetadata) -> None:
        pet = client.pet.find_by_tags()
        assert_matches_type(PetFindByTagsResponse, pet, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_find_by_tags_with_all_params(self, client: StrezlessMusickNexusMetadata) -> None:
        pet = client.pet.find_by_tags(
            tags=["string"],
        )
        assert_matches_type(PetFindByTagsResponse, pet, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_find_by_tags(self, client: StrezlessMusickNexusMetadata) -> None:
        response = client.pet.with_raw_response.find_by_tags()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        pet = response.parse()
        assert_matches_type(PetFindByTagsResponse, pet, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_find_by_tags(self, client: StrezlessMusickNexusMetadata) -> None:
        with client.pet.with_streaming_response.find_by_tags() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            pet = response.parse()
            assert_matches_type(PetFindByTagsResponse, pet, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update_with_form(self, client: StrezlessMusickNexusMetadata) -> None:
        pet = client.pet.update_with_form(
            pet_id=0,
        )
        assert pet is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update_with_form_with_all_params(self, client: StrezlessMusickNexusMetadata) -> None:
        pet = client.pet.update_with_form(
            pet_id=0,
            name="name",
            status="status",
        )
        assert pet is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_update_with_form(self, client: StrezlessMusickNexusMetadata) -> None:
        response = client.pet.with_raw_response.update_with_form(
            pet_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        pet = response.parse()
        assert pet is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_update_with_form(self, client: StrezlessMusickNexusMetadata) -> None:
        with client.pet.with_streaming_response.update_with_form(
            pet_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            pet = response.parse()
            assert pet is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_upload_image(self, client: StrezlessMusickNexusMetadata) -> None:
        pet = client.pet.upload_image(
            pet_id=0,
            body=b"Example data",
        )
        assert_matches_type(PetUploadImageResponse, pet, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_upload_image_with_all_params(self, client: StrezlessMusickNexusMetadata) -> None:
        pet = client.pet.upload_image(
            pet_id=0,
            body=b"Example data",
            additional_metadata="additionalMetadata",
        )
        assert_matches_type(PetUploadImageResponse, pet, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_upload_image(self, client: StrezlessMusickNexusMetadata) -> None:
        response = client.pet.with_raw_response.upload_image(
            pet_id=0,
            body=b"Example data",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        pet = response.parse()
        assert_matches_type(PetUploadImageResponse, pet, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_upload_image(self, client: StrezlessMusickNexusMetadata) -> None:
        with client.pet.with_streaming_response.upload_image(
            pet_id=0,
            body=b"Example data",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            pet = response.parse()
            assert_matches_type(PetUploadImageResponse, pet, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncPet:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncStrezlessMusickNexusMetadata) -> None:
        pet = await async_client.pet.create(
            name="doggie",
            photo_urls=["string"],
        )
        assert_matches_type(Pet, pet, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncStrezlessMusickNexusMetadata) -> None:
        pet = await async_client.pet.create(
            name="doggie",
            photo_urls=["string"],
            id=10,
            category={
                "id": 1,
                "name": "Dogs",
            },
            status="available",
            tags=[
                {
                    "id": 0,
                    "name": "name",
                }
            ],
        )
        assert_matches_type(Pet, pet, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncStrezlessMusickNexusMetadata) -> None:
        response = await async_client.pet.with_raw_response.create(
            name="doggie",
            photo_urls=["string"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        pet = await response.parse()
        assert_matches_type(Pet, pet, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncStrezlessMusickNexusMetadata) -> None:
        async with async_client.pet.with_streaming_response.create(
            name="doggie",
            photo_urls=["string"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            pet = await response.parse()
            assert_matches_type(Pet, pet, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncStrezlessMusickNexusMetadata) -> None:
        pet = await async_client.pet.retrieve(
            0,
        )
        assert_matches_type(Pet, pet, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncStrezlessMusickNexusMetadata) -> None:
        response = await async_client.pet.with_raw_response.retrieve(
            0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        pet = await response.parse()
        assert_matches_type(Pet, pet, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncStrezlessMusickNexusMetadata) -> None:
        async with async_client.pet.with_streaming_response.retrieve(
            0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            pet = await response.parse()
            assert_matches_type(Pet, pet, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncStrezlessMusickNexusMetadata) -> None:
        pet = await async_client.pet.update(
            name="doggie",
            photo_urls=["string"],
        )
        assert_matches_type(Pet, pet, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncStrezlessMusickNexusMetadata) -> None:
        pet = await async_client.pet.update(
            name="doggie",
            photo_urls=["string"],
            id=10,
            category={
                "id": 1,
                "name": "Dogs",
            },
            status="available",
            tags=[
                {
                    "id": 0,
                    "name": "name",
                }
            ],
        )
        assert_matches_type(Pet, pet, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncStrezlessMusickNexusMetadata) -> None:
        response = await async_client.pet.with_raw_response.update(
            name="doggie",
            photo_urls=["string"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        pet = await response.parse()
        assert_matches_type(Pet, pet, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncStrezlessMusickNexusMetadata) -> None:
        async with async_client.pet.with_streaming_response.update(
            name="doggie",
            photo_urls=["string"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            pet = await response.parse()
            assert_matches_type(Pet, pet, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncStrezlessMusickNexusMetadata) -> None:
        pet = await async_client.pet.delete(
            0,
        )
        assert pet is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncStrezlessMusickNexusMetadata) -> None:
        response = await async_client.pet.with_raw_response.delete(
            0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        pet = await response.parse()
        assert pet is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncStrezlessMusickNexusMetadata) -> None:
        async with async_client.pet.with_streaming_response.delete(
            0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            pet = await response.parse()
            assert pet is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_find_by_status(self, async_client: AsyncStrezlessMusickNexusMetadata) -> None:
        pet = await async_client.pet.find_by_status()
        assert_matches_type(PetFindByStatusResponse, pet, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_find_by_status_with_all_params(self, async_client: AsyncStrezlessMusickNexusMetadata) -> None:
        pet = await async_client.pet.find_by_status(
            status="available",
        )
        assert_matches_type(PetFindByStatusResponse, pet, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_find_by_status(self, async_client: AsyncStrezlessMusickNexusMetadata) -> None:
        response = await async_client.pet.with_raw_response.find_by_status()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        pet = await response.parse()
        assert_matches_type(PetFindByStatusResponse, pet, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_find_by_status(self, async_client: AsyncStrezlessMusickNexusMetadata) -> None:
        async with async_client.pet.with_streaming_response.find_by_status() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            pet = await response.parse()
            assert_matches_type(PetFindByStatusResponse, pet, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_find_by_tags(self, async_client: AsyncStrezlessMusickNexusMetadata) -> None:
        pet = await async_client.pet.find_by_tags()
        assert_matches_type(PetFindByTagsResponse, pet, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_find_by_tags_with_all_params(self, async_client: AsyncStrezlessMusickNexusMetadata) -> None:
        pet = await async_client.pet.find_by_tags(
            tags=["string"],
        )
        assert_matches_type(PetFindByTagsResponse, pet, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_find_by_tags(self, async_client: AsyncStrezlessMusickNexusMetadata) -> None:
        response = await async_client.pet.with_raw_response.find_by_tags()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        pet = await response.parse()
        assert_matches_type(PetFindByTagsResponse, pet, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_find_by_tags(self, async_client: AsyncStrezlessMusickNexusMetadata) -> None:
        async with async_client.pet.with_streaming_response.find_by_tags() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            pet = await response.parse()
            assert_matches_type(PetFindByTagsResponse, pet, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update_with_form(self, async_client: AsyncStrezlessMusickNexusMetadata) -> None:
        pet = await async_client.pet.update_with_form(
            pet_id=0,
        )
        assert pet is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update_with_form_with_all_params(
        self, async_client: AsyncStrezlessMusickNexusMetadata
    ) -> None:
        pet = await async_client.pet.update_with_form(
            pet_id=0,
            name="name",
            status="status",
        )
        assert pet is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_update_with_form(self, async_client: AsyncStrezlessMusickNexusMetadata) -> None:
        response = await async_client.pet.with_raw_response.update_with_form(
            pet_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        pet = await response.parse()
        assert pet is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_update_with_form(self, async_client: AsyncStrezlessMusickNexusMetadata) -> None:
        async with async_client.pet.with_streaming_response.update_with_form(
            pet_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            pet = await response.parse()
            assert pet is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_upload_image(self, async_client: AsyncStrezlessMusickNexusMetadata) -> None:
        pet = await async_client.pet.upload_image(
            pet_id=0,
            body=b"Example data",
        )
        assert_matches_type(PetUploadImageResponse, pet, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_upload_image_with_all_params(self, async_client: AsyncStrezlessMusickNexusMetadata) -> None:
        pet = await async_client.pet.upload_image(
            pet_id=0,
            body=b"Example data",
            additional_metadata="additionalMetadata",
        )
        assert_matches_type(PetUploadImageResponse, pet, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_upload_image(self, async_client: AsyncStrezlessMusickNexusMetadata) -> None:
        response = await async_client.pet.with_raw_response.upload_image(
            pet_id=0,
            body=b"Example data",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        pet = await response.parse()
        assert_matches_type(PetUploadImageResponse, pet, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_upload_image(self, async_client: AsyncStrezlessMusickNexusMetadata) -> None:
        async with async_client.pet.with_streaming_response.upload_image(
            pet_id=0,
            body=b"Example data",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            pet = await response.parse()
            assert_matches_type(PetUploadImageResponse, pet, path=["response"])

        assert cast(Any, response.is_closed) is True
