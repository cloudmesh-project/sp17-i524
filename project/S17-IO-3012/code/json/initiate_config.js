rs.initiate(
  {
    _id: "repset_config",
    configsvr: true,
    members: [
      { _id : 0, host : "{{inventory_hostname}}:27019" }
    ]
  }
)
