from typing import Annotated

from fastapi import Depends, HTTPException, Path

from zpodapi.lib.global_dependencies import service_init_annotation
from zpodcommon import models as M

from .endpoint__services import EndpointService
from .endpoint__types import EndpointIdType


async def get_endpoint(
    *,
    endpoint_service: "EndpointAnnotations.EndpointService",
    id: Annotated[
        EndpointIdType,
        Path(
            examples={
                "id": {"value": "1"},
                "name": {"value": "name=main"},
            },
        ),
    ],
):
    if endpoint := endpoint_service.get(value=id):
        return endpoint
    raise HTTPException(status_code=404, detail="Endpoint not found")


class EndpointDepends:
    pass


class EndpointAnnotations:
    GetEndpoint = Annotated[M.Endpoint, Depends(get_endpoint)]
    EndpointService = service_init_annotation(EndpointService)
