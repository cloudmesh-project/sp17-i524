rs.initiate(
  {
    _id: "repset_config",
    configsvr: true,
    members: [
      { _id : 0, host : "lmundia-020:27019" }
    ]
  }
)
