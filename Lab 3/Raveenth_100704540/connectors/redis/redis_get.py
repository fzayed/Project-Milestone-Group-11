import redis        # pip install redis
ip='34.135.147.252';
r = redis.Redis(host=ip, port=6379, db=0, password='SOFE4630U')
v=r.get('OntarioTech');
with open("./recieved.jpg", "wb") as f:
    f.write(v);
