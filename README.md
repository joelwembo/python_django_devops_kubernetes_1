# Django DevOps with Kubernetes: Django Deployment to Azure AKS using CI/CD Pipeline with Python, Terraform, GitHub Actions, and Istio Integration 
## Automating Django , Celery , Redis and postgres deployment to AWS EC2 / EKS / ECS / Azure AKS using Terraform ( Complete Guide)

![image](https://github.com/user-attachments/assets/51952bdc-5017-4203-a191-cefcf07ac0f7)

- [@Joel O. Wembo](https://www.joelotepawembo.com)
- [@twitter](twitter.com/joelwembo1)
- [@linkedin](https://www.linkedin.com/in/joelotepawembo)

## Introduction
In this article, we explore the integration of Terraform, Kubernetes, and Azure CLI within a GitHub Actions workflow to automate the django deployment and management of cloud infrastructure. With a focus on best practices for Continuous Integration and Continuous Deployment (CI/CD) pipelines, we demonstrate how to securely manage Azure credentials, configure Kubernetes access, and execute Azure CLI commands. This guide provides practical examples and step-by-step instructions, empowering DevOps professionals to streamline their workflows and ensure reliable deployments across cloud environments.


### Prerequisites:
Before we get into the good stuffs, first we need to make sure we have the required services on our local machine or dev server, which are:

- Basic knowledge of Django
- AWS Account
- Github Account
- AWS CLI installed and configured.
- ECS CLI
- Docker installed locally.
- Typescript installed
- Postman
- Python 3
- NPM
- NodeJS
- Terraform
- A Domain name Hosted from any domain name provider ( Ex: AWS Route 53 )
- Basic familiarity with YAML and GitHub workflows.
- A Django project hosted in a GitHub repository
- Basic knowledge of HTML or React
- Any Browser for testing
- Intermediate knowledge in Serverless Computing ( Ex : AWS Lambda , ECS,..)

You can follow along with this source code:
GitHub - joelwembo/django-multitenant-saas-ecommerce-kubernetes: Django Multi-tenant …
Django Multi-tenant , microservices , Kubernetes, Jenkins, Github Actions and Multiple Databases using docker, bash…
github.com

## Steps

## Step 1: Create a virtual environment to hold all pip libraries installations

If you don’t have virtualenv installed, you can install it by running the following command in your CMD after Python was installed:

Create virtual environment for Python
    ```
    python3 -m venv venv 
    or
    python -m venv venv
    ```
## Step 2 : Activate the environment:

```
source ./venv/bin/activate
source ./venv/bin/deactivate ( To Deactivate )
or
.\venv\Scripts\activate
```

### Step 3: Create project folder
268770
```
mkdir app
```
## Step 4: Install Django

pip install django
## Step 5: Create a new Django project inside the project folder

A Django app is a self-contained component of a Django project. It is a module that provides specific functionality, such as handling authentication, managing blog posts, or serving an API. An app should represent a single, specific functionality or purpose within the overall website.

django-admin startproject django-multitenant-saas-ecommerce-kubernetes
## Step 6: Create a new test app:

within the django project using the following command:
```
python manage.py startapp testapp
```
***Adding a new app into the project***
```
python manage.py startapp home apps/home
python manage.py startapp finances apps/finances
python manage.py startapp snippets apps/snippets
python manage.py startapp users apps/users
python manage.py startapp payments apps/payments
python manage.py startapp products apps/products
```
 'apps.home',
    'apps.snippets',
    'apps.users',
    'apps.finances',
    'apps.payments',
    'apps.products',


## Step 7 : Execute ORM Data Migrations:
```
python manage.py makemigrations
```
```
python manage.py migrate
```

## Step 8: Launch the django development server
```
python manage.py runserver
```

## Step 9:  create admin user

```
python manage.py createsuperuser
```
## start using shell 
```
bash ./server-entrypoint.sh
```

# Docker
 ```
bash ./run.sh
http://127.0.0.1:8585/
 ```

# API Docs
 ```
http://127.0.0.1:8585/swagger/
 ```
 [@Swagger](http://127.0.0.1:8585/swagger/)

# Data Browser

http://127.0.0.1:8585/data-browser/
![image](https://github.com/joelwembo/django-restful-api-postgres-kubernetes-poc/assets/19718580/83a0f788-36ea-4bb1-a626-17c2154bd512)


# GraphQL
![Alt text](image.png)
http://127.0.0.1:8585/graphql

# Extensions
python manage.py show_urls
python manage.py graph_models finances -a -o finances_models.png

# wagtail

# Django ledger
 ```
pip install pipenv (globally)
 ```
To activate this project's virtualenv, run pipenv shell.
Alternatively, run a command inside the virtualenv with pipenv run.
 ```
pipenv install django-ledger[graphql,pdf]
 ```
  ```
python manage.py test django_ledger
 ```


# Multi tenant Settings

 ```
pip install -r requirements.txt
 ```
  ```
python manage.py makemigrations finances
 ```
  ```
python manage.py makemigrations app
 ```

 ```
python manage.py migrate finances
 ```
  ```
python manage.py migrate app
 ```
tenant = Client(schema_name="test", name="test Company")

domain = Domain(domain="btest.localhost", tenant=tenant, is_primary=True)


# A step-by-step guide for AWS EC2 provisioning using Terraform: How to set up an Nginx reverse proxy with SSL using Certbot for a Django application running in Ubuntu server  - Part 17



ssh -i id_rsa.pem ubuntu@20.28.8.41

sudo certbot certonly --nginx -d prodxcloud.io -d *.prodxcloud.io -m joelwembo@outlook.com --agree-tos --preferred-challenges dns

if error chose this one

sudo certbot certonly --manual --preferred-challenges=dns -d prodxcloud.io -d *.prodxcloud.io -m joelwembo@outlook.com --agree-tos

## Docker and Docker-compose

docker-compose -f docker-compose-dev.yaml up 

# Ansible

- Generate SSH / Copy  / Replace SSH Key Pair for your ec2

ssh-keygen -t rsa -b 4096 -f ~/.ssh/id_rsa
cat ~/.ssh/id_rsa
chmod 400 ~/.ssh/id_rsa.pem

rm ~/.ssh/id_rsa
vim ~/.ssh/id_rsa.pem
chmod 400 ~/.ssh/id_rsa.pem

- Inventory file
/etc/ansible/inventory

[hosts_to_add_key]
20.28.8.41 ansible_ssh_port=22  ansible_user=ubuntu

[hosts_to_add_key:vars]
ansible_ssh_common_args="-o StrictHostKeyChecking=no"

- ansible.cfg
/etc/ansible/ansible.cfg

 [defaults]
inventory =/etc/ansible/inventory
host_key_checking = False
deprecation_warnings = False
remote_user = ubuntu
# Increase connection attempts in case of temporary network issues
retries = 3
# Optional: Specify SSH private key file
private_key_file = ~/.ssh/id_rsa

Ansible Commands :
root@ip-10-0-2-236:/etc/ansible# ansible all --list-hosts
  hosts (1):
    20.28.8.41

ansible-inventory --list -y

root@ip-10-0-2-236:/etc/ansible# ansible-inventory --list -y
all:
  children:
    hosts_to_add_key:
      hosts:
        20.28.8.41:
          ansible_ssh_common_args: -o StrictHostKeyChecking=no
          ansible_ssh_port: 22
          ansible_user: ubuntu
    ungrouped: {}

ansible all -m ping -u root

root@ip-10-0-2-236:~# ansible all -m ping -u root
20.28.8.41 | SUCCESS => {
    "ansible_facts": {
        "discovered_interpreter_python": "/usr/bin/python3"
    },
    "changed": false,
    "ping": "pong"
}

Next, write the playbook

 - ansible-playbook -i hosts deploy_nginx.yml
 - ansible-playbook -i deploy_nginx.yml # host in default

ANSIBLE_LOCALHOST_WARNING=False \
ANSIBLE_INVENTORY_UNPARSED_WARNING=False \
ansible-playbook deploy_nginx.yaml --tags deploy_nginx


## EKS Deployment
 # Deploy DB
kubectl apply -f pg_secrets.yaml
kubectl apply -f pg_storage.yaml
kubectl apply -f pg_deployment.yaml
kubectl apply -f pg_service.yaml
kubectl get pods

# Deploy environment ConfigMap Configuration
kubectl create -f .\django-env-configmap.yaml
configmap/django-env-configmap created

kubectl describe configmaps django-env-configmap
# Deploy Django image
kubectl apply -f deployment-django-dev.yaml

# Create django service
kubectl apply -f prodxcloud-django-web-dev-service.yaml

# For more information about the author visit
https://blog.devgenius.io/django-devops-with-kubernetes-django-deployment-to-azure-aks-using-ci-cd-pipeline-with-terraform-76c138be2ada

- [@Joel O. Wembo](https://www.joelotepawembo.com)
- [@twitter](twitter.com/joelwembo1)
- [@linkedin](https://www.linkedin.com/in/joelotepawembo)

Thank you for Reading !! 🙌🏻, see you in the next article.🤘