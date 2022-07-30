1. Install docker
2. Install docker-compose
3. docker-compose up -d
4. docker exec -it my_postgres psql -U postgres -c "create database expenser"
5. docker exec -it my_postgres psql expenser -U postgres -f /root/Expenser.sql
6. docker exec -it my_postgres psql expenser -U postgres -c "\dt"
