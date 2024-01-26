import pytest
import time
from model_bakery import baker
from rest_framework.test import APIClient
from students.models import Course, Student



@pytest.fixture
def client():
    return APIClient()

@pytest.fixture
def course_factory():
    def factory(*args, **kwargs):
        return baker.make(Course, *args, **kwargs)
    return factory

@pytest.fixture
def student_factory():
    def factory(*args, **kwargs):
        return baker.make(Student, *args, **kwargs)
    return factory





# Проверка получения первого курса (retrieve-логика)
@pytest.mark.django_db
def test_get_course(client, course_factory):
    course = course_factory()
    response = client.get("/api/v1/courses/")
    data = response.json()
    assert response.status_code == 200
    assert data[0]["name"] == course.name


# Проверка получения списка курсов (list-логика):    
@pytest.mark.django_db
def test_get_courses(client,course_factory):
    course = course_factory(_quantity=10)
    response = client.get("/api/v1/courses/")
    data = response.json()
    assert response.status_code == 200
    for i, m in enumerate(data):
        assert m["name"] == course[i].name

# Проверка фильтрации списка курсов по id
@pytest.mark.django_db
def test_get_courses_by_id(client,course_factory):
    course = course_factory(_quantity=10)
    response = client.get("/api/v1/courses/",{"id":course[2].id},format="json")
    data = response.json()
    assert response.status_code == 200
    assert data[0]["id"] == course[2].id
# Проверка фильтрации списка курсов по name
@pytest.mark.django_db
def test_get_courses_by_name(client,course_factory):
    course = course_factory(_quantity=10)
    response = client.get("/api/v1/courses/",{"name":course[2].name},format="json")
    data = response.json()
    assert response.status_code == 200
    assert data[0]["name"] == course[2].name

# Тест успешного создания курса
@pytest.mark.django_db
def test_create_course(client):
    response = client.post("/api/v1/courses/",{"name":"test"},format="json")
    data = response.json()
    print(data)
    assert response.status_code == 201
    

# Тест успешного обновления курса
@pytest.mark.django_db
def test_upgrade_course(client,course_factory):
    course = course_factory()
    response = client.patch(f"/api/v1/courses/{course.id}/",{"name":course.name},format="json")
    assert response.status_code == 200    

# Тест успешного удаления курса
@pytest.mark.django_db
def test_delete_course(client,course_factory):
    course = course_factory()
    response = client.delete(f"/api/v1/courses/{course.id}/",format="json")
    assert response.status_code == 204   
