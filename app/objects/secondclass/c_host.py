import marshmallow as ma

from app.utility.base_object import BaseObject
from plugins.crag.app.objects.secondclass.c_port import PortSchema


class HostSchema(ma.Schema):

    unique = ma.fields.String()
    hostname = ma.fields.String()
    ip = ma.fields.String()
    ports = ma.fields.Dict(keys=ma.fields.Integer(), values=ma.fields.Nested(PortSchema()))
    cves = ma.fields.List(ma.fields.String())

    @ma.post_load()
    def build_host(self, data, **_):
        return Host(**data)


class Host(BaseObject):

    schema = HostSchema()

    def __init__(self, ip, hostname=None, match='.*'):
        super().__init__()
        self.hostname = hostname
        self.ip = ip
        self.ports = dict()
        self.cves = []
