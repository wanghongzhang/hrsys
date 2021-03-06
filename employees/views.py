from material.frontend.views import ModelViewSet

from . import models


class EmployeeViewSet(ModelViewSet):
    model = models.Employee


class AttendanceViewSet(ModelViewSet):
    model = models.Attendance


class TechnologyViewSet(ModelViewSet):
    model = models.Technology


class CareerViewSet(ModelViewSet):
    model = models.CareerHistory
