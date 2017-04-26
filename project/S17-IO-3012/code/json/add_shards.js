db.getSiblingDB("admin").auth("cluster_admin_user", "cluster_admin_password" )
sh.addShard("repset_shard1/129.114.32.173:27018")
