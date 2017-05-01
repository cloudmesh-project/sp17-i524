db.getSiblingDB("admin").auth("cluster_admin_user", "cluster_admin_password" )
use mlb
db.pitches.getShardDistribution()
