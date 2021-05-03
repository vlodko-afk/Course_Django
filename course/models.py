from django.db import models, IntegrityError, DataError
from  django.core.validators import MinLengthValidator

class Course(models.Model):

    name = models.CharField(max_length=30)
    description = models.TextField()
    start_course = models.DateTimeField(null= True)
    end_course = models.DateTimeField(null= True)
    count = models.IntegerField()

    def get_absolute_url(self):
        return f'/'

    def __str__(self):
        return str(self.to_dict())[1:-1]

    def __repr__(self):
        return f'{self.__class__.__name__}(id={self.id})'
    
    @staticmethod
    def get_by_id(course_id):
        try:
            return Course.objects.get(id=course_id)
        except Course.DoesNotExist:
            pass
    
    @staticmethod
    def delete_by_id(course_id):
        try:
            course = Course.objects.get(id=course_id)
            course.delete()
            return True
        except Course.DoesNotExist:
            # LOGGER.error("User does not exist")
            pass
        return False
    
    @staticmethod
    def create(name, description, start_course, end_course, count):
        """
        param name: Describes name of the course
        type name: str max_length=128
        param description: Describes description of the course
        type description: str
        param count: Describes count of course
        type count: int 
        start course: data start course
        end course: data end course
        :return: a new course object which is also written into the DB
        """
        course = Course(name = name, description = description, start_course = start_course, end_course = end_course, count = count)
        try:
            course.save()
            return book
        except (IntegrityError, AttributeError, DataError):
            # LOGGER.error("Wrong attributes or relational integrity error")
            pass

    def to_dict(self):
       
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'start_course': self.start_course,
            'end_course': self.end_course,
            'count': self.count,
        }

    def update(self, name = None, description = None, start_course = None, end_course = None, count = None):

        if name:
            self.name = name
        if description:
            self.description = description
        if start_course:
            self.start_course = start_course
        if end_course:
            self.end_course = end_course
        if count:
            self.count = count
        self.save()

    @staticmethod
    def get_all():
        """
        returns data for json request with QuerySet of all course
        """
        all_course = Course.objects.all()
        return list(all_course)