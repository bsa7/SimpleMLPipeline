const _getEnv = (name) => {
  return process.ENV[name]
}

conn = new Mongo();
db = conn.getDB(_getEnv("MONGO_INITDB_DATABASE"));
db.createUser(
  {
    user: _getEnv("MONGO_USER"),
    pwd: cat(_getEnv("MONGO_PASSWORD_FILE")),
    roles: [
      "readWrite", "dbAdmin"
    ]
  }
);

db.log.insertOne({"message": "Database created.======================================================================="});
