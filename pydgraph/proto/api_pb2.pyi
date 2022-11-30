from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Check(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class Facet(_message.Message):
    __slots__ = ["alias", "key", "tokens", "val_type", "value"]
    class ValType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    ALIAS_FIELD_NUMBER: _ClassVar[int]
    BOOL: Facet.ValType
    DATETIME: Facet.ValType
    FLOAT: Facet.ValType
    INT: Facet.ValType
    KEY_FIELD_NUMBER: _ClassVar[int]
    STRING: Facet.ValType
    TOKENS_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    VAL_TYPE_FIELD_NUMBER: _ClassVar[int]
    alias: str
    key: str
    tokens: _containers.RepeatedScalarFieldContainer[str]
    val_type: Facet.ValType
    value: bytes
    def __init__(self, key: _Optional[str] = ..., value: _Optional[bytes] = ..., val_type: _Optional[_Union[Facet.ValType, str]] = ..., tokens: _Optional[_Iterable[str]] = ..., alias: _Optional[str] = ...) -> None: ...

class Jwt(_message.Message):
    __slots__ = ["access_jwt", "refresh_jwt"]
    ACCESS_JWT_FIELD_NUMBER: _ClassVar[int]
    REFRESH_JWT_FIELD_NUMBER: _ClassVar[int]
    access_jwt: str
    refresh_jwt: str
    def __init__(self, access_jwt: _Optional[str] = ..., refresh_jwt: _Optional[str] = ...) -> None: ...

class Latency(_message.Message):
    __slots__ = ["assign_timestamp_ns", "encoding_ns", "parsing_ns", "processing_ns", "total_ns"]
    ASSIGN_TIMESTAMP_NS_FIELD_NUMBER: _ClassVar[int]
    ENCODING_NS_FIELD_NUMBER: _ClassVar[int]
    PARSING_NS_FIELD_NUMBER: _ClassVar[int]
    PROCESSING_NS_FIELD_NUMBER: _ClassVar[int]
    TOTAL_NS_FIELD_NUMBER: _ClassVar[int]
    assign_timestamp_ns: int
    encoding_ns: int
    parsing_ns: int
    processing_ns: int
    total_ns: int
    def __init__(self, parsing_ns: _Optional[int] = ..., processing_ns: _Optional[int] = ..., encoding_ns: _Optional[int] = ..., assign_timestamp_ns: _Optional[int] = ..., total_ns: _Optional[int] = ...) -> None: ...

class ListOfString(_message.Message):
    __slots__ = ["value"]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    value: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, value: _Optional[_Iterable[str]] = ...) -> None: ...

class LoginRequest(_message.Message):
    __slots__ = ["namespace", "password", "refresh_token", "userid"]
    NAMESPACE_FIELD_NUMBER: _ClassVar[int]
    PASSWORD_FIELD_NUMBER: _ClassVar[int]
    REFRESH_TOKEN_FIELD_NUMBER: _ClassVar[int]
    USERID_FIELD_NUMBER: _ClassVar[int]
    namespace: int
    password: str
    refresh_token: str
    userid: str
    def __init__(self, userid: _Optional[str] = ..., password: _Optional[str] = ..., refresh_token: _Optional[str] = ..., namespace: _Optional[int] = ...) -> None: ...

class Metrics(_message.Message):
    __slots__ = ["num_uids"]
    class NumUidsEntry(_message.Message):
        __slots__ = ["key", "value"]
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: int
        def __init__(self, key: _Optional[str] = ..., value: _Optional[int] = ...) -> None: ...
    NUM_UIDS_FIELD_NUMBER: _ClassVar[int]
    num_uids: _containers.ScalarMap[str, int]
    def __init__(self, num_uids: _Optional[_Mapping[str, int]] = ...) -> None: ...

class Mutation(_message.Message):
    __slots__ = ["commit_now", "cond", "del_nquads", "delete_json", "set", "set_json", "set_nquads"]
    COMMIT_NOW_FIELD_NUMBER: _ClassVar[int]
    COND_FIELD_NUMBER: _ClassVar[int]
    DELETE_JSON_FIELD_NUMBER: _ClassVar[int]
    DEL_FIELD_NUMBER: _ClassVar[int]
    DEL_NQUADS_FIELD_NUMBER: _ClassVar[int]
    SET_FIELD_NUMBER: _ClassVar[int]
    SET_JSON_FIELD_NUMBER: _ClassVar[int]
    SET_NQUADS_FIELD_NUMBER: _ClassVar[int]
    commit_now: bool
    cond: str
    del_nquads: bytes
    delete_json: bytes
    set: _containers.RepeatedCompositeFieldContainer[NQuad]
    set_json: bytes
    set_nquads: bytes
    def __init__(self, set_json: _Optional[bytes] = ..., delete_json: _Optional[bytes] = ..., set_nquads: _Optional[bytes] = ..., del_nquads: _Optional[bytes] = ..., set: _Optional[_Iterable[_Union[NQuad, _Mapping]]] = ..., cond: _Optional[str] = ..., commit_now: bool = ..., **kwargs) -> None: ...

