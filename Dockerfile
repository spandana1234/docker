FROM centos:centos7
# install python
RUN yum -y update && yum -y install gcc libffi-devel cyrus-sasl-devel krb5-devel python36-devel \
    openldap-devel openssl-devel uwsgi python3-pip python3-virtualenv \
    uwsgi-logger-file nginx vim python3-setuptools python3-wheel gcc-c++ unixODBC unixODBC-devel
#RUN yum -y install python3.6
#RUN /bin/bash -c 'pip3 install --upgrade pip'
#RUN /bin/bash -c 'pip3 install virtualenv' 

# add new user 'oncall'
#RUN useradd -m -s /bin/bash api_user

RUN mkdir ./project
# copy required scripts to required location

COPY . ./project
#COPY manage.py ./app/


# use this directory
WORKDIR ./project
# append permissions to user 'oncall'
#RUN chown -R api_user:api_user .
# run as 'oncall' user
#USER api_user


#RUN /bin/bash -c 'virtualenv -p /usr/bin/python3.6 ./virtenv'
#RUN /bin/bash -c 'source ./virtenv/bin/activate'

    
RUN pip3 install flask
RUN /bin/bash -c 'pip3 install flask-restplus'
RUN /bin/bash -c 'pip3 install Flask-Migrate'
RUN /bin/bash -c 'pip3 install pyjwt'
RUN /bin/bash -c 'pip3 install Flask-Script'
RUN /bin/bash -c 'pip3 install flask-testing'
RUN /bin/bash -c 'pip3 install flask-marshmallow'
RUN /bin/bash -c 'pip3 install marshmallow-sqlalchemy'
RUN /bin/bash -c 'pip3 install Flask-SQLAlchemy'
RUN /bin/bash -c 'pip3 install psycopg2-binary'


# create ENV variables
ENV LANG en_US.UTF-8
EXPOSE 5000

# command that has to be xecuted
CMD ["bash", "-c", "python3.6 manage.py run "]
