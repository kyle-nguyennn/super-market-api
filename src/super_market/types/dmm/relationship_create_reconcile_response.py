# File generated from our OpenAPI spec by Scalar. See README.md for details.

from typing import List
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["RelationshipCreateReconcileResponse"]


class RelationshipCreateReconcileResponse(BaseModel):
    engine_sync: Literal["queued"] = FieldInfo(alias="engineSync")

    derivation_diagnostics: List[object] = FieldInfo(alias="derivationDiagnostics")

    mapping_diagnostics: List[object] = FieldInfo(alias="mappingDiagnostics")
