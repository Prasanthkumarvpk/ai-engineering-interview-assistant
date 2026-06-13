from app.db.base import Base
from app.models.user import User
from app.models.resume import Resume
from app.models.interview import Interview
from app.models.question import Question
from app.models.answer import Answer
from app.models.feedback import Feedback
from app.models.roadmap import Roadmap

# In the config function:
target_metadata = Base.metadata