class NQuad(_message.Message):
    __slots__ = ["facets", "lang", "namespace", "object_id", "object_value", "predicate", "subject"]
    FACETS_FIELD_NUMBER: _ClassVar[int]
    LANG_FIELD_NUMBER: _ClassVar[int]
    NAMESPACE_FIELD_NUMBER: _ClassVar[int]
    OBJECT_ID_FIELD_NUMBER: _ClassVar[int]
    OBJECT_VALUE_FIELD_NUMBER: _ClassVar[int]
    PREDICATE_FIELD_NUMBER: _ClassVar[int]
    SUBJECT_FIELD_NUMBER: _ClassVar[int]
    facets: _containers.RepeatedCompositeFieldContainer[Facet]
    lang: str
    namespace: int
    object_id: str
    object_value: Value
    predicate: str
    subject: str
    def __init__(self, subject: _Optional[str] = ..., predicate: _Optional[str] = ..., object_id: _Optional[str] = ..., object_value: _Optional[_Union[Value, _Mapping]] = ..., lang: _Optional[str] = ..., facets: _Optional[_Iterable[_Union[Facet, _Mapping]]] = ..., namespace: _Optional[int] = ...) -> None: ...

class Operation(_message.Message):
    __slots__ = ["drop_all", "drop_attr", "drop_op", "drop_value", "run_in_background", "schema"]
    class DropOp(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    ALL: Operation.DropOp
    ATTR: Operation.DropOp
    DATA: Operation.DropOp
    DROP_ALL_FIELD_NUMBER: _ClassVar[int]
    DROP_ATTR_FIELD_NUMBER: _ClassVar[int]
    DROP_OP_FIELD_NUMBER: _ClassVar[int]
    DROP_VALUE_FIELD_NUMBER: _ClassVar[int]
    NONE: Operation.DropOp
    RUN_IN_BACKGROUND_FIELD_NUMBER: _ClassVar[int]
    SCHEMA_FIELD_NUMBER: _ClassVar[int]
    TYPE: Operation.DropOp
    drop_all: bool
    drop_attr: str
    drop_op: Operation.DropOp
    drop_value: str
    run_in_background: bool
    schema: str
    def __init__(self, schema: _Optional[str] = ..., drop_attr: _Optional[str] = ..., drop_all: bool = ..., drop_op: _Optional[_Union[Operation.DropOp, str]] = ..., drop_value: _Optional[str] = ..., run_in_background: bool = ...) -> None: ...

class Payload(_message.Message):
    __slots__ = ["Data"]
    DATA_FIELD_NUMBER: _ClassVar[int]
    Data: bytes
    def __init__(self, Data: _Optional[bytes] = ...) -> None: ...

class Request(_message.Message):
    __slots__ = ["best_effort", "commit_now", "hash", "mutations", "query", "read_only", "resp_format", "start_ts", "vars"]
    class RespFormat(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    class VarsEntry(_message.Message):
        __slots__ = ["key", "value"]
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    BEST_EFFORT_FIELD_NUMBER: _ClassVar[int]
    COMMIT_NOW_FIELD_NUMBER: _ClassVar[int]
    HASH_FIELD_NUMBER: _ClassVar[int]
    JSON: Request.RespFormat
    MUTATIONS_FIELD_NUMBER: _ClassVar[int]
    QUERY_FIELD_NUMBER: _ClassVar[int]
    RDF: Request.RespFormat
    READ_ONLY_FIELD_NUMBER: _ClassVar[int]
    RESP_FORMAT_FIELD_NUMBER: _ClassVar[int]
    START_TS_FIELD_NUMBER: _ClassVar[int]
    VARS_FIELD_NUMBER: _ClassVar[int]
    best_effort: bool
    commit_now: bool
    hash: str
    mutations: _containers.RepeatedCompositeFieldContainer[Mutation]
    query: str
    read_only: bool
    resp_format: Request.RespFormat
    start_ts: int
    vars: _containers.ScalarMap[str, str]
    def __init__(self, start_ts: _Optional[int] = ..., query: _Optional[str] = ..., vars: _Optional[_Mapping[str, str]] = ..., read_only: bool = ..., best_effort: bool = ..., mutations: _Optional[_Iterable[_Union[Mutation, _Mapping]]] = ..., commit_now: bool = ..., resp_format: _Optional[_Union[Request.RespFormat, str]] = ..., hash: _Optional[str] = ...) -> None: ...

class Response(_message.Message):
    __slots__ = ["hdrs", "json", "latency", "metrics", "rdf", "txn", "uids"]
    class HdrsEntry(_message.Message):
        __slots__ = ["key", "value"]
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: ListOfString
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[ListOfString, _Mapping]] = ...) -> None: ...
    class UidsEntry(_message.Message):
        __slots__ = ["key", "value"]
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    HDRS_FIELD_NUMBER: _ClassVar[int]
    JSON_FIELD_NUMBER: _ClassVar[int]
    LATENCY_FIELD_NUMBER: _ClassVar[int]
    METRICS_FIELD_NUMBER: _ClassVar[int]
    RDF_FIELD_NUMBER: _ClassVar[int]
    TXN_FIELD_NUMBER: _ClassVar[int]
    UIDS_FIELD_NUMBER: _ClassVar[int]
    hdrs: _containers.MessageMap[str, ListOfString]
    json: bytes
    latency: Latency
    metrics: Metrics
    rdf: bytes
    txn: TxnContext
    uids: _containers.ScalarMap[str, str]
    def __init__(self, json: _Optional[bytes] = ..., txn: _Optional[_Union[TxnContext, _Mapping]] = ..., latency: _Optional[_Union[Latency, _Mapping]] = ..., metrics: _Optional[_Union[Metrics, _Mapping]] = ..., uids: _Optional[_Mapping[str, str]] = ..., rdf: _Optional[bytes] = ..., hdrs: _Optional[_Mapping[str, ListOfString]] = ...) -> None: ...

