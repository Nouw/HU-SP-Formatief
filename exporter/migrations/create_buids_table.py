from sqlalchemy import Column, Boolean, ForeignKey, Integer, func, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from exporter.migrations.create_sessions_table import Sessions
from exporter.migrations.create_profiles_table import Profiles

Base = declarative_base()


class Buids(Base):
    __tablename__ = "buids"
    id = Column(Integer(), primary_key=True)
    session_id = Column(Integer, ForeignKey(Sessions.id_pk))
    profile_id = Column(Integer, ForeignKey(Profiles.id_pk))

    def __repr__(self):
        return 'id: {}'.format(self.id)
