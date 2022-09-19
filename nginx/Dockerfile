FROM nginx:1.21-alpine

RUN mkdir /opt/webapp
RUN mkdir /opt/webapp/static
COPY static /opt/webapp/static

RUN rm /etc/nginx/conf.d/default.conf
COPY nginx.conf /etc/nginx/conf.d