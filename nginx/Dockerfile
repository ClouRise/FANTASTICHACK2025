FROM nginx:alpine

# Удаляем дефолтные конфиги
RUN rm -rf /etc/nginx/conf.d/*

# Копируем наши конфиги
COPY nginx.conf /etc/nginx/nginx.conf
COPY conf.d/app.conf /etc/nginx/conf.d/app.conf

# Права для статики
RUN chown -R nginx:nginx /usr/share/nginx/html && \
    chmod -R 755 /usr/share/nginx/html