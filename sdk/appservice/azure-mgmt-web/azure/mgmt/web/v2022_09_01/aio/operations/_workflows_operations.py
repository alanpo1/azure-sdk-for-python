# pylint: disable=too-many-lines
# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
import sys
from typing import Any, Callable, Dict, IO, Optional, TypeVar, Union, overload

from azure.core.exceptions import (
    ClientAuthenticationError,
    HttpResponseError,
    ResourceExistsError,
    ResourceNotFoundError,
    ResourceNotModifiedError,
    map_error,
)
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import AsyncHttpResponse
from azure.core.rest import HttpRequest
from azure.core.tracing.decorator_async import distributed_trace_async
from azure.core.utils import case_insensitive_dict
from azure.mgmt.core.exceptions import ARMErrorFormat

from ... import models as _models
from ..._vendor import _convert_request
from ...operations._workflows_operations import build_regenerate_access_key_request, build_validate_request
from .._vendor import WebSiteManagementClientMixinABC

if sys.version_info >= (3, 8):
    from typing import Literal  # pylint: disable=no-name-in-module, ungrouped-imports
else:
    from typing_extensions import Literal  # type: ignore  # pylint: disable=ungrouped-imports
T = TypeVar("T")
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, AsyncHttpResponse], T, Dict[str, Any]], Any]]


