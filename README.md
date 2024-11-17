# Quran API

[![Django CI](https://github.com/youzarsiph/quran-api/actions/workflows/django.yml/badge.svg)](https://github.com/youzarsiph/quran-api/actions/workflows/django.yml)
[![Code Style](https://github.com/youzarsiph/quran-api/actions/workflows/black.yml/badge.svg)](https://github.com/youzarsiph/quran-api/actions/workflows/black.yml)
[![Linting](https://github.com/youzarsiph/quran-api/actions/workflows/ruff.yml/badge.svg)](https://github.com/youzarsiph/quran-api/actions/workflows/ruff.yml)
[![License](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)

## Overview

The Quran API provides a robust set of RESTful endpoints designed to digitalize and facilitate access to the Quranic text. Leveraging Python, Django, and Django Rest Framework (DRF), the API supports multilingual translations and transliterations, ensuring comprehensive and user-friendly data retrieval.

## Key Features

- **Data Categorization:** Organized structure including chapters, verses, juz, and more.
- **Multilingual Support:** Accessible translations and transliterations in multiple languages.
- **Advanced Search and Filter Options:** Facilitating efficient data retrieval and exploration.
- **Pagination:** Optimized for handling large datasets.
- **Secure Authentication:** Employs Django's authentication mechanisms for data protection.

## Getting Started

### Prerequisites

Ensure you have the following installed on your system:

- Python 3.10 or higher
- Django 5.0 or higher

### Installation

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/youzarsiph/quran-api.git
   cd quran-api
   ```

2. **Set Up a Virtual Environment:**

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. **Install Dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

### Integration

1. **Integrate the API into a Django Project:**

   - Start a new Django project:

     ```bash
     django-admin startproject mysite
     ```

   - Move the `quran_api` directory into the `mysite` directory:

     ```bash
     mv quran_api mysite/quran_api
     ```

2. **Configure the Django Settings:**

   - Add the Quran API and related applications to `INSTALLED_APPS` in `mysite/settings.py`:

     ```python
     INSTALLED_APPS = [
         # Core applications
         "quran_api",
         "quran_api.chapters",
         "quran_api.groups",
         "quran_api.juz",
         "quran_api.pages",
         "quran_api.verses",
         # Multilingual features
         "quran_api.i18n.languages",
         "quran_api.i18n.translations",
         "quran_api.i18n.transliterations",
         # Required libraries
         "corsheaders",
         "drf_redesign",
         "rest_framework",
         "django_filters",
         # Default Django applications
         "django.contrib.admin",
         "django.contrib.auth",
         "django.contrib.contenttypes",
         "django.contrib.sessions",
         "django.contrib.messages",
         "django.contrib.staticfiles",
     ]
     ```

   - Update `MIDDLEWARE` in `mysite/settings.py`:

     ```python
     MIDDLEWARE = [
         "django.middleware.security.SecurityMiddleware",
         "django.contrib.sessions.middleware.SessionMiddleware",
         "corsheaders.middleware.CorsMiddleware",
         "django.middleware.common.CommonMiddleware",
         "django.middleware.csrf.CsrfViewMiddleware",
         "django.contrib.auth.middleware.AuthenticationMiddleware",
         "django.contrib.messages.middleware.MessageMiddleware",
         "django.middleware.clickjacking.XFrameOptionsMiddleware",
     ]
     ```

   - Enable Cross-Origin Resource Sharing (CORS) for development:

     ```python
     CORS_ALLOW_ALL_ORIGINS = True
     ```

   - Customize REST framework settings in `mysite/settings.py` (optional):

     ```python
     REST_FRAMEWORK = {
         "DEFAULT_FILTER_BACKENDS": [
             "rest_framework.filters.SearchFilter",
             "rest_framework.filters.OrderingFilter",
             "django_filters.rest_framework.DjangoFilterBackend",
         ],
         "DEFAULT_AUTHENTICATION_CLASSES": [
             "rest_framework.authentication.BasicAuthentication",
             "rest_framework.authentication.SessionAuthentication",
             "rest_framework.authentication.TokenAuthentication",
         ],
         "DEFAULT_PAGINATION_CLASS": "rest_framework.pagination.LimitOffsetPagination",
         "PAGE_SIZE": 25,
     }
     ```

3. **Incorporate API URLs into Project:**

   - Modify `mysite/urls.py` to include the API endpoints:

     ```python
     from django.contrib import admin
     from django.urls import path, include

     urlpatterns = [
         path("admin/", admin.site.urls),
         path("api/", include("quran_api.urls")),
         path("api/auth/", include("rest_framework.urls")),
         # Multilingual features
         path("i18n/", include("quran_api.i18n.urls")),
     ]
     ```

4. **Apply Database Migrations:**

   ```bash
   python manage.py migrate
   ```

5. **Create an Administrative User:**

   ```bash
   python manage.py createsuperuser
   ```

6. **Launch the Development Server:**

   ```bash
   python manage.py runserver
   ```

### Usage

- **API Documentation:** Access the API documentation via `http://localhost:8000/api/`.
- **Authentication:** Secure API access using Django's built-in authentication mechanisms.

## Contributing

We welcome contributions from the community! To contribute, please refer to the [Contribution Guidelines](CONTRIBUTING.md) and adhere to our [Code of Conduct](CODE_OF_CONDUCT.md).

1. **Fork the Repository.**
2. **Create a Feature Branch:** `git checkout -b feature/AmazingFeature`
3. **Commit Your Changes:** `git commit -m 'Add some AmazingFeature'`
4. **Push to Branch:** `git push origin feature/AmazingFeature`
5. **Submit a Pull Request.**

## License

This project is distributed under the MIT License. For details, see the [LICENSE](LICENSE) file.

## Contact

- **Maintainer:** Yousuf Abu Shanab
- **GitHub:** [youzarsiph](https://github.com/youzarsiph)

We invite you to utilize this project in your endeavors and contribute to its development by sharing your expertise and innovations. May this resource serve you well.
