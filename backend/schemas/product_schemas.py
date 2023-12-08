from marshmallow import fields, validates, ValidationError

class ProductSchema:
    name = fields.String(required=True)
    category = fields.String(required=True)
    price = fields.Float(required=True)

    @validates('name')
    def validate_name(self, value):
        if len(value) < 5:
            raise ValidationError('Name must be at least 5 characters long.')

    @validates('category')
    def validate_category(self, value):
        if len(value) < 3:
            raise ValidationError('Category must be at least 3 characters long.')

    @validates('price')
    def validate_price(self, value):
        if value <= 0:
            raise ValidationError('Price must be greater than zero.')
