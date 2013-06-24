from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy import Column, Integer, String, Sequence, ForeignKey, Float
from sqlalchemy.orm import relationship, backref

Base = declarative_base()

class Orthography(Base):
    __tablename__ = 'orthographies'
    
    id = Column(Integer, Sequence('orthography_id_seq'), primary_key = True)
    spelling = Column(String(100))
    frequency = Column(Float)

class Transcription(Base):
    __tablename__ = 'transcriptions'
    
    id = Column(Integer, Sequence('transcription_id_seq'), primary_key = True)
    phones = Column(String(100))
    neighbourhood_density = Column(Integer)
    
spellings_table = Table('spelledas', Base.metadata,
            Column('left_id', Integer, ForeignKey('left.id')),
            Column('right_id', Integer, ForeignKey('right.id')))
    
pronunciations_table = Table('pronouncedas', Base.metadata,
            Column('left_id', Integer, ForeignKey('left.id')),
            Column('right_id', Integer, ForeignKey('right.id')))
    
class Word(Base):
    __tablename__ = 'words'
    
    id = Column(Integer, Sequence('word_id_seq'), primary_key = True)
    spellings = relationship("Orthography",
                            secondary= spellings_table,
                            backref = "words_spelledas")
    pronunciations = relationship("Transcription",
                            secondary= pronunciations_table,
                            backref = "words_pronouncedas")
    
