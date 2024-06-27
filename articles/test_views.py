from django.test import TestCase

# Create your tests here.
import pytest
from django.urls import reverse
from django.contrib.auth import get_user_model
from .models import Article

@pytest.mark.django_db
def test_home_page_status_code(client):
    # Create a test user
    newuser = get_user_model().objects.create_user(username='testuser', password='testpassword')
    # Log in the test client
    client.login(username='testuser', password='testpassword')
    response = client.get(reverse('article_list'))
    assert response.status_code == 200

@pytest.mark.django_db
def test_about_page_status_code(client):
    user = get_user_model().objects.create_user(username='testuser', password='testpassword')
    
    # Log in the test client
    client.login(username='testuser', password='testpassword')
    
    # Create a test article
    article = Article.objects.create(title='Test Article', body='Test Content', author=user)
    
    # Perform the request
    url = reverse('article_detail', args=[article.pk])
    response = client.get(url)
