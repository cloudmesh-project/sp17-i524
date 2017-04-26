db.getSiblingDB("admin").auth("cluster_admin_user", "cluster_admin_password" )
sh.enableSharding("mlb")
use admin
db.runCommand({ shardCollection: "mlb.pitches", key: { pitchID: 1 } })
