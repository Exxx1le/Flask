from marshmallow_jsonapi import Schema, fields

#Описываем схему тега
class TagSchema(Schema):
    class Meta:
        type_ = "tag"
        self_view = "tag_detail"
        self_view_kwargs = {"id": "<id>"}
        self_view_many = "tag_list"
    
    d = fields.Integer(as_string=True)
    name = fields.String(allow_none=False, required=True)
    