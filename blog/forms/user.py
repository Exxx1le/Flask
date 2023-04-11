from wtforms import Form, StringField, validators, PasswordField, SubmitField


class UserBaseForm(Form):
    first_name = StringField("First Name")
    last_name = StringField("Last Name")
    username = StringField(
        "username",
        [validators.DataRequired()],
    )
    email = StringField(
        "Email Address",
        [
        validators.DataRequired(),
        validators.Email(),
        validators.Length(min=6, max=200),
        ],
        filters=[lambda data: data and data.lower()],
    )


class RegistrationForm(UserBaseForm):
    password = PasswordField(
        "New Password",
        [
        validators.DataRequired(),
        validators.EqualTo("confirm", message="Passwords must match"),
        ],
    )
    confirm = PasswordField("Repeat Password")
    submit = SubmitField("Register")


class LoginForm(Form):
    username = StringField(
        "username",
        [validators.DataRequired()],
    )
    password = PasswordField(
        "Password",
        [validators.DataRequired()],
    )
    submit = SubmitField("Login")