class WorkflowsOperations:
    """
    .. warning::
        **DO NOT** instantiate this class directly.

        Instead, you should access the following operations through
        :class:`~azure.mgmt.web.v2022_09_01.aio.WebSiteManagementClient`'s
        :attr:`workflows` attribute.
    """

    models = _models

    def __init__(self, *args, **kwargs) -> None:
        input_args = list(args)
        self._client = input_args.pop(0) if input_args else kwargs.pop("client")
        self._config = input_args.pop(0) if input_args else kwargs.pop("config")
        self._serialize = input_args.pop(0) if input_args else kwargs.pop("serializer")
        self._deserialize = input_args.pop(0) if input_args else kwargs.pop("deserializer")

    @overload
    async def regenerate_access_key(  # pylint: disable=inconsistent-return-statements
        self,
        resource_group_name: str,
        name: str,
        workflow_name: str,
        key_type: _models.RegenerateActionParameter,
        *,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> None:
        """Regenerates the callback URL access key for request triggers.

        :param resource_group_name: Name of the resource group to which the resource belongs. Required.
        :type resource_group_name: str
        :param name: Site name. Required.
        :type name: str
        :param workflow_name: The workflow name. Required.
        :type workflow_name: str
        :param key_type: The access key type. Required.
        :type key_type: ~azure.mgmt.web.v2022_09_01.models.RegenerateActionParameter
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None or the result of cls(response)
        :rtype: None
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @overload
    async def regenerate_access_key(  # pylint: disable=inconsistent-return-statements
        self,
        resource_group_name: str,
        name: str,
        workflow_name: str,
        key_type: IO,
        *,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> None:
        """Regenerates the callback URL access key for request triggers.

        :param resource_group_name: Name of the resource group to which the resource belongs. Required.
        :type resource_group_name: str
        :param name: Site name. Required.
        :type name: str
        :param workflow_name: The workflow name. Required.
        :type workflow_name: str
        :param key_type: The access key type. Required.
        :type key_type: IO
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None or the result of cls(response)
        :rtype: None
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @distributed_trace_async
    async def regenerate_access_key(  # pylint: disable=inconsistent-return-statements
        self,
        resource_group_name: str,
        name: str,
        workflow_name: str,
        key_type: Union[_models.RegenerateActionParameter, IO],
        **kwargs: Any
    ) -> None:
        """Regenerates the callback URL access key for request triggers.

        :param resource_group_name: Name of the resource group to which the resource belongs. Required.
        :type resource_group_name: str
        :param name: Site name. Required.
        :type name: str
        :param workflow_name: The workflow name. Required.
        :type workflow_name: str
        :param key_type: The access key type. Is either a RegenerateActionParameter type or a IO type.
         Required.
        :type key_type: ~azure.mgmt.web.v2022_09_01.models.RegenerateActionParameter or IO
        :keyword content_type: Body Parameter content-type. Known values are: 'application/json'.
         Default value is None.
        :paramtype content_type: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None or the result of cls(response)
        :rtype: None
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        error_map = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version: Literal["2022-09-01"] = kwargs.pop("api_version", _params.pop("api-version", "2022-09-01"))
        content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("Content-Type", None))
        cls: ClsType[None] = kwargs.pop("cls", None)

        content_type = content_type or "application/json"
        _json = None
        _content = None
        if isinstance(key_type, (IO, bytes)):
            _content = key_type
        else:
            _json = self._serialize.body(key_type, "RegenerateActionParameter")

        request = build_regenerate_access_key_request(
            resource_group_name=resource_group_name,
            name=name,
            workflow_name=workflow_name,
            subscription_id=self._config.subscription_id,
            api_version=api_version,
            content_type=content_type,
            json=_json,
            content=_content,
            template_url=self.regenerate_access_key.metadata["url"],
            headers=_headers,
            params=_params,
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)

        _stream = False
        pipeline_response: PipelineResponse = await self._client._pipeline.run(  # pylint: disable=protected-access
            request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.ErrorResponse, pipeline_response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        if cls:
            return cls(pipeline_response, None, {})

    regenerate_access_key.metadata = {
        "url": "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/hostruntime/runtime/webhooks/workflow/api/management/workflows/{workflowName}/regenerateAccessKey"
    }

    @overload
    async def validate(  # pylint: disable=inconsistent-return-statements
        self,
        resource_group_name: str,
        name: str,
        workflow_name: str,
        validate: _models.Workflow,
        *,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> None:
        """Validates the workflow definition.

        :param resource_group_name: Name of the resource group to which the resource belongs. Required.
        :type resource_group_name: str
        :param name: Site name. Required.
        :type name: str
        :param workflow_name: The workflow name. Required.
        :type workflow_name: str
        :param validate: The workflow. Required.
        :type validate: ~azure.mgmt.web.v2022_09_01.models.Workflow
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None or the result of cls(response)
        :rtype: None
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @overload
    async def validate(  # pylint: disable=inconsistent-return-statements
        self,
        resource_group_name: str,
        name: str,
        workflow_name: str,
        validate: IO,
        *,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> None:
        """Validates the workflow definition.

        :param resource_group_name: Name of the resource group to which the resource belongs. Required.
        :type resource_group_name: str
        :param name: Site name. Required.
        :type name: str
        :param workflow_name: The workflow name. Required.
        :type workflow_name: str
        :param validate: The workflow. Required.
        :type validate: IO
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None or the result of cls(response)
        :rtype: None
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @distributed_trace_async
    async def validate(  # pylint: disable=inconsistent-return-statements
        self,
        resource_group_name: str,
        name: str,
        workflow_name: str,
        validate: Union[_models.Workflow, IO],
        **kwargs: Any
    ) -> None:
        """Validates the workflow definition.

        :param resource_group_name: Name of the resource group to which the resource belongs. Required.
        :type resource_group_name: str
        :param name: Site name. Required.
        :type name: str
        :param workflow_name: The workflow name. Required.
        :type workflow_name: str
        :param validate: The workflow. Is either a Workflow type or a IO type. Required.
        :type validate: ~azure.mgmt.web.v2022_09_01.models.Workflow or IO
        :keyword content_type: Body Parameter content-type. Known values are: 'application/json'.
         Default value is None.
        :paramtype content_type: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None or the result of cls(response)
        :rtype: None
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        error_map = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version: Literal["2022-09-01"] = kwargs.pop("api_version", _params.pop("api-version", "2022-09-01"))
        content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("Content-Type", None))
        cls: ClsType[None] = kwargs.pop("cls", None)

        content_type = content_type or "application/json"
        _json = None
        _content = None
        if isinstance(validate, (IO, bytes)):
            _content = validate
        else:
            _json = self._serialize.body(validate, "Workflow")

        request = build_validate_request(
            resource_group_name=resource_group_name,
            name=name,
            workflow_name=workflow_name,
            subscription_id=self._config.subscription_id,
            api_version=api_version,
            content_type=content_type,
            json=_json,
            content=_content,
            template_url=self.validate.metadata["url"],
            headers=_headers,
            params=_params,
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)

        _stream = False
        pipeline_response: PipelineResponse = await self._client._pipeline.run(  # pylint: disable=protected-access
            request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.ErrorResponse, pipeline_response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        if cls:
            return cls(pipeline_response, None, {})

    validate.metadata = {
        "url": "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/hostruntime/runtime/webhooks/workflow/api/management/workflows/{workflowName}/validate"
    }
