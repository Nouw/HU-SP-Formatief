from sqlalchemy import Column, Boolean, String, Integer, func, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class Sessions(Base):
    __tablename__ = "sessions"
    id_pk = Column(Integer(), primary_key=True)
    id = Column(String(255))
    session_start = Column(DateTime)
    session_end = Column(DateTime)
    browser_name = Column(String(255))
    os_name = Column(String(255))
    is_mobile_flag = Column(Boolean)
    is_pc_flag = Column(Boolean)
    is_tablet_flag = Column(Boolean)
    is_email_flag = Column(Boolean)
    device_family = Column(String(255))
    device_brand = Column(String(255))
    device_model = Column(String(255))

    children = relationship("Buids")

    def __repr__(self):
        return 'id: {}'.format(self.id_pk)
