from wtforms import StringField, TextAreaField, SubmitField, SelectMultipleField, validators, Form


class CreateArticleForm(Form):
    title = StringField(
        "Title",
        [validators.DataRequired()],
    )
    body = TextAreaField(
        "Body",
        [validators.DataRequired()],
    )
    submit = SubmitField("Publish")
    tags = SelectMultipleField("Tags", coerce=int)