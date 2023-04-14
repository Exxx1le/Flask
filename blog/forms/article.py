from wtforms import StringField, TextAreaField, SubmitField, validators, Form


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