class TxnContext(_message.Message):
    __slots__ = ["aborted", "commit_ts", "hash", "keys", "preds", "start_ts"]
    ABORTED_FIELD_NUMBER: _ClassVar[int]
    COMMIT_TS_FIELD_NUMBER: _ClassVar[int]
    HASH_FIELD_NUMBER: _ClassVar[int]
    KEYS_FIELD_NUMBER: _ClassVar[int]
    PREDS_FIELD_NUMBER: _ClassVar[int]
    START_TS_FIELD_NUMBER: _ClassVar[int]
    aborted: bool
    commit_ts: int
    hash: str
    keys: _containers.RepeatedScalarFieldContainer[str]
    preds: _containers.RepeatedScalarFieldContainer[str]
    start_ts: int
    def __init__(self, start_ts: _Optional[int] = ..., commit_ts: _Optional[int] = ..., aborted: bool = ..., keys: _Optional[_Iterable[str]] = ..., preds: _Optional[_Iterable[str]] = ..., hash: _Optional[str] = ...) -> None: ...

class Uids(_message.Message):
    __slots__ = ["uids"]
    UIDS_FIELD_NUMBER: _ClassVar[int]
    uids: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, uids: _Optional[_Iterable[str]] = ...) -> None: ...

class Value(_message.Message):
    __slots__ = ["bool_val", "bytes_val", "date_val", "datetime_val", "default_val", "double_val", "geo_val", "int_val", "password_val", "str_val", "uid_val"]
    BOOL_VAL_FIELD_NUMBER: _ClassVar[int]
    BYTES_VAL_FIELD_NUMBER: _ClassVar[int]
    DATETIME_VAL_FIELD_NUMBER: _ClassVar[int]
    DATE_VAL_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_VAL_FIELD_NUMBER: _ClassVar[int]
    DOUBLE_VAL_FIELD_NUMBER: _ClassVar[int]
    GEO_VAL_FIELD_NUMBER: _ClassVar[int]
    INT_VAL_FIELD_NUMBER: _ClassVar[int]
    PASSWORD_VAL_FIELD_NUMBER: _ClassVar[int]
    STR_VAL_FIELD_NUMBER: _ClassVar[int]
    UID_VAL_FIELD_NUMBER: _ClassVar[int]
    bool_val: bool
    bytes_val: bytes
    date_val: bytes
    datetime_val: bytes
    default_val: str
    double_val: float
    geo_val: bytes
    int_val: int
    password_val: str
    str_val: str
    uid_val: int
    def __init__(self, default_val: _Optional[str] = ..., bytes_val: _Optional[bytes] = ..., int_val: _Optional[int] = ..., bool_val: bool = ..., str_val: _Optional[str] = ..., double_val: _Optional[float] = ..., geo_val: _Optional[bytes] = ..., date_val: _Optional[bytes] = ..., datetime_val: _Optional[bytes] = ..., password_val: _Optional[str] = ..., uid_val: _Optional[int] = ...) -> None: ...

class Version(_message.Message):
    __slots__ = ["tag"]
    TAG_FIELD_NUMBER: _ClassVar[int]
    tag: str
    def __init__(self, tag: _Optional[str] = ...) -> None: ...
