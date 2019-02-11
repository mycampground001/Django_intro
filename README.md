# Django

## 1. 시작하기

1. 프로젝트 시작하기

   ```bash
   $ django-admin startproject 프로젝트이름
   ```

   아래와 같이 프로젝트 구조가 만들어 진다.

   ```w
   django_intro/
   	django_intro/
   		__init__.py
   		settings.py
   		urls.py
   		wsgi.py
   	db.sqlite3
   	manage.py
   ```

   ```python
   sudo apt-get install tree
   tree
   ```

   입력하면 tree형태로 나옴

   지금부터 pwd(현재 디렉토리)는 `~/workspace/django_intro` 이다.

   

2. 서버 실행하기

   - `settings.py`

     ```python
     ALLOWED_HOST = ['*'] #모든 호스트를 열겠다.
     # C9에서는 host - 0.0.0.0, port - 8080만 활용할 수  있기 때문에 위와 같이 설정한다.
     ```

   ```bash
   ~/workspace/django_intro $ python manage.py runserver 0.0.0.0:8080 
   ```

   앞으로 모든 장고 명령어는 프로젝트 만들 때를 제외하고 `python manage.py` 를 활용한다. 따라서 반드시 `pwd` 와 `ls` 를 통해서 현재 bash(터미널) 위치를 확인해야 한다.



## 2. Hello, Django

> Django 프로젝트는 여러가지 app의 집합이다.
>
> 각각의 app은 MTV 패턴으로 구성되어 있다.
>
> M (Model) : 어플리케이션의 핵심 로직의 동작을 수행한다.
>
> T (Template) : 사용자에게 결과물을 보여준다.
>
> V (View) : 모델과 템플릿의 동작을 제어한다. (모델의 상태를 변경하거나 값을 가져오고, 템플릿에 값을 전달하기 등)
>
> **일반적으로 MVC 패턴으로 더 많이 사용된다.**

### 1. 기본 로직

앞으로 우리는 1. 요청 url 설정(`urls.py`) 2. 처리 할 view 설정(view.py) 3. 결과 보여줄 template 설정

(`templates/`) 으로 작성할 것이다.

1. url 설정

   ```python
   # django_intro/urls.py
   from django.contrib import admin
   from django.urls import path
   # home 폴더 내에 있는 views.py를 불러온다.
   from home import views
   
   urlpatterns = [
       path('admin/', admin.site.urls),
       # 요청이 home/으로 오면, views의 index 함수를 실행시킨다.
       path('home/',views.index)
   ]
   ```

2. View 설정

   ```python
   # home/views.py
   from django.shortcuts import render, HttpResponse
   
   # Create your views here.
   def index(request):
       return HttpResponse('hello, django!')
   ```

   - 주의할 점은 선언된 함수에서 `request`를 인자로 받아야 한다.
     - request 는 사용자(클라이언트)의 요청 정보와 서버에 대한 정보가 담겨 있다.
     - Django 내부에서 해당 함수를 호출하면서 정보를 넘겨주기 때문에 반드시 명시해줘야 한다.

## 3. Template (MTV - T)

> Django 에서 활용되는 Template은 DTL(Django Template Language)이다.
>
> Jinja2와 문법이 유사하다.

1. 요청 url 설정

   ```python
   path('home/dinner/',views.dinner)
   ```

2. view 설정

   ```python
   def dinner(request):
       box = ['a','b','c','d']
       dinner = random.choice(box)
       return render(request, 'dinner.html',{'dinner':dinner})
   ```

   - Template을 리턴하려면, `render` 를 사용하여야 한다.
     - `request`(필수)
     - `template 명` (필수)
     - `template에서 쓸 변수` (선택) : {'item': item} : `dictionary` 타입으로 구성해야 한다.

3. Template 설정

   ```bash
   $ mkdir home/templates
   $ touch home/templates/dinner.html
   ```

   ```html
   <!-- home/templates/dinner.html-->
   <h1>
       {{dinner}}
   </h1>
   ```



## 4. Variable Routing

1. url 설정

   ```python
   path('home/you/<name>',views.you)
   path('home/cube/<int:num>', views.cube)
   ```

2. view 파일 설정

   ```python
   def you(request, name):
       return render(request, 'you.html',{'name':name})
   
   def cube(request, num):
       return render(request,'cube.html',{'num':num,'res':num**3})
   ```

3. 템플릿 파일 설정

   ```django
   <h1> {{name}}, 안녕!!</h1>
   ```
 ![image_from_ios](/django_intro/home/image/image_from_ios.jpg)
   

   