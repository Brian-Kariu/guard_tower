"""Apps forms."""
from flask_wtf import FlaskForm
from wtforms import StringField, URLField
from wtforms.validators import Length, URL, DataRequired

from guard_tower.user.models import User



class CreateAppForm(FlaskForm):
    """Create App Form"""

    name = StringField(
        "name", validators=[DataRequired(), Length(min=3, max=100)]
    )
    url = URLField("url", validators=[DataRequired(), URL(require_tld=True, allow_ip=False)])
   