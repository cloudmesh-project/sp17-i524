db.getSiblingDB("admin").createUser(
  {
    user: "admin_user",
    pwd: "admin_password",
    roles: [ { role: "userAdminAnyDatabase", db: "admin" } ]
  }
)

db.getSiblingDB("admin").auth("admin_user", "admin_password" )

db.getSiblingDB("admin").createUser(
  {
    "user" : "cluster_admin_user",
    "pwd" : "cluster_admin_password",
    roles: [ { "role" : "clusterAdmin", "db" : "admin" } ]
  }
)

db.getSiblingDB("admin").createUser(
  {
    "user" : "user1",
    "pwd" : "user1_password",
    roles: [ { "role" : "readWrite", "db" : "mlb" } ]
  }